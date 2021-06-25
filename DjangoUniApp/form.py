from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Usuario
from .models import Postulante

class PostulanteForm(ModelForm):
    class Meta:
        model = Postulante
        fields = ['codPostulante','nombres','apellidos','email','fecha_de_nacimiento','nivelEscolar','genero','rut']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Contraseña2", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password1']
        help_texts = {k:"" for k in fields}

