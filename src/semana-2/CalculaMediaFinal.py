class AvaliaMediaFinal:
    def __init__(self, notas, pesos, nota_substituta):
        self.notas = notas
        self.pesos = pesos
        self.nota_substituta = nota_substituta

    '''Método privado que calcula a média ponderada.'''
    def __calcular_media(self, notas, pesos):
        return sum(x * y for x, y in zip(notas, pesos))

    '''Método privado que inicializa os cenários calculando a média das notas sem substitução.'''
    def __avaliar_cenarios(self):
        cenarios_avaliacao = {"Cenário 1": self.__calcular_media(notas=self.notas, pesos=self.pesos)}
        
        for i in range(len(self.notas)):
            novas_notas = self.notas.copy()
            novas_notas[i] = self.nota_substituta
            media = self.__calcular_media(notas=novas_notas, pesos=self.pesos)
            cenarios_avaliacao[f"Cenário {i + 2}"] = media

        return cenarios_avaliacao

    '''Método público que imprime o resultado da avaliação.'''
    def resultado(self):
        cenarios_avaliacao = self.__avaliar_cenarios()
        melhor_cenario = max(cenarios_avaliacao, key=cenarios_avaliacao.get)
        melhor_nota = cenarios_avaliacao[melhor_cenario]

        if melhor_nota >= 60:
            print(f'Aluno aprovado com nota {melhor_nota}.')
        else:
            print(f'Aluno reprovado com nota {melhor_nota}.')