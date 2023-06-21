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

    path('autofields-record/', views.AutoFieldsViewRetrieve, name='autofields-record'),
    path('autofields-update/', views.AutoFieldsViewUpdate, name='autofields-update'),
    path('autofields-create/', views.AutoFieldsViewCreate, name='autofields-create'),

    path('plucking-rounds-record/', views.PluckingRoundsViewRetrieve, name='plucking-rounds-record'),
    path('plucking-rounds-update/', views.PluckingRoundsViewUpdate, name='plucking-rounds-update'),
    path('plucking-rounds-create/', views.PluckingRoundsViewCreate, name='plucking-rounds-create'),


    path('growing-cycle/', views.GrowingCycleViewRetrieve, name='growing-cycle'),
    path('growing-cycle-update/', views.GrowingCycleViewUpdate, name='growing-cycle-update'),
    path('growing-cycle-create/', views.GrowingCycleViewCreate, name='growing-cycle-create'),

    path('plucking-rounds/', views.PluckingRoundsViewRetrieve, name='plucking-rounds'),

    path('division-zones/', views.DivisionZonesViewRetrieve, name='division-zones'),
    path('division-zones-update/', views.DivisionZonesViewUpdate, name='division-zones-update'),
    path('division-zones-create/', views.DivisionZonesViewCreate, name='division-zones-create'),
    path('division-inspect/', views.DivisionZonesViewInspect, name='division-inspect'),

    path('programmedscheme-update/<int:pk>/', views.ProgrammedSchemeUpdate, name='programmedscheme-update'),
    path('programmedscheme-delete/<int:pk>/', views.ProgrammedSchemeDelete, name='programmedscheme-delete'),

    path('roundsmonitor-edit/<int:pk>/', views.RoundsMonitorEdit, name='roundsmonitor-edit'),
    path('roundsmonitor-delete/<int:pk>/', views.RoundsMonitorDelete, name='roundsmonitor-delete'),

    path('autofields-edit/<int:pk>/', views.AutoFieldsEdit, name='autofields-edit'),
    path('autofields-delete/<int:pk>/', views.AutoFieldsDelete, name='autofields-delete'),


    path('growingcycle-edit/<int:pk>/', views.GrowingCycleEdit, name='growingcycle-edit'),
    path('growingcycle-delete/<int:pk>/', views.GrowingCycleDelete, name='growingcycle-delete'),

    path('division-zones-edit/<int:pk>/', views.DivisionZonesEdit, name='division-zones-edit'),
    path('division-zones-delete/<int:pk>/', views.DivisionZonesDelete, name='division-zones-delete'),

    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
]
