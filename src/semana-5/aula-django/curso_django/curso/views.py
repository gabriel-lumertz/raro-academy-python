from django.shortcuts import render
from django.http import HttpResponse
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
    contexto = {
        'nome': 'Gabriel',
        'cargo': 'Desenvolvedor',
        'data_de_nascimento': '10/11/1988',
        'aposentado': True,
        'empresas': [
            'Sanremo',
            'Gauchafarma',
            'Procfit',
            'Mais Economica'
        ],
        'cidades': [
            {'nome': 'Esteio', 'estado': 'RS'},
            {'nome': 'Porto Alegre', 'estado': 'RS'},
            {'nome': 'Santos', 'estado': 'SP'},
            {'nome': 'Canoas', 'estado': 'RS'}
        ]
    }

    return render(request, 'acesso_contexto.html', contexto)