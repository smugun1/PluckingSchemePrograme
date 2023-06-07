from django.contrib import admin
from .models import Resources
# Register your models here.
from import_export.admin import ImportExportModelAdmin
from . import models

admin.site.register(models.Resources)


class ResourcesAdminSite(admin.AdminSite):
    site_header = "PSP Resources admin"
    site_title = "PSP Resources admin Portal"
    index_title = "The PSP page"


resources_admin_site = ResourcesAdminSite(name='resources_admin')
resources_admin_site.register(Resources)


class ResourcesAdmin(ImportExportModelAdmin):
    pass
