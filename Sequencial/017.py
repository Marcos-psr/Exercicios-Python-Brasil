"""
Faça um Programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18
litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações
-comprar apenas latas de 18 litros;
-comprar apenas galões de 3,6 litros;
-misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os
valores para cima, isto é, considere latas cheias.
"""

import math

area = float(input("Insira uma área em metros quadrados: "))
litros = area / 6

galao = math.ceil(litros / 18)
preco_galao = galao * 80
latas = math.ceil(litros / 3.6)
preco_latas = latas * 25

mistura_galao = litros // 18
mistura_lata = math.ceil((litros - mistura_galao * 18) / 3.6)
if mistura_lata > 3:
    mistura_galao += 1
    mistura_lata = 0
    preco = mistura_galao * 80
else: 
    preco = mistura_galao * 80 + mistura_lata * 25

print('''Para a área de {:.2f} m² será necessário {:.2f} litros de tinta.\n
Será necessário {} galão(ões) de 18 litros: R$ {:.2f}
Será necessário {} lata(s) de 3,6 litros: R$ {:.2f}
Preço latas e galões misturados: {:.2f}'''.format(area, litros, galao, preco_galao, latas, preco_latas, preco))
