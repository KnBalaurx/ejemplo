from django import forms
from app2.models import Usuario

class FormUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'