import random

lista_diciplinas = ["Português", "Matemática", "Física", "Química", "Geografia", "História", "Biologia"]
notas_das_diciplinas = {}

def media_notas (lista_notas):
    lista_notas.sort()
    lista_notas.pop(0)
    mediaNotas = sum(lista_notas) / len(lista_notas)
    return mediaNotas
    
def gerar_notas_aleatorias():
    notas_aleatorias = random.sample(range(0, 100), 5)
    return notas_aleatorias
    

def atribuir_nota_materia(lista_diciplinas):
    for diciplina in lista_diciplinas:
        notas_provas = gerar_notas_aleatorias()
        mediaNotas = media_notas(notas_provas)
        notas_das_diciplinas.update({diciplina : mediaNotas})

def avaliar_diciplinas(notas_das_diciplinas):
    for diciplina, nota in notas_das_diciplinas.items():
        if(nota < 60):
            print(f"Diciplina {diciplina}, nota {nota} - Resultado: Reprovado.")
        else:
            print(f"Diciplina {diciplina}, nota {nota} - Resultado: Aprovado.")

notas_diciplinas = atribuir_nota_materia(lista_diciplinas)

resultado_final = avaliar_diciplinas(notas_das_diciplinas)

print(resultado_final)