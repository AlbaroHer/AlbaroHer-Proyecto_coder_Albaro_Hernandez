from django.shortcuts import render
from servicios.models import Servicio
from django.http import HttpResponse

# Create your views here.


def service(request):
    
    servicios=Servicio.objects.all()
    
    return render(request, "servicios/templates/servicios/servicios.html",{'servicios':servicios})