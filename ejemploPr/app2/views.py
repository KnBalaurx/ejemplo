from django.shortcuts import render
from django.shortcuts import redirect
from app2.models import Usuario
from app2.forms import FormUsuario


def index(request):
    return render(request, 'index.html')

def Tabla(request):
    usuario = Usuario.objects.all()
    data = {'usuario':usuario}
    return render(request, 'tabla.html', data)

def agUsuarios(request):
    form = FormUsuario()
    if request.method == 'POST':
        form = FormUsuario(request.POST)
        if form.is_valid():
            form.save()
    data = {'form': form}
    return render(request, 'agUsuarios.html', data)

def actualizarUsu(request,id):
    usuario = Usuario.objects.get(id = id)
    form = FormUsuario(instance= usuario)
    if request.method == 'POST':
        form = FormUsuario(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
        return Tabla(request)
    data = {'form': form}
    return render(request, 'agUsuarios.html', data)

def borrarUsu(request, id):
    usuario = Usuario.objects.get(id = id)
    usuario.delete()
    return redirect('/princi')