from django.views import View
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Turma, Professor
from curso.forms import CriarTurma, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class CriarTurmaView(LoginRequiredMixin, View):
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


@login_required
@require_GET
def listar_turma(request):
    print(f'Usuário que logou: # {request.user.id} {request.user.username}')
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


class LoginView(View):
    def get(self, request):
        contexto = {
            'form': LoginForm()
        }
        return render(request, 'login.html', contexto)

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            senha = form.cleaned_data['senha']

            user = authenticate(
                request,
                username=usuario,
                password=senha
            )

            if user is not None:
                login(request, user)
                return redirect('listar_turma')
            else:
                messages.error(request, 'Usuário ou senha inválidos')
                return render(request, 'login.html', {'form': form})

        return render(request, 'login.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)

        return redirect('login')
