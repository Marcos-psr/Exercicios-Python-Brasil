# Faça um Programa que leia três números e mostre-os em ordem decrescente.

primeiro = float(input("Insira o valor do primeiro número: "))
segundo = float(input("Insira o valor do segundo número: "))
terceiro = float(input("Insira o valor do terceiro número: "))

if segundo > primeiro:
    primeiro, segundo = segundo, primeiro
if terceiro > primeiro:
    primeiro, terceiro = terceiro, primeiro
if terceiro > segundo:
    terceiro, segundo = segundo, terceiro

print(f"\nOrdem decrescente: {primeiro} -> {segundo} -> {terceiro}")
