# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

salario_hora = float(input("Insira o valor da hora trabalhada: "))
horas_trabalhadas = int(input("Insira o total de horas trabalhadas no mês: "))
total_salario = horas_trabalhadas * salario_hora

print("\nO salário total é de R$ {:.2f}!".format(total_salario))
