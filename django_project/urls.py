from django.contrib import admin
from django.urls import path, include
from portfolio_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
]
