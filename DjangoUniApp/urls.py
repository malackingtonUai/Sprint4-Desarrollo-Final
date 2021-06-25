from django.urls import path
from django.contrib.auth.views import  logout_then_login ,LoginView, LogoutView
from . import views

urlpatterns = [
    path('login/',LoginView.as_view(template_name='login.html'), name="login"),
    path('register/',views.register, name="register"),
    path('entrevistador/',views.entrevistador, name="indexentrevistador"),
    path('postulante/',views.postulante, name="indexpostulante"),
    path('listapostulante/', views.listapostulante, name="listapostulante"),
    path('login-postulante/', views.loginpostulante, name="loginpostulante"),
    path('miperfil/', views.miperfil, name="miperfil"),
    path('miperfilpostulante/', views.miperfilpostulante, name="miperfilpostulante"),
    path('chequearcv/',views.chequearcv, name="chequearcv"),
    path('crearentrevista/',views.crearentrevista, name="crearentrevista"),
    path('documentopostulantes/',views.documentopostulantes, name="documentopostulantes"),
    path('entrevistas/',views.entrevistas, name="entrevistas"),
    path('listaentrevistas/',views.listaentrevistas, name="listaentrevistas"),
    path('registrarpostulante/',views.registrarpostulante, name="registrarpostulante"),
    path('seleccionpostulante/',views.seleccionpostulante, name="seleccionpostulante"),
    path('calificar/',views.calificarpostulante, name="calificarpostulante"),
    path('entrevistapostulante/',views.entrevistapostulante, name="entrevistapostulante"),
    path('misdocumentos/',views.misdocumentos, name="misdocumentos"),
    path('logout/',logout_then_login,name='logout'),
    path('eliminar/<int:codPostulante>/',views.eliminarpostulante, name="eliminarpostulante"),  
    path('',views.homepage, name="index"),
]
