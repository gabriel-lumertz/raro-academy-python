from CalculaMediaFinal import AvaliaMediaFinal

'''
    Para usar a classe você deve:
    
    - Instanciar AvaliaMediaFinal passando os parâmetros notas, pesos e nota_substituta.
    - Chamar o método resultado.
'''

pesos = [0.4, 0.3, 0.3]

notas1 = [40, 40, 55]

nota_substituta = 75


notas2 = [80, 80, 55]

nota_substituta2 = 75


AvaliaMediaFinal(notas1, pesos, nota_substituta).resultado()

AvaliaMediaFinal(notas2, pesos, nota_substituta2).resultado()