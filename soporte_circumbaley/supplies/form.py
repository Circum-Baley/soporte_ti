from django import forms
from .models import Supply


class SuppliesForm(forms.ModelForm):
    class Meta:
        model = Supply
        fields = ['name', 'departments', 'suppliers', 'description', 'quantity', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'departments': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'suppliers': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}),
            'image': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Imagen'}),
        }
        labels = {
            'name': '',
        }
