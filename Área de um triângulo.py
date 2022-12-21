""" Faça um algoritmo que calcule a área de um triângulo, considerando a fórmula Area = BASE.ALTURA / 2.
    Utilize as variáveis AREA, BASE e ALTURA e os operadores aritméticos de multiplicação e divisão."""


def calc_area(base, height):
    # Calculando a área do triangulo
    area = (base * height) / 2
    return area


# Teste a função com base 10 e altura 5
base = 10
height = 5
result = calc_area(base, height)
print(result)

"""Isso imprimirá a área de um triângulo com base 10 e altura 5. O '/' operador é usado para realizar a divisão.

Você também pode definir as variáveis BASE e ALTURA ao invés de basee heightse preferir:"""


def calc_area(BASE, ALTURA):
    # Calculando a área do triangulo
    AREA = (BASE * ALTURA) / 2
    return AREA
