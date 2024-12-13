"""
URL configuration for eloCARS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Aplicaciones.Mecanico import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.pagina_principal, name='pagina_principal'),  # Página inicial.
    path('listadoModelos/', include('Aplicaciones.Mecanico.urls')),
    path('listadoCiudades/', views.listadoCiudades, name='listadoCiudades'),
    path('listadoVehiculos/', views.listadoVehiculos, name='listadoVehiculos'),
    path('listadoPropietarios/', views.listadoPropietarios, name='listadoPropietarios'),
    path('agregarModelo/', views.agregarModelo, name='agregarModelo'),
    path('agregarCiudad/', views.agregarCiudad, name='agregarCiudad'),
    path('agregarVehiculo/', views.agregarVehiculo, name='agregarVehiculo'),
    path('agregarPropietario/', views.agregarPropietario, name='agregarPropietario'),
    path('editarModelo/<int:pk>/', views.editarModelo, name='editarModelo'),
    path('editarCiudad/<int:pk>/', views.editarCiudad, name='editarCiudad'),
    path('eliminarModelo/<int:pk>/', views.eliminarModelo, name='eliminarModelo'),
    path('eliminarCiudad/<int:pk>/', views.eliminarCiudad, name='eliminarCiudad'),
    path('eliminarVehiculo/<int:pk>/', views.eliminarVehiculo, name='eliminarVehiculo'),
    path('eliminarPropietario/<int:pk>/', views.eliminarPropietario, name='eliminarPropietario'),
    path('editarVehiculo/<int:pk>/', views.editarVehiculo, name='editarVehiculo'),
    path('editarPropietario/<int:pk>/', views.editarPropietario, name='editarPropietario'),
]