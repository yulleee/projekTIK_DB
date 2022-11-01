from dataclasses import fields
from django.forms import ModelForm
from django import forms
from dosen.models import Dosen

class FormDosen(ModelForm):
    class Meta: 
        model = Dosen
        fields = '__all__'

        widgets = {
            'nip' : forms.TextInput({'class':'form-control'}),
            'nama' : forms.TextInput({'class':'form-control'}),
            'jabatan' : forms.TextInput({'class':'form-control'}),
            'email' : forms.TextInput({'class':'form-control'}),
            'foto' : forms.FileInput({'class':'form-control'}),
        }