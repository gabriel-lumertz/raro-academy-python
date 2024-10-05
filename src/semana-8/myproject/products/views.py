from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from django.contrib.auth.decorators import permission_required

# Create your views here.


@permission_required('products.pode_ver_produto', raise_exception=True)
def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(
        request,
        'products/listar_produtos.html',
        {'produtos': produtos}
    )


@permission_required('products.pode_adicionar_produto', raise_exception=True)
def adicionar_produto(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        preco = request.POST['preco']
        Produto.objects.create(nome=nome, preco=preco)
        return redirect('listar_produtos')
    return render(request, 'products/adicionar_produto.html')


@permission_required('products.pode_editar_produto', raise_exception=True)
def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        produto.nome = request.POST['nome']
        produto.preco = request.POST['preco']
        produto.save()
        return redirect('listar_produtos')
    return render(
        request,
        'products/editar_produto.html',
        {'produto': produto}
    )


@permission_required('products.pode_deletar_produto', raise_exception=True)
def deletar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('listar_produtos')
