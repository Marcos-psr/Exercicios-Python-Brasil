# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celsius = float(input("Insira um valor em graus celsius: "))
fahr = ((celsius / 5) * 9) + 32

print("\nA temperatura convertida é de {}°".format(fahr))
