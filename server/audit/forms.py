from django import forms
from .models import Dict, Dict_type

class DictForm(forms.ModelForm):
    class Meta:
        model = Dict
        fields = ['code', 'name']

class DictTypeForm(forms.ModelForm):
    class Meta:
        model = Dict_type
        fields = ['name']
