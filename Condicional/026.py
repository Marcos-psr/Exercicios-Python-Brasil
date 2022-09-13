"""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
(codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago
pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""

print("""Bem vindo ao posto!

TABELA DE PREÇOS
Litro do Álcool: R$ 1,90 
Litro da Gasolina: R$ 2,50 """)

combustivel = input("Insira o combustível desejado (A para álcool e G para gasolina): ")
litros = int(input("Insira quantos litros deseja: "))

if combustivel.upper() == "A":
    if litros <= 20:
        desconto = 0.03
    else:
        desconto = 0.05
    preco = (litros * 1.9) * (1 - desconto)
elif combustivel.upper() == "G":
    if litros <= 20:
        desconto = 0.04
    else:
        desconto = 0.06
    preco = (litros * 2.5) * (1 - desconto)
else:
    raise ValueError("Combustível inserido é inválido.")

print("\nValor total: R$ {:.2f}".format(preco))
