from django import forms
from .models import Devices


class DevicesForm(forms.ModelForm):
    is_new = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'onoffswitch', 'id': 'myonoffswitch'})),

    class Meta:
        model = Devices
        fields = ['name', 'description', 'order', 'is_new']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}),
            # : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}),

        }
        labels = {
            'name': '',
        }
