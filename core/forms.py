from django import forms
from .models import SugestoesModel

class SugestoesModelForm(forms.ModelForm):
    class Meta:
        model = SugestoesModel
        fields = ('nome', 'email', 'mensagem')
