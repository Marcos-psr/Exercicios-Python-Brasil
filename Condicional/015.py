"""Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um
triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;"""

a = float(input("Insira o valor do primeiro lado do triângulo: "))
b = float(input("Insira o valor do segundo lado do triângulo: "))
c = float(input("Insira o valor do terceiro lado do triângulo: "))

if a + b < c or a + c < b or c + b < a:
    print("Não é um triângulo")
elif a == b == c:
    print("Triângulo Equilátero")
elif a != b != c:
    print("Triângulo Escaleno")
else:
    print("Triângulo Isósceles")
