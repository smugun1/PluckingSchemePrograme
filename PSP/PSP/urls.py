from django.contrib import admin
from django.urls import path, include
from plucking.admin import resourcesexcell_admin_site
from plucking_resources.admin import resources_admin_site
from plucking_resources.models import Resources

urlpatterns = [
    path('admin/', admin.site.urls),
    path('resourcesexcell-admin/', resourcesexcell_admin_site.urls),
    path('resources-admin/', resources_admin_site.urls),
    path('', include('plucking.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('plucking_resources/', include('plucking_resources.urls')),

]
