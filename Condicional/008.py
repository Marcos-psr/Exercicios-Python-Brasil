"""Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a
decisão é sempre pelo mais barato."""

produto1 = float(input("Insira o valor do primeiro produto: "))
produto2 = float(input("Insira o valor do segundo produto: "))
produto3 = float(input("Insira o valor do terceiro produto: "))

menor = "primeiro"
valor = produto1
if produto2 < produto1:
    menor = "segundo"
    valor = produto2
if produto3 < produto1:
    menor = "terceiro"
    valor = produto3

print("\nVocê deve comprar o {} produto que custa R$ {}.".format(menor, valor))
