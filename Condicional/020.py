"""
Faça um Programa para leitura de três notas parciais de um aluno. 
O programa deve calcular a média alcançada por aluno e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.
"""

pri_nota = float(input("Insira o valor da primeira nota do aluno: "))
seg_nota = float(input("Insira o valor da segunda nota do aluno: "))
ter_nota = float(input("Insira o valor da terceira nota do aluno: "))
media = (pri_nota + seg_nota + ter_nota) / 3

status = "aprovado"
if media == 10:
    status = "aprovado com distinção"
elif media < 7:
    status = "reprovado"

print("O aluno foi {}!".format(status))
