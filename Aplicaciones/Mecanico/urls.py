from django.urls import path
from . import views

urlpatterns = [
    path('listadoModelos/', views.listadoModelos, name='listadoModelos'),
    path('listadoCiudades/', views.listadoCiudades, name='listadoCiudades'),
    path('listadoVehiculos/', views.listadoVehiculos, name='listadoVehiculos'),
    path('listadoPropietarios/', views.listadoPropietarios, name='listadoPropietarios'),
    path('agregarModelo/', views.agregarModelo, name='agregarModelo'),
    path('agregarCiudad/', views.agregarCiudad, name='agregarCiudad'),
    path('agregarVehiculo/', views.agregarVehiculo, name='agregarVehiculo'),
    path('agregarPropietario/', views.agregarPropietario, name='agregarPropietario'),
    path('eliminarModelo/<int:pk>',views.eliminarModelo, name='eliminarModelo'),
    path('eliminarCiudad/<int:pk>',views.eliminarCiudad, name='eliminarCiudad'),
    path('eliminarVehiculo/<int:pk>',views.eliminarVehiculo, name='eliminarVehiculo'),
    path('eliminarPropietario/<int:pk>',views.eliminarPropietario, name='eliminarPropietario'),
    path('editarModelo/<int:pk>/', views.editarModelo, name='editarModelo'),
    path('editarCiudad/<int:pk>/', views.editarCiudad, name='editarCiudad'),
    path('editarVehiculo/<int:pk>/', views.editarVehiculo, name='editarVehiculo'),
    path('editarPropietario/<int:pk>/', views.editarPropietario, name='editarPropietario'),
]