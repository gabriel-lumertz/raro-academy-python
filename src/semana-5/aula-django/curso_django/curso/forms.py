from django import forms


class CriarTurma(forms.Form):
    nome = forms.CharField(
        label='Nome',
        max_length='50',
        required=True
    )
    inicio_aulas = forms.DateField(
        label='Início das Aulas',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    fim_aulas = forms.DateField(
        label='Fim das Aulas',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    ativa = forms.BooleanField(
        label='Turma ativa',
        required=False
    )

    def clean_nome(self):
        black_list = [
            "Cyber Security",
            "QA",
            "PO",
        ]

        if self.cleaned_data['nome'] in black_list:
            raise forms.ValidationError('Proibido essa turma.')

        return self.cleaned_data['nome']
