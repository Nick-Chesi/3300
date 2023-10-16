from django.urls import path
from . import views
from .views import ProjectListView, ProjectDetailView 


urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
path('', views.index, name='index'),
path('projects/', ProjectListView.as_view(), name='project_list'),
path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
path('portfolio/<int:portfolio_id>/create_project/', views.createProject, name='create_project'),
path('projects/<int:pk>/delete/', views.deleteProject, name='delete_project'),
]
