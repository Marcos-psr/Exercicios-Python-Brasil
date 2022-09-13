"""Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito
for A, B ou C ou “REPROVADO” se o conceito for D ou E."""

nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
media = (nota1 + nota2)/2

if media >= 10:
    media = 10
elif media <= 0:
    media = 0

if 10 >= media >= 9:
    conceito = "A"
    status = "Aprovado"
elif 9 > media >= 7.5:
    conceito = "B"
    status = "Aprovado"
elif 7.5 > media >= 6:
    conceito = "C"
    status = "Aprovado"
elif 6 > media >= 4:
    conceito = "D"
    status = "Reprovado"
else:
    conceito = "E"
    status = "Reprovado"

print("""\nO aluno foi {}!
Média: {} - Conceito: {}
Primeira nota: {}
Segunda nota: {}
""".format(status, media, conceito, nota1, nota2))
