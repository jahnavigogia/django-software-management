"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from software import views
from software.views import hash_data_view
import os

urlpatterns = [
    path( '', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('software/', views.software_list, name='software_list'),
    path('software/add', views.add_software, name='add_software'),
    path('software/del', views.delete_software, name='del_software'),
    #path('documents/', views.document_list, name='document_list'),
    #path('documents/upload', views.upload_document, name='upload_document'),
    path('login/', views.User_LoginView.as_view(), name='login'),
    path('logout/', views.User_LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('accounts/profile/', views.profile, name='profile'),
    path('csrf_failure/', views.csrf_failure_view, name='csrf_failure'),
    path('my-template/', views.log, name='x'),
    path('hash-data/', hash_data_view, name='hash_data'),
    # Default view or redirect to another URL
]
