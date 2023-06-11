from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from . import models
from .models import Resources

# Register your models here.
admin.site.register(models.Resources)


class ResourcesAdminSite(admin.AdminSite):
    site_header = "PSP Resources admin"
    site_title = "PSP Resources admin Portal"
    index_title = "The PSP page"


resources_admin_site = ResourcesAdminSite(name='resources_admin')
resources_admin_site.register(Resources)


class ResourcesAdmin(ImportExportModelAdmin):
    pass


# Register your models with Resourcesexcell_admin_site


class ResourcesexcellAdminSite(admin.AdminSite):
    site_header = "PSP Resourcesexcell admin"
    site_title = "PSP Resourcesexcell admin Portal"
    index_title = "The PSP page"


resource_site = ResourcesexcellAdminSite(name='ResourcesexcellAdminSite')

resourcesexcell_admin_site = ResourcesexcellAdminSite(name='Resourcesexcell_admin')



