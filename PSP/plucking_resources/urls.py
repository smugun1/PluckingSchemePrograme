from django.urls import path

from . import views

urlpatterns = [
    path('admin/', views.Admin, name='admin'),
    path('127.0.0.1:8000/admin/', views.Admin, name='/127.0.0.1/admin'),
    path('127.0.0.1:8000/adminresources-admin/', views.ResourcesAdmin,
         name='/127.0.0.1/resourcesadmin-admin'),
]
