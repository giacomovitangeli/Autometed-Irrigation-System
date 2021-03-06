"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

urlpatterns = [
    path('', views.index, name = 'index'),
    path('update/', views.update_sensors, name = 'update_sensors'),
    path('update2/', views.update_motor, name ='motor_update'),
    path('graphics/', views.graphics, name = 'graphics'),
    path('gallery/', views.gallery, name = 'gallery'),
    path('update_graph/', views.update_graph, name='update_graph'),
    path('upadate3/', views.chek_motor_status, name ='motor_check'),


]
