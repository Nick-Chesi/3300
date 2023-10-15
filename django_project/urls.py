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

]
