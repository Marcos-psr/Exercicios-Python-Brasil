# Faça um Programa que peça dois números e imprima o maior deles.

print("--MAIOR NÚMERO--\n")
primeiro = float(input("Informe o primeiro número: "))
segundo = float(input("Informe o segundo número: "))

if primeiro > segundo:
    print("\nO maior número é o {}".format(primeiro))
elif primeiro < segundo:
    print("\nO maior número é o {}".format(segundo))
else:
    print("\nOs dois números são iguais.")
