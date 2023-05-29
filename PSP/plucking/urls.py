from django.urls import path
from django.views.generic import RedirectView
from . import views
from .views import PSP, chart_view

urlpatterns = [
    path('', PSP, name='psp'),
    path('psp-graphs', views.PSPGraphs, name='psp-graphs'),
    path('psp-calc', views.PSPCalculator, name='psp-calc'),

    path('admin/', views.Admin, name='admin'),
    path('resources-admin/', views.AdminResources, name='resources-admin'),

    path('http://127.0.0.1:8000/resourcesexcell-admin/', views.Resourcesexcell, name='resourcesexcell-admin'),
    path('http:/127.0.0.1:8000/admin/', views.Admin, name='django-admin'),
    path('save/', views.save_changes, name='save_changes'),

    path('chart/', chart_view, name='chart_view'),

    path('programmedscheme-record/', views.ProgrammedSchemeViewRetrieve, name='programmedscheme-record'),
    path('programmedscheme-update/', views.ProgrammedSchemeViewUpdate, name='programmedscheme-update'),
    path('programmedscheme-create/', views.ProgrammedSchemeViewCreate, name='programmedscheme-create'),

    path('roundsmonitor-record/', views.RoundsMonitorViewRetrieve, name='roundsmonitor-record'),
    path('roundsmonitor-update/', views.RoundsMonitorViewUpdate, name='roundsmonitor-update'),
    path('roundsmonitor-create/', views.RoundsMonitoViewCreate, name='roundsmonitor-create'),

    path('fields-record/', views.FieldsViewRetrieve, name='fields-record'),
    path('fields-update/', views.FieldsViewUpdate, name='fields-update'),
    path('fields-create/', views.FieldsViewCreate, name='fields-create'),

    path('plucking-rounds/', views.PluckingRoundsViewRetrieve, name='plucking-rounds'),
    path('plucking-rounds-update/', views.PluckingRoundsViewUpdate, name='plucking-rounds-update'),

    path('programmedscheme-update/<int:pk>/', views.ProgrammedSchemeUpdate, name='programmedscheme-update'),
    path('programmedscheme-delete/<int:pk>/', views.ProgrammedSchemeDelete, name='programmedscheme-delete'),

    path('roundsmonitor-edit/<int:pk>/', views.RoundsMonitorEdit, name='roundsmonitor-edit'),
    path('roundsmonitor-delete/<int:pk>/', views.RoundsMonitorDelete, name='roundsmonitor-delete'),

    path('fields-edit/<int:pk>/', views.FieldsEdit, name='fields-edit'),
    path('fields-delete/<int:pk>/', views.FieldsDelete, name='fields-delete'),

    path('plucking-rounds-update/<int:pk>/', views.PluckingRoundsViewUpdate, name='plucking-rounds-update'),
    path('plucking-rounds-create/<int:pk>/', views.PluckingRoundsViewCreate, name='plucking-rounds-create'),

    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
]
