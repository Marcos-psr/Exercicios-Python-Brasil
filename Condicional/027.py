"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto
de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças
adquiridas e escreva o valor a ser pago pelo cliente.
"""

qtd_morangos = float(input("Insira a quantidade (em KG) de morangos: "))
qtd_macas = float(input("Insira a quantidade (em KG) de maças: "))

if qtd_morangos <= 5:
    preco_morango = 2.5
else:
    preco_morango = 2.2

if qtd_macas <= 5:
    preco_maca = 1.8
else:
    preco_maca = 1.5


valor_total = (preco_morango * qtd_morangos) + (preco_maca * qtd_macas)
peso_frutas = qtd_morangos + qtd_macas
if valor_total > 25 or peso_frutas > 8:
    valor_total *= 0.9

print("""\nPeso total das compras: {:.2f} Kg
Valor total das compras: R$ {:.2f}""".format(peso_frutas, valor_total))
