from django.contrib import admin
from django.urls import path, include
from plucking.admin import resources_admin_site

urlpatterns = [
    path('admin/', admin.site.urls),
    path('resources-admin/', resources_admin_site.urls),
    path('', include('plucking.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),

]
