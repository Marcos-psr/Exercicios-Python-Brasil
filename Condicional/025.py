"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""

contador_sim = 0

pergunta1 = input("Telefonou para a vítima? -> ").lower()
if pergunta1 == "s" or pergunta1 == "sim":
    contador_sim += 1

pergunta2 = input("Esteve no local do crime? -> ").lower()
if pergunta2 == "s" or pergunta2 == "sim":
    contador_sim += 1

pergunta3 = input("Mora perto da vítima? -> ").lower()
if pergunta3 == "s" or pergunta3 ==  "sim":
    contador_sim += 1

pergunta4 = input("Devia para a vítima? -> ").lower()
if pergunta4 == "s" or pergunta4 == "sim":
    contador_sim += 1

pergunta5 = input("Já trabalhou com a vítima? -> ").lower()
if pergunta5 == "s" or pergunta5 == "sim":
    contador_sim += 1

if contador_sim == 2:
    print("\nA pessoa é suspeita.")
elif contador_sim == 3 or contador_sim == 4:
    print("\nA pessoa é cumplíce.")
elif contador_sim == 5:
    print("\nA pessoa é o assassino.")
else:
    print("\nA pessoa é inocente.")
