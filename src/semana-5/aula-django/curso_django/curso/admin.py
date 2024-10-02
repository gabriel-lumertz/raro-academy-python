from django.contrib import admin
from .models import Turma, AtividadeAluno, Aluno, Professor

# Register your models here.


def marcar_como_inativa(modeladmin, request, queryset):
    queryset.update(ativa=False)
    modeladmin.message_user(request, 'Turmas marcadas como inativas.')


class TurmaAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'ativa',
        'fim_aulas'
    )
    search_fields = (
        'nome',
    )
    list_filter = ('ativa',)
    fieldsets = (
        ('Informações da turma', {
                'fields': ('nome', 'ativa')
        }),
        ('Datas', {
            'fields': ('inicio_aulas', 'fim_aulas')
        }),
        ('Participantes', {
            'fields': ('professores', 'alunos')
        })
    )
    filter_horizontal = (
        'professores',
        'alunos'
    )
    readonly_fields = ('nome',)

    actions = [marcar_como_inativa]


class AtividadeAlunoInline(admin.StackedInline):
    model = AtividadeAluno
    fields = ('atividade', 'data_entrega', 'nota')
    readonly_fields = ('nota',)


class AtividadeAlunoTabularInline(admin.TabularInline):
    model = AtividadeAluno
    fields = ('atividade', 'data_entrega', 'nota')


class AlunoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Informações pessoais', {
            'fields': ('nome', 'data_nascimento', 'mentor')
        }),
        ('Informações extras', {
            'fields': ('data_matricula',)
        })
    )
    list_display = ('nome', 'data_nascimento', 'mentor')

    inlines = [AtividadeAlunoTabularInline]


class ProfessorAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Informações pessoais', {
            'fields': ('nome', 'data_nascimento')
        }),
        ('Informações extras', {
            'fields': ('data_contratacao', 'ativo')
        })
    )
    list_display = ('nome', 'data_nascimento', 'ativo')


admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Turma, TurmaAdmin)
