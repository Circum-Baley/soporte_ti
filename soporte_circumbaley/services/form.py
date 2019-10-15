from django import forms
from .models import Service


class ServicesForm(forms.ModelForm):
    expiration = forms.DateField(widget=forms.SelectDateWidget)
    payday = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Service
        fields = ['name', 'description', 'number', 'file', 'payday', 'expiration']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre Servicio'}),
            'description': forms.Textarea(attrs={'class': 'form-control mt-1', 'placeholder': 'Descripcion'}),
            'number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numero De Servicio'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control-file mt-3'}),
            'payday': forms.DateInput(attrs={'class': 'md-form'}),
            'expiration': forms.DateInput(attrs={'class': 'md-form'}),
        }
        labels = {
            'name': '',
            'description': 'Descripcion De Servicios',
            'number': '',
            'payday': 'Fecha De Pago',
        }
