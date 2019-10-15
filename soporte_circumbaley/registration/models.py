from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from messenger.models import Message
from departments.models import Department


# Create your models here.
def custom_upland_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=custom_upland_to, null=True, blank=True, verbose_name="Avatar")
    bio = models.TextField(null=True, blank=True, verbose_name="BioModel")
    link = models.URLField(max_length=200, null=True, blank=True, verbose_name="Enlace")
    department_profile = models.ForeignKey(Department, on_delete=models.PROTECT, null=True)

    class Meta:
        ordering = ['user__username']


@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Message.objects.get_or_create(user=instance)
#         print("Se Acaba De Crear Un Mensaje")
#
#
# @receiver(post_save, sender=User)
# def ensure_message_exists(sender, instance, **kwargs):
#     if kwargs.get('created', False):
#         Message.objects.get_or_create(user=instance)
#         print("Se Acaba De Crear Un Usuario Y Su Perfil Enlazado")
