# from django.shortcuts import render
# from .models import Categoria_producto, Producto

# # Create your views here.

# def shop(request):
    
#     producto=Producto.objects.all()
    
#     return render(request, "tienda/template/tienda/tienda.html", {'producto': producto})

# def categoria(request, categoria_id):
    
#     categoria=Categoria_producto.objects.get(id=categoria_id)
    
#     producto=Producto.objects.filter(categorias=categoria)
    
#     return render(request, "tienda/template/tienda/tienda.html", {'categoria':categoria, 'producto': producto})
    
    
