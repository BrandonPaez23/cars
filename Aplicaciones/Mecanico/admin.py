from django.contrib import admin
from .models import modelos,ciudades,vehiculos,propietarios
# Register your models here.

admin.site.register(modelos)
admin.site.register(ciudades)
admin.site.register(vehiculos)
admin.site.register(propietarios)
