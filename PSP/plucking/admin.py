from django.contrib import admin
from .models import PluckingRequirements, PluckingRounds, PluckingPlanner, ProgrammedSchemePlucking

# Register your models here.

admin.site.register(PluckingRequirements)
admin.site.register(PluckingRounds)
admin.site.register(PluckingPlanner)
admin.site.register(ProgrammedSchemePlucking)