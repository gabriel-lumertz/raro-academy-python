import math
import platform
import os

def clear():
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear()

vertice_x0 = float(input('Digite o vértice de x0: '))
vertice_y0 = float(input('Digite o vértice de y0: '))

vertice_x1 = float(input('Digite o vértice de x1: '))
vertice_y1 = float(input('Digite o vértice de y1: '))

vertice_x2 = float(input('Digite o vértice de x2: '))
vertice_y2 = float(input('Digite o vértice de y2: '))

clear()

lado_a = math.sqrt((vertice_x1 - vertice_x0) ** 2 + (vertice_y1 - vertice_y0) ** 2)
lado_b = math.sqrt((vertice_x2 - vertice_x1) ** 2 + (vertice_y2 - vertice_y1) ** 2)
lado_c = math.sqrt((vertice_x2 - vertice_x0) ** 2 + (vertice_y2 - vertice_y0) ** 2)

semi_perimetro = (lado_a + lado_b + lado_c) / 2

area = math.sqrt(
    semi_perimetro * 
    (semi_perimetro - lado_a) * 
    (semi_perimetro - lado_b) *
    (semi_perimetro - lado_c)
    )

print(
    'A triangle with vertices ({:.1f}, {:.1f}), ({:.1f}, {:.1f}) and ({:.1f}, {:.1f}) has an area of {:.1f}.'
    .format(
        vertice_x0,
        vertice_y0,
        vertice_x1,
        vertice_y1,
        vertice_x2,
        vertice_y2,
        area
    )
)