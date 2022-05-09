# from django.db import models

# # Create your models here.

# class Categoria_producto(models.Model):
    
#     nombre=models.CharField(max_length=50)
#     created=models.DateField(auto_now_add=True)
#     updated=models.DateField(auto_now_add=True)
    
#     class meta:
#         verbose_name="Categoria_producto"
#         verbose_name="Categorias_productos"
    
#     def __str__(self):
#         return self.nombre
    
# class Producto(models.Model):
#     nombre=models.CharField(max_length=50)
#     categorias=models.ForeignKey(Categoria_producto, on_delete=models.CASCADE)
#     imagen=models.ImageField(upload_to="tienda", null=True, blank=True)
#     precio=models.FloatField()
#     disponibilidad=models.BooleanField(default=True)
#     created=models.DateField(auto_now_add=True)
#     updated=models.DateField(auto_now_add=True)
    
#     class meta:
#         verbose_name="Producto"
#         verbose_name="Productos"
        
#     def __str__(self):
#         return self.nombre
        
    
    
    