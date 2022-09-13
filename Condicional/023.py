#  Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de
# arredondamento.

numero = float(input("Insira um número: "))
if numero == round(numero):
    print("\nO número é inteiro!")
else:
    print("\nO número é decimal!")