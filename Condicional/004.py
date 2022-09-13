# Faça um Programa que verifique se uma caracter digitada é vogal ou consoante.

from string import ascii_lowercase # Importando 
import unidecode  # Biblioteca usada para retirar acentuação.

caracteres_validos = ascii_lowercase

print("--VOGAL OU CONSOANTE--\n") 
caracter = input("Insira uma letra: ")
caracter_modificado = unidecode.unidecode(caracter.lower())

if caracter_modificado not in caracteres_validos or len(caracter) > 1:
    print("O carácter '{}' é inválido.".format(caracter))
elif caracter_modificado in "aeiou":
    print("A caracter '{}' é uma vogal.".format(caracter))
else:
    print("A caracter '{}' é uma consoante.".format(caracter))
