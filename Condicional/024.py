"""
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
"""

num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))
operacao = input("Insira a operação a ser realizada (+, -, *, /): ")

if operacao == "+":
    resultado = num1 + num2

elif operacao == "-":
    resultado = num1 - num2

elif operacao == "*":
    resultado = num1 * num2

else:
    if num2 == 0:
        num2 = 1
        print("\nImpossível dividir por 0, o segundo número será substituído por 1!\n")
    resultado = num1 / num2


if resultado % 2 == 0:
    impar_par = "par"
else:
    impar_par = "ímpar"

status = "Neutro (0)"
if resultado < 0:
    status = "Negativo"
elif resultado > 0:
    status = "Positivo"

if resultado == round(resultado):
    inteiro_decimal = "inteiro"
else:
    inteiro_decimal = "decimal"

print(f"\nO número {resultado} é um {impar_par}, {status} e {inteiro_decimal}.")
