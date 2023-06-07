from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required


@permission_required('your_app.view_psp')
def psp_view(request):
    pass


def ResourcesAdmin(request):
    pass

    return HttpResponse('127.0.0.1:8000/AdminResources-admin/')


# Create your views here.
def Admin(request):
    pass
    return HttpResponse('http:/127.0.0.1:8000/admin/')
