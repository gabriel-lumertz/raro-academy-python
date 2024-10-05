from django.urls import path
from .views import (
    listar_produtos,
    adicionar_produto,
    editar_produto,
    deletar_produto
)


urlpatterns = [
    path('', listar_produtos, name='listar_produtos'),
    path('adicionar/', adicionar_produto, name='adicionar_produto'),
    path('editar/<int:id>/', editar_produto, name='editar_produto'),
    path('deletar/<int:id>/', deletar_produto, name='deletar_produto'),
]
