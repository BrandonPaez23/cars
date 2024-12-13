from django.db import models

# Create your models here.
class modelos(models.Model):
    id_mod = models.AutoField(primary_key=True) 
    nombre_mod = models.CharField(max_length=100)
    color_mod = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre_mod
    
class ciudades(models.Model):
    id_ciu = models.AutoField(primary_key=True) 
    nombre_ciu = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_ciu
    
class vehiculos(models.Model):
    id_vehi = models.AutoField(primary_key=True)  
    fabricacion_vehi = models.IntegerField()
    precio_vehi = models.DecimalField(max_digits=10, decimal_places=2)
    placa_vehi = models.CharField(max_length=100)
    fk_id_mod = models.ForeignKey(modelos, on_delete=models.RESTRICT)

    def __str__(self):
        return self.placa_vehi

class propietarios(models.Model):
    id_pro = models.AutoField(primary_key=True) 
    nombre_pro = models.CharField(max_length=100)
    apellido_pro = models.CharField(max_length=100)
    email_pro = models.EmailField(max_length=250)
    telefono_pro = models.CharField(max_length=100)
    fk_id_ciu = models.ForeignKey(ciudades, on_delete=models.RESTRICT)
    fk_id_vehi = models.ForeignKey(vehiculos, on_delete=models.RESTRICT)

    def __str__(self):
        return self.nombre_pro + " " + self.apellido_pro
