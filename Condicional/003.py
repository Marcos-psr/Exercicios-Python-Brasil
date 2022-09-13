# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input('''Insira a primeira letra do seu sexo:
F - Feminino | M - Masculino
--> ''').upper()

if sexo == "F":
    validador = "F - Feminino"
elif sexo == "M":
    validador = "M - Masculino"
else:
    validador = "Sexo Inválido"

print("\n"+validador)
