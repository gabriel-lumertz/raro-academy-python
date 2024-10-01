from django.contrib import admin
from .models import Turma

# Register your models here.


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
        (
            'Informações da turma', {
                'fields': ('nome', 'ativa')
            }
        ),
        (
            'Datas', {
                'fields': (
                    'inicio_aulas',
                    'fim_aulas'
                )
            }
        ),
        (
            'Participantes', {
                'fields': (
                    'professores',
                    'alunos'
                )
            }
        )
    )
    filter_horizontal = (
        'professores',
        'alunos'
    )


admin.site.register(Turma, TurmaAdmin)
