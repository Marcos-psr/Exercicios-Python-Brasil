"""As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para
desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o
reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00: aumento de 10% salários
de R$ 1500,00 em diante : aumento de 5%
Após o aumento ser realizado, informe na tela: o salário antes do reajuste; o  percentual de aumento aplicado;
o valor do aumento; o novo salário, após o aumento."""

salario = abs(float(input("Insira o valor do salário em reais: ")))

reajuste = 5
if salario <= 280:
    reajuste = 20
elif 700 > salario > 280:
    reajuste = 15
elif 1500 > salario >= 700:
    reajuste = 10

acresimo = salario * (reajuste / 100)

print("""\nValor do salário antes do reajuste: R$ {}
Percentual de aumento: {} % ou R$ {}
Novo salário: R$ {}""".format(salario, reajuste, acresimo, salario + acresimo))
