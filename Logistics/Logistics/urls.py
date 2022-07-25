"""Logistics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from Driver import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('driver_detail/<int:pk>', views.driver_details),
    path('driver_detail/', views.driver_list),
    path('driver_create/', views.driver_create),
    path('driver_update/', views.driver_update),
    path('driver_delete/', views.driver_delete),
    
    

]
