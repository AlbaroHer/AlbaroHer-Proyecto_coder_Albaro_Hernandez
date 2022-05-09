from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def home(request):
    
    return render(request,'project_app/template/project_app/inicio.html')



    

