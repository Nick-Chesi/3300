from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from .forms import ProjectForm
from .models import Student, Project, Portfolio, ProjectsInPortfolio
# Create your views here.
def index(request):
    student_active_portfolios = Student.objects.select_related('portfolio').all().filter(portfolio__is_active=True)
    print("active portfolio query set", student_active_portfolios)
    return render( request, 'portfolio_app/index.html', {'student_active_portfolios':student_active_portfolios})

class ProjectListView(generic.ListView):
    model = Project
    template_name = 'portfolio_app/project_list.html'

class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = 'portfolio_app/project_detail.html'

class StudentListView(generic.ListView):
    model = Student
    template_name = 'portfolio_app/student_list.html' 

class StudentDetailView(generic.DetailView):
    model = Student
    template_name = 'portfolio_app/student_detail.html'

class PortfolioDetailView(generic.DetailView):
    model = Student
    template_name = 'portfolio_app/portfolio_detail.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        projects_associated = ProjectsInPortfolio.objects.filter(portfolio=self.object.portfolio).select_related('project')
        context['projects'] = [project_association.project for project_association in projects_associated]
        return context

def createProject(request, portfolio_id):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.portfolio_id = portfolio_id 
            project.save()
            return redirect('portfolio-detail', pk=portfolio_id)
    else:
        form = ProjectForm()
    return render(request, 'portfolio_app/create_project.html', {'form': form})
