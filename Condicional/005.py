"""Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por
aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez."""

pri_nota = float(input("Insira o valor da primeira nota do aluno: "))
seg_nota = float(input("Insira o valor da segunda nota do aluno: "))
media = (pri_nota + seg_nota) / 2

status = "aprovado"
if media == 10:
    status = "aprovado com distinção"
elif media < 7:
    status = "reprovado"

print("O aluno foi {}!".format(status))
