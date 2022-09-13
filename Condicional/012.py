"""Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário
Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os
descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10% Salário Bruto acima de 2500 - desconto de 20%"""

valor_hora = float(input("Insira o valor em reais da hora trabalhada: "))
horas_totais = int(input("Insira o valor de horas trabalhadas: "))

salario_bruto = valor_hora * horas_totais
ir = 20
if salario_bruto <= 900:
    ir = 0
elif salario_bruto <= 1500:
    ir = 5
elif salario_bruto <= 2500:
    ir = 10

desconto_ir = salario_bruto * (ir / 100)
inss = salario_bruto * 0.1
fgts = salario_bruto * 0.11
salario_liquido = salario_bruto - desconto_ir - inss

print(f"""\nSalário Bruto: ({valor_hora} * {horas_totais})         : R$ {salario_bruto:.2f}
(-) IR ({ir}%)                        : R$  {desconto_ir:.2f} 
(-) INSS (10%)                     : R$  {inss:.2f}
FGTS (11%)                         : R$  {fgts:.2f}
Total de descontos                 : R$  {inss + desconto_ir:.2f}
Salário Liquido                    : R$  {salario_liquido:.2f}""")
