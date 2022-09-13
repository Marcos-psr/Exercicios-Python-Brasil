# Faça um Programa que leia três números e mostre o maior deles.

print("--MAIOR NÚMERO--\n")
primeiro = float(input("Informe o primeiro número: "))
segundo = float(input("Informe o segundo número: "))
terceiro = float(input("Informe o terceiro número: "))

maior = primeiro
if segundo > maior:
    maior = segundo
if terceiro > maior:
    maior = terceiro

print("O maior número é o {}".format(maior))
