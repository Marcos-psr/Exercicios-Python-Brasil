"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
"""

numint1 = int(input("Insira o primeiro número inteiro: "))
numint2 = int(input("Insira o segundo número inteiro: "))
numreal = float(input("Insira um número real: "))

solucao1 = numint1 * 2 + numint2 / 2
solucao2 = numint1 * 3 + numreal
solucao3 = numreal ** 3

print('''\nPrimeira Solução: {}
Segunda Solução: {}
Terceira Solução: {}'''.format(solucao1, solucao2, solucao3))
