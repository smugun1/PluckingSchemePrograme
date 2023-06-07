from os import path
from django.contrib import admin
from django.core.paginator import Paginator, Page
from .models import ProgrammedScheme, Resourcesexcell, RoundsMonitor, FieldsToPluck, DataEntry, AutoFields
from . import models

# Register your models with Resourcesexcell_admin_site


class ResourcesexcellAdminSite(admin.AdminSite):
    site_header = "PSP Resourcesexcell admin"
    site_title = "PSP Resourcesexcell admin Portal"
    index_title = "The PSP page"


resource_site = ResourcesexcellAdminSite(name='ResourcesexcellAdminSite')

resourcesexcell_admin_site = ResourcesexcellAdminSite(name='Resourcesexcell_admin')

admin.site.register(Resourcesexcell)
admin.site.register(ProgrammedScheme)
admin.site.register(RoundsMonitor)
admin.site.register(FieldsToPluck)
admin.site.register(AutoFields)

resourcesexcell_admin_site.register(models.Resourcesexcell)
resourcesexcell_admin_site.register(models.DataEntry)
