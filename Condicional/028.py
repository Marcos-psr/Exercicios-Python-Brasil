"""
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá
ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada
pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total,
tipo de pagamento, valor do desconto e valor a pagar.
"""

print("----HIPERMERCADO TABAJARA----\n")
print("""Confira nossas promoções!
Código   |   Produtos    |   Até 5 Kg         |     Acima de 5 Kg
  1      |   File Duplo      R$ 4,90 por Kg         R$ 5,80 por Kg
  2      |   Alcatra         R$ 5,90 por Kg         R$ 6,80 por Kg
  3      |   Picanha         R$ 6,90 por Kg         R$ 7,80 por Kg""")

codigo = int(input("\nInsira o código do produto desejado: "))
qtd_de_carne = float(input("Insira a quantidade de carne (em Kg) a ser comprada: "))


if qtd_de_carne <= 5:
    if codigo == 1:
        preco_carne = 4.9
        tipo = "File Duplo"
    elif codigo == 2:
        preco_carne = 5.9
        tipo = "Alcatra"
    elif codigo == 3:
        preco_carne = 6.9
        tipo = "Picanha"
    else:
        raise ValueError("O Código inserido é inválido")
else:
    if codigo == 1:
        preco_carne = 5.8
        tipo = "File Duplo"
    elif codigo == 2:
        preco_carne = 6.8
        tipo = "Alcatra"
    elif codigo == 3:
        preco_carne = 7.8
        tipo = "Picanha"
    else:
        raise ValueError("O Código inserido é inválido")

cartao = input("Deseja realizar a compra utilizando o cartão Tabajara e receber 5% de desconto?\n(s/n) -> ")

preco_total = qtd_de_carne * preco_carne
if cartao.lower() == "s" or cartao.lower() == "sim":
    desconto = preco_total * 0.05
    preco_total *= 0.95
    forma_de_pagamento = "Cartão Tabajara"
else:
    desconto = 0
    forma_de_pagamento = input("Insira a forma de pagamento: ")

print("""\n\n-------------CUPOM FISCAL-------------
Tipo de Carne: {}
Quantidade de carne {} Kg
Forma de pagamento: {}
Desconto Total: R$ {}

Total a pagar: R$ {}""".format(tipo, qtd_de_carne, forma_de_pagamento, desconto, preco_total))
