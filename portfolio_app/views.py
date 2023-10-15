from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
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
    model = Portfolio
    template_name = 'portfolio_app/portfolio_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve the associated projects for this portfolio
        projects = ProjectsInPortfolio.objects.filter(portfolio=self.object).values_list('project', flat=True)
        context['projects'] = Project.objects.filter(pk__in=projects)
        return context
