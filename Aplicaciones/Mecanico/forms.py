from django import forms
from .models import modelos, ciudades, vehiculos, propietarios

# Formulario para agregar un nuevo modelo
class ModeloForm(forms.ModelForm):
    class Meta:
        model = modelos
        fields = ['nombre_mod', 'color_mod']

# Formulario para agregar una nueva ciudad
class CiudadForm(forms.ModelForm):
    class Meta:
        model = ciudades
        fields = ['nombre_ciu']

# Formulario para agregar un nuevo vehículo
class VehiculoForm(forms.ModelForm):
    class Meta:
        model = vehiculos
        fields = ['fabricacion_vehi', 'precio_vehi', 'placa_vehi', 'fk_id_mod']

# Formulario para agregar un nuevo propietario
class PropietarioForm(forms.ModelForm):
    class Meta:
        model = propietarios
        fields = ['nombre_pro', 'apellido_pro', 'email_pro', 'telefono_pro', 'fk_id_ciu', 'fk_id_vehi']