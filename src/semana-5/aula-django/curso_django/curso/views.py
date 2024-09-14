from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Aluno
# Create your views here.

def acesso_curso(request):
    aluno = 'Gabriel Lumertz'
    professor = 'Leonarod Marco'
    nome_curso = 'Curso Python'

    retorno = (f'Nome do curso: {nome_curso}, Professor: {professor}, Aluno: {aluno}')
    
    return HttpResponse(retorno)

def acesso_curso_template(request):
    return render(request, 'acesso.html')

def acesso_curso_template_contexto(request):
    alunos = Aluno.objects.all()

    contexto = {
        'alunos': alunos
    }

    return render(request, 'listagem_alunos.html', contexto)


def criar_aluno(request):
    nome = request.POST.get('nome')
    cargo = request.POST.get('cargo')
    aposentado = request.POST.get('aposentado')
    data_nascimento = request.POST.get('data_nascimento')

    aluno = Aluno(
        nome=nome,
        cargo=cargo,
        aposentado=True if aposentado else False,
        data_de_nascimento=data_nascimento
    )

    aluno.save()

    return redirect('listagem_alunos')

def excluir_aluno(request, id):
    aluno = Aluno.objects.get(id=id)
    aluno.delete()

    return redirect('listagem_alunos')