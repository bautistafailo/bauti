from django.db import models

# Create your models here.

 

class Pago(models.Model):
    nombre=models.CharField(max_length=20)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()

    def __str__(self):
        return 'El curso es %s , la seccion es %s y el precio es %s' %(self.nombre, self.seccion, self.precio)

class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    email=models.EmailField(blank=True, null=True)
    telefono=models.CharField(max_length=20)

class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    pagado=models.BooleanField()
        

