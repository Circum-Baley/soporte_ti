from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.db.models.signals import m2m_changed


# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="UsuarioMessage")
    content = RichTextField(verbose_name="Contenido")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha De Actualizacion")

    class Meta:
        ordering = ['created']


class ThreadManager(models.Manager):
    def find(self, user1, user2):
        queryset = self.filter(users=user1).filter(users=user2)
        if len(queryset) > 0:
            return queryset[0]
        return None

    def find_or_create(self, user1, user2):
        thread = self.find(user1, user2)
        if thread is None:
            thread = Thread.objects.create()
            thread.users.add(user1, user2)
        return thread


# Solucion Al no eliminar un usuario ya que solo se desactivara cuando quiera darlo de baja

class Thread(models.Model):
    users = models.ManyToManyField(User, related_name="threads")
    messages = models.ManyToManyField(Message)
    # Thread.objects.find(user1,user2)
    updated = models.DateTimeField(auto_now=True)
    objects = ThreadManager()

    class Meta:
        ordering = ['-updated']


def messages_chenged(sender, **kwargs):
    instance = kwargs.pop("instance", None)
    action = kwargs.pop("action", None)
    pk_set = kwargs.pop("pk_set", None)
    print(instance, action, pk_set)
    false_pk_set = set()
    if action is 'pre_add':
        for msg_pk in pk_set:
            msg = Message.objects.get(pk=msg_pk)
            if msg.user not in instance.users.all():
                print("Ups,({}) no forma parte del hilo".format(msg.user))
                false_pk_set.add(msg_pk)

    # Esto no funciono?? y lo de arriba no me quedo muy claro

    # busca mensajes de false_pk_set que no estan en pk_set y los borramos de pk_set
    pk_set.difference_update(false_pk_set)

    instance.save()


m2m_changed.connect(messages_chenged, sender=Thread.messages.through)
