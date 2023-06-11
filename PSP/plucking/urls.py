from django.urls import path
from django.views.generic import RedirectView
from . import views
from .views import PSPDashboard, chart_view

urlpatterns = [
    path('', views.FirstPage, name='first-page'),

    path('psp-dashboard', PSPDashboard, name='psp-dashboard'),
    path('psp-graphs', views.PSPGraphs, name='psp-graphs'),

    path('127.0.0.1:8000/resourcesexcell-admin/', views.Resourcesexcell,
         name='127.0.0.1/resourcesadmin-admin'),

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

    path('autofields-record/', views.AutoFieldsViewRetrieve, name='autofields-record'),
    path('autofields-update/', views.AutoFieldsViewUpdate, name='autofields-update'),
    path('autofields-create/', views.AutoFieldsViewCreate, name='autofields-create'),

    path('plucking-rounds-record/', views.PluckingRoundsViewRetrieve, name='plucking-rounds-record'),
    path('plucking-rounds-update/', views.PluckingRoundsViewUpdate, name='plucking-rounds-update'),
    path('plucking-rounds-create/', views.PluckingRoundsViewCreate, name='plucking-rounds-create'),

    path('plucking-cycle/', views.TeaPluckingCycleViewRetrieve, name='plucking-cycle'),
    path('plucking-cycle-update/', views.TeaPluckingCycleViewUpdate, name='plucking-cycle-update'),
    path('plucking-cycle-create/', views.TeaPluckingCycleViewCreate, name='plucking-cycle-create'),

    path('plucking-rounds/', views.PluckingRoundsViewRetrieve, name='plucking-rounds'),

    path('programmedscheme-update/<int:pk>/', views.ProgrammedSchemeUpdate, name='programmedscheme-update'),
    path('programmedscheme-delete/<int:pk>/', views.ProgrammedSchemeDelete, name='programmedscheme-delete'),

    path('roundsmonitor-edit/<int:pk>/', views.RoundsMonitorEdit, name='roundsmonitor-edit'),
    path('roundsmonitor-delete/<int:pk>/', views.RoundsMonitorDelete, name='roundsmonitor-delete'),

    path('fields-edit/<int:pk>/', views.FieldsEdit, name='fields-edit'),
    path('fields-delete/<int:pk>/', views.FieldsDelete, name='fields-delete'),

    path('autofields-edit/<int:pk>/', views.AutoFieldsEdit, name='autofields-edit'),
    path('autofields-delete/<int:pk>/', views.AutoFieldsDelete, name='autofields-delete'),

    path('teapluckingcycle-edit/<int:pk>/', views.TeaPluckingCycleEdit, name='teapluckingcycle-edit'),
    path('teapluckingcycle-delete/<int:pk>/', views.TeaPluckingCycleDelete, name='teapluckingcycle-delete'),

    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
]
