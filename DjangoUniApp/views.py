from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import * 
from .form import PostulanteForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request,f'Usuario {username} creado')
    else:
        form = UserRegisterForm()
    
    context ={'form': form}
    return render(request,'registrar.html',context)

def logoutUser(request):
    logout(request)
    return render(request,'login.html') 

def loginpostulante(request):
    return render(request,'login-postulante.html')

@login_required
def homepage(request):
    return render(request,'index.html')

@login_required
def entrevistador(request):
    return render(request,'index-entrevistador.html')

@login_required
def postulante(request):
    return render(request,'index-postulante.html')

@login_required
def listapostulante(request):
    postulantes= Postulante.objects.all()
    total_postulantes = postulantes.count()
    context ={'postulantes':postulantes, 'total_postulantes':total_postulantes}
    return render(request,'Lista_Postulantes.html',context)

@login_required
def login(request):
    return render(request,'login.html')

@login_required
def miperfil(request):
    return render(request,'mi_perfil_entrevistador.html')

@login_required
def miperfilpostulante(request):
    return render(request,'mi_perfil_postulante.html')

@login_required
def chequearcv(request):
    return render(request,'chequear_cv.html')

@login_required
def crearentrevista(request):
    return render(request,'crear_entrevista.html')

@login_required
def documentopostulantes(request):
    return render(request,'documentos_postulante.html')

@login_required
def entrevistas(request):
    return render(request,'entrevistas_entrevistador.html')

@login_required
def listaentrevistas(request):
    return render(request,'lista_entrevistas_postulante.html')

@login_required
def registrarpostulante(request):
    if request.method == "POST":
        form = PostulanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listapostulante')

    else:
        form= PostulanteForm()

    context ={'form': form}
    return render(request,'registrar_postulante.html',context)

@login_required
def eliminarpostulante(request,codPostulante):
    postulante = Postulante.objects.get(codPostulante=codPostulante)
    postulante.delete()
    return redirect('listapostulante')


@login_required
def seleccionpostulante(request):
    return render(request,'seleccion_postulante.html')

@login_required
def calificarpostulante(request):
    return render (request,'calificar.html')

@login_required
def entrevistapostulante(request):
    return render(request,'entrevista-postulante.html')

@login_required
def misdocumentos(request):
    return render(request,'misdocumentos.html')