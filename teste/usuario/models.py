from django.db import models

# Create your models here.

class Usuarios(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    senha = models.CharField(max_length=50)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
