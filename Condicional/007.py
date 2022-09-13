# Faça um Programa que leia três números e mostre o maior e o menor deles.

primeiro = float(input("Informe o primeiro número: "))
segundo = float(input("Informe o segundo número: "))
terceiro = float(input("Informe o terceiro número: "))

maior = primeiro
if segundo > maior:
    maior = segundo
if terceiro > maior:
    maior = terceiro

menor = primeiro
if segundo < menor:
    menor = segundo
if terceiro < menor:
    menor = terceiro

print("O maior número é {}\nO menor número é {}".format(maior, menor))
