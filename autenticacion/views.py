import imp
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


# Create your views here.

class Registro(View):
    
    def get(self, request):
        form=UserCreationForm()
        
        return render(request,"autenticacion/templates/registro/registro.html", {"form":form})
    
    
    def post(self, request):
        form=UserCreationForm(request.POST)
        
        if form.is_valid():
        
            usuario=form.save()
            
            login(request, usuario)
            
            return redirect('inicio')
        
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            
            return render(request,"autenticacion/templates/registro/registro.html", {"form":form})
        
        
    
def cerrar_sesion(request):
    logout(request)
    
    return redirect('inicio')


def loguear(request):
    
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_ususario=form.cleaned_data.get("username")
            contrasena_ususario=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_ususario, password=contrasena_ususario)
            if usuario is not None:
                login(request, usuario)
                return redirect('inicio')
            else:
                messages.error(request, "Usuario no valido")
        else:
            messages.error(request, "Informacion incorrecta")
            
            
    form=AuthenticationForm()
    
    return render(request,"autenticacion/templates/login/login.html", {"form":form})
    
    