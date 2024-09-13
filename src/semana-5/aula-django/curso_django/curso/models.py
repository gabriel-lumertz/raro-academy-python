from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    cargo = models.CharField(max_length=50)
    aposentado = models.BooleanField(default=False)
    data_de_nascimento = models.CharField(max_length=12)