from django.contrib import admin
from django.urls import path, include
from portfolio_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #connect path to portfolio_app urls
    path('', include('portfolio_app.urls')),
    path('students/', views.StudentListView.as_view(), name= 'students'),
    path('student/<int:pk>', views.StudentDetailView.as_view(), name='student-detail'),
    path('portfolio/<int:pk>/', views.PortfolioDetailView.as_view(), name='portfolio-detail'),
    path('projects/<int:pk>/edit/', views.editProject, name='edit_project'),
    path('projects/<int:pk>/delete/', views.deleteProject, name='delete_project'),
    path('portfolio/<int:pk>/edit/', views.editPortfolio, name='edit_portfolio'),
    path('portfolio/<int:pk>/delete/', views.deletePortfolio, name='delete_portfolio'),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
]
