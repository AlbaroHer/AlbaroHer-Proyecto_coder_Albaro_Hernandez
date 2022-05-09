from django.shortcuts import render, redirect
from .forms import Formulario_contact
from django.core.mail import EmailMessage

# Create your views here.
    
    
def contact(request):
    
    formulario= Formulario_contact()
    
    if request.method=="POST":
        
        formulario= Formulario_contact(data=request.POST)
        
        if formulario.is_valid:
            nombre= request.POST.get("nombre")
            email= request.POST.get("email")
            contenido= request.POST.get("contenido")
            
            email_1=EmailMessage(subject="Mensaje de django",
                               body=f"El usuario {nombre} con direccion {email} envia lo siguien:\n\n {contenido}",
                               from_email="",to=['hernandezalbaro@hotmail.com'],reply_to=[email]
                               )
            
        
           
            try:
                email_1.send()
                
                return redirect("/contacto/?valido")
                
            except:
                
                return redirect("/contacto/?valido")
                 
    
    return render(request, "contacto/templates/contacto/contacto.html",{'mi_formulario':formulario})