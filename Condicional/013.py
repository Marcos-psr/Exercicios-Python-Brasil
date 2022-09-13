# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
# se digitar outro valor deve aparecer valor inválido.

numero_semana = int(input("""Insira um número que representa um dia da semana:
1- Domingo, 2- Segunda, 3- Terça, 4- Quarta, 5- Quinta, 6- Sexta, 7- Sábado

-> """))

if numero_semana == 1:
    dia = "Domingo"
elif numero_semana == 2:
    dia = "Segunda"
elif numero_semana == 3:
    dia = "Terça"
elif numero_semana == 4:
    dia = "Quarta"
elif numero_semana == 5:
    dia = "Quinta"
elif numero_semana == 6:
    dia = "Sexta"
elif numero_semana == 7:
    dia = "Sábado"
else:
    dia = "Dia inválido"

print("\n{} - {}".format(numero_semana, dia))
