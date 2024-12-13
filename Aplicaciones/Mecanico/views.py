from django.shortcuts import get_object_or_404, redirect, render
from .forms import ModeloForm, CiudadForm, VehiculoForm, PropietarioForm
from .models import modelos, ciudades, vehiculos, propietarios

def pagina_principal(request):
    return render(request, 'index.html')

def listadoModelos(request):
    modelosBdd= modelos.objects.all()
    return render(request,"listadoModelos.html", {'modelos':modelosBdd})

def listadoCiudades(request):
    ciudadesBdd= ciudades.objects.all()
    return render(request,"listadoCiudades.html", {'ciudades':ciudadesBdd})

def listadoVehiculos(request):
    vehiculosBdd= vehiculos.objects.all()
    return render(request,"listadoVehiculos.html", {'vehiculos':vehiculosBdd})

def listadoPropietarios(request):
    propietariosBdd= propietarios.objects.all()
    return render(request,"listadoPropietarios.html", {'propietarios':propietariosBdd})

def agregarModelo(request):
    if request.method == 'POST':
        form = ModeloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listadoModelos')
    else:
        form = ModeloForm()
    return render(request, 'agregarModelo.html', {'form': form})

# Vista para agregar una nueva ciudad
def agregarCiudad(request):
    if request.method == 'POST':
        form = CiudadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listadoCiudades')
    else:
        form = CiudadForm()
    return render(request, 'agregarCiudad.html', {'form': form})

# Vista para agregar un nuevo vehículo
def agregarVehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listadoVehiculos')
    else:
        form = VehiculoForm()
    return render(request, 'agregarVehiculo.html', {'form': form})

# Vista para agregar un nuevo propietario
def agregarPropietario(request):
    if request.method == 'POST':
        form = PropietarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listadoPropietarios')
    else:
        form = PropietarioForm()
    return render(request, 'agregarPropietario.html', {'form': form})

def eliminarModelo(request,pk):
    modelosEliminar=modelos.objects.get(pk=pk)
    modelosEliminar.delete()
    return redirect('listadoModelos')

def eliminarCiudad(request,pk):
    ciudadesEliminar=ciudades.objects.get(pk=pk)
    ciudadesEliminar.delete()
    return redirect('listadoCiudades')

def eliminarVehiculo(request,pk):
    vehiculosEliminar=vehiculos.objects.get(pk=pk)
    vehiculosEliminar.delete()
    return redirect('listadoVehiculos')

def eliminarPropietario(request,pk):
    propietariosEliminar=propietarios.objects.get(pk=pk)
    propietariosEliminar.delete()
    return redirect('listadoPropietarios')

def editarModelo(request, pk):
    modelo = get_object_or_404(modelos, pk=pk)
    
    if request.method == 'POST':
        form = ModeloForm(request.POST, instance=modelo)
        if form.is_valid():
            form.save()
            return redirect('listadoModelos')
    else:
        form = ModeloForm(instance=modelo)

    return render(request, 'editarModelo.html', {'form': form, 'modelo': modelo})

# Vista para editar una ciudad
def editarCiudad(request, pk):
    ciudad = get_object_or_404(ciudades, pk=pk)

    if request.method == 'POST':
        form = CiudadForm(request.POST, instance=ciudad)
        if form.is_valid():
            form.save()
            return redirect('listadoCiudades')
    else:
        form = CiudadForm(instance=ciudad)

    return render(request, 'editarCiudad.html', {'form': form, 'ciudad': ciudad})

# Vista para editar un vehículo
def editarVehiculo(request, pk):
    vehiculo = get_object_or_404(vehiculos, pk=pk)

    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            return redirect('listadoVehiculos')
    else:
        form = VehiculoForm(instance=vehiculo)

    return render(request, 'editarVehiculo.html', {'form': form, 'vehiculo': vehiculo})

# Vista para editar un propietario
def editarPropietario(request, pk):
    propietario = get_object_or_404(propietarios, pk=pk)

    if request.method == 'POST':
        form = PropietarioForm(request.POST, instance=propietario)
        if form.is_valid():
            form.save()
            return redirect('listadoPropietarios')
    else:
        form = PropietarioForm(instance=propietario)

    return render(request, 'editarPropietario.html', {'form': form, 'propietario': propietario})



