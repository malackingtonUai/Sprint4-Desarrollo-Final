from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class Usuario(models.Model):
    username = models.CharField(max_length=15,primary_key=True)
    password = models.CharField(max_length=40)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField()


class Desafio(models.Model):
    codDesafio = models.CharField(max_length=5,primary_key=True)
    nombre= models.CharField(max_length=50)
    descripcion = models.CharField(max_length=70)
    resolusion = models.CharField(max_length=70)
    lenguajeProgramacion = models.CharField(max_length=30)

class Calificacion(models.Model):
    idCalificacion = models.CharField(max_length=5,primary_key=True)
    puntaje = models.PositiveSmallIntegerField(default=1)
    descripcion = models.CharField(max_length=30)
    RESULTADO_POSTULANTE=(
        ('a','Aceptado'),
        ('r','Rechazado')
    )
    resultado = models.CharField(max_length=1, choices=RESULTADO_POSTULANTE, blank=True, default='a', help_text='Resultado de la calificación')

class Documento(models.Model):
    codDocumento = models.CharField(max_length=5,primary_key=True)
    nombre = models.CharField(max_length=15)
    peso = models.CharField(max_length=5)
    documento = models.CharField(max_length=100)

class Postulante(models.Model):
    codPostulante = models.CharField(max_length=5,primary_key=True)
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    fecha_de_nacimiento = models.DateField()
    NIVEL_ESCOLARIDAD=[
        ('P','Profesional'),
        ('T','Técnico'),
        ('E','Estudiante Universitario'),
        ('M','Magister'),
        ('D','Doctorado')
    ]
    SEXO = [
        ('F','Femenino'),
        ('M','Masculino')
    ]
    nivelEscolar = models.CharField(max_length=1,choices=NIVEL_ESCOLARIDAD,default='E')
    genero= models.CharField(max_length=1,choices=SEXO,default='F')
    rut = models.CharField(max_length=15)


class PostulanteDesafio(models.Model):
    codPostulanteDesafio = models.CharField(max_length=5,primary_key=True)
    resolucionPostulante = models.CharField(max_length=70)
    tiemporespuesta = models.TimeField()
    estado = models.BooleanField(default=True)
    postulante = models.ForeignKey(Postulante, null=True, blank=True,on_delete=models.CASCADE)
    desafio = models.ForeignKey(Desafio, null=True, blank=True,on_delete=models.CASCADE)

class Entrevista(models.Model):
    codEntrevista = models.CharField(max_length=5,primary_key=True)
    nota = models.PositiveSmallIntegerField(default=1)
    tiempo = models.TimeField()
    postulantedesafio = models.ForeignKey(PostulanteDesafio, null=True, blank=True,on_delete=models.CASCADE)
    calificacion = models.ForeignKey(Calificacion, null=True, blank=True,on_delete=models.CASCADE)
    postulante = models.ForeignKey(Postulante, null=True,blank=True,on_delete=models.CASCADE)
    entrevistador = models.ForeignKey(Usuario, null=True,blank=True,on_delete=models.CASCADE)