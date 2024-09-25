from django.views import View
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST
from django.contrib import messages
from .models import Turma, Professor
from curso.forms import CriarTurma
# Create your views here.


class CriarTurmaView(View):
    def get(self, request, *args, **kwargs):
        contexto = {
            'form': CriarTurma()
        }
        return render(request, 'criar_turma.html', contexto)

    def post(self, request, *args, **kwargs):
        form = CriarTurma(request.POST)

        if form.is_valid():
            nome = form.cleaned_data['nome']
            ativa = form.cleaned_data['ativa']
            inicio_aulas = form.cleaned_data['inicio_aulas']
            fim_aulas = form.cleaned_data['fim_aulas']

            Turma.objects.create(
                nome=nome,
                ativa=True if ativa else False,
                inicio_aulas=inicio_aulas,
                fim_aulas=fim_aulas
            )

            messages.success(request, 'A turma foi criada com sucesso.')

            return redirect('listar_turma')

        contexto = {
            'form': form
        }

        return render(request, 'criar_turma.html', contexto)


@require_POST
def criar_turma(request):
    form = CriarTurma(request.POST)

    if form.is_valid():
        nome = form.cleaned_data['nome']
        ativa = form.cleaned_data['ativa']
        inicio_aulas = form.cleaned_data['inicio_aulas']
        fim_aulas = form.cleaned_data['fim_aulas']

        Turma.objects.create(
            nome=nome,
            ativa=True if ativa else False,
            inicio_aulas=inicio_aulas,
            fim_aulas=fim_aulas
        )

        messages.success(request, 'A turma foi criada com sucesso.')

        return redirect('listar_turma')

    form = CriarTurma()

    return redirect('listar_turma')


@require_GET
def listar_turma(request):
    turmas = Turma.objects.all()

    contexto = {
        'turmas': turmas
    }

    return render(request, 'listar_turma.html', contexto)


@require_GET
def criar_turma_formulario(request):
    contexto = {
        'form': CriarTurma()
    }
    return render(request, 'criar_turma.html', contexto)


@require_POST
def criar_professor(request):
    nome = request.POST.get('nome')
    ativo = request.POST.get('ativo')
    data_nascimento = request.POST.get('data_nascimento')
    data_contratacao = request.POST.get('data_contratacao')
    turma = request.POST.get('turma')

    professor = Professor.objects.create(
        nome=nome,
        ativo=True if ativo else False,
        data_nascimento=data_nascimento,
        data_contratacao=data_contratacao
    )

    professor.turmas.add(turma)

    turma = Turma.objects.get(id=turma)

    turma.professores.add(professor)

    return redirect('listar_turma')


@require_GET
def criar_professor_formulario(request):
    turmas = Turma.objects.all()

    contexto = {
        'turmas': turmas
    }

    return render(request, 'criar_professor.html', contexto)
