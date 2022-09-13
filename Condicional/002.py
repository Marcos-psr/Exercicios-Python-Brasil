# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

print("--NEGATIVO OU POSITIVO--\n")
numero = float(input("Informe um valor: "))

status = "Neutro (0)"
if numero < 0:
    status = "Negativo"
elif numero > 0:
    status = "Positivo"

print("O número é {}.".format(status))
