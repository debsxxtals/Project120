"""
URL configuration for app2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from .views import MessageReceiver
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('', LoginView.as_view(template_name='login.html'), name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('api/messages/', MessageReceiver.as_view(), name='receive_message'),
    path('logout/', LoginView.as_view(template_name='login.html'), name='logout'),


]
