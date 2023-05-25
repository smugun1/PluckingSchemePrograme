from os import path

from django.contrib import admin
from django.core.paginator import Paginator, Page
from import_export.admin import ImportExportModelAdmin

from .models import ProgrammedScheme, Resources, Resourcesexcell, RoundsMonitor

from django.contrib import admin


class ResourcesAdminSite(admin.AdminSite):
    site_header = "PSP Resources admin"
    site_title = "PSP Resources admin Portal"
    index_title = "The PSP page"


resources_admin_site = ResourcesAdminSite(name='resources_admin')

# Register your models with resources_admin_site
resources_admin_site.register(Resources)


class ResourcesAdminSite(admin.AdminSite):
    site_header = "PSP Resources admin"
    site_title = "PSP Resources admin Portal"
    index_title = "The PSP page"


resources_admin_site = ResourcesAdminSite(name='resources_admin')
resources_admin_site.register(Resources)
admin.site.register(Resources)
admin.site.register(Resourcesexcell)
admin.site.register(ProgrammedScheme)
admin.site.register(RoundsMonitor)


#
# @admin.register(Resources)
# class ResourcesAdmin(ImportExportModelAdmin):
#     pass

#
# if path == 'resources-admin/':
#     admin.site.register(Resources)
#     admin.site.register(Resourcesexcell)
#     admin.site.register(PluckingPlanner)
#     admin.site.register(ProgrammedScheme)
#     admin.site.register(Plucking)
#     admin.site.register(Fields)
