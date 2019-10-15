from django import forms
from .models import Document


class DocumentsForm(forms.ModelForm):
    expiration = forms.DateField(widget=forms.SelectDateWidget)
    payday = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Document
        fields = ['types', 'number', 'payday', 'expiration']
        widgets = {
            'types': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tipos'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'payday': forms.DateInput(attrs={'class': 'md-form'}),
            'expiration': forms.DateInput(attrs={'class': 'md-form'}),
        }
        labels = {
            'name': '',
        }
