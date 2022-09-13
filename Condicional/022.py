# Faça um Programa que peça um número inteiro e determine se ele é par ou impar. 
# Dica: utilize o operador módulo (resto da divisão).

inteiro = int(input("Insira um número inteiro: "))


if inteiro % 2 == 0:
    tipo = "par"
else:
    tipo = "ímpar"
    
print("O número é {}.".format(tipo))