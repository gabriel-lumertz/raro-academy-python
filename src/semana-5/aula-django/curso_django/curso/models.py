from django.db import models
from datetime import datetime

# Create your models here.


class Turma(models.Model):
    nome = models.CharField(max_length=50)
    ativa = models.BooleanField(default=False)
    inicio_aulas = models.DateField()
    fim_aulas = models.DateField()
    professores = models.ManyToManyField('Professor', related_name='turmas')
    alunos = models.ManyToManyField('Aluno', related_name='turmas')

    def __str__(self):
        return f'{self.nome}'


class Professor(models.Model):
    nome = models.CharField(max_length=50)
    ativo = models.BooleanField(default=False)
    data_nascimento = models.DateField()
    data_contratacao = models.DateField()

    def __str__(self):
        return f'{self.nome}'


class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    data_nascimento = models.DateField(blank=True, null=True)
    data_matricula = models.DateField(blank=True, null=True)
    mentor = models.OneToOneField(
        'Mentor',
        related_name='aluno',
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return f'#{self.id} | {self.nome}'

    def calcular_idade(self):
        # try:
        hoje = datetime.now().date()
        idade = hoje.year() - self.data_nascimento.year()
        # except:
        #     pass
        return idade

    def calcular_notas(self):
        atividades_aluno = self.atividades_aluno.filter(
            nota__isnull=False
        )

        if not atividades_aluno.exists():
            return 'Nenhuma atividade entregue.'

        # total_notas = sum(atividade.nota for atividade in atividades_aluno)


class Mentor(models.Model):
    nome = models.CharField(max_length=50)
    ativo = models.BooleanField(default=False)


class Atividade(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField()
    data_criacao = models.DateField(auto_now_add=True)
    data_entrega = models.DateField()


class AtividadeAluno(models.Model):
    aluno = models.ForeignKey(
        'Aluno',
        related_name='atividades_aluno',
        on_delete=models.CASCADE
    )
    atividade = models.ForeignKey(
        'Atividade',
        related_name='atividades_alunos',
        on_delete=models.CASCADE
    )
    data_entrega = models.DateField(
        null=True,
        blank=True
    )
    nota = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )
