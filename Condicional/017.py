# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não
# bissexto.

ano = int(input("Insira um ano (Exemplo: 2012): "))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("\nO ano {} é bissexto.".format(ano))
else:
    print("\nO ano {} não é bissexto.".format(ano))
