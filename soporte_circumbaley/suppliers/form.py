from django import forms
from .models import Supplier


class SuppliersForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['rut', 'name', 'description']  # , 'image']
        widgets = {
            'rut': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rut'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripcion'}),
            # 'image': forms.ImageField(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': '',
        }
