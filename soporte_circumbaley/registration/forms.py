from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile, Department


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 Caracteres como maximo para ser valido")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    department_profile = forms.ModelChoiceField(
        queryset=Department.objects.all())  # , to_field_name='department_profile')
    # widgets = forms.Select(attrs={''})

    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link', 'department_profile']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control-file mt-3'}),
            'bio': forms.Textarea(attrs={'class': 'form-control-file mt-3', 'rows': 3, 'placeholder': 'Biografia'}),
            'link': forms.TextInput(attrs={'class': 'form-control-file mt-3', 'placeholder': 'Enlace'}),
            # guarda pero falta la clase que no se puede eliminar si esta con un usuario
            'department_profile': forms.Select(attrs={'class': ''}),
        }

        # class authorForm(forms.ModelForm):

        class departmentForm(forms.ModelForm):
            class Meta:
                model = Department
                fields = ['name']


class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 Caracteres como maximo para ser valido")

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("El Email Ya Se Encuentra En Nuestra Base De Datos, Prueba Con otro")
        return email
