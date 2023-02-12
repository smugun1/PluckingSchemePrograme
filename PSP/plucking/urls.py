from django.urls import path
from . import views
from .views import Home

urlpatterns = [
    path('', Home, name='home'),
    path('plucking_requirement/', views.Plucking_requirements, name='plucking_requirement'),
    path('plucking_planner/', views.TeaPlucking_planner, name='plucking_planner'),
    path('plucking_planner_save_data/', views.TeaPlucking_planner_save_data, name='plucking_planner_save_data'),
    path('plucking_scheme/', views.Plucking_scheme, name='plucking_scheme'),
    path('plucking_rounds/', views.PluckingRounds, name='plucking_rounds'),
    path('programmed_scheme_plucking/', views.ProgrammedSchemePlucking, name='programmed_scheme_plucking'),

]
