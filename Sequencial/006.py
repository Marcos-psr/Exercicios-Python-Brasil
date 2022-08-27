# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

raio = float(input("Informe o valor do raio: "))
area = math.pi * raio**2

print("\nA área do círculo com raio {} é {:.2f}".format(raio, area))
