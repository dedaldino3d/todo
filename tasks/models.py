from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.

class Task(models.Model):
    STATUS = (
        ('doing', 'Doing'),
        ('done', 'Done'),
    )

    title = models.CharField(verbose_name='Titulo', max_length=250)
    description = models.TextField(verbose_name='Descrição')
    done = models.CharField(
        max_length=5, choices=STATUS)

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    created_at = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Actualizado em', auto_now=True)

    def __str__(self):
        return self.title
