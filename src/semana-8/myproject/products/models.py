from django.db import models

# Create your models here.


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

    class Meta:
        permissions = [
            ("pode_adicionar_produto", "Pode adicionar produto"),
            ("pode_editar_produto", "Pode editar produto"),
            ("pode_deletar_produto", "Pode deletar produto"),
            ("pode_ver_produto", "Pode ver produto"),
        ]
