# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

fahr = float(input("Insira um temperatura em graus fahrenheit: "))
celsius = 5 * ((fahr - 32) / 9)

print("\nO resultado da conversão é {:.2f}°".format(celsius))
