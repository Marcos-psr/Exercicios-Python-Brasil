"""
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas,
dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310, 305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""
numeros = [1000, 326, 300, 100, 320, 310, 305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7, 16]

for numero in numeros: 
    
    separador1 = ", "
    separador2 = " e "

    if numero >= 1000:
        print("Número inválido!")
    else: 
        centena = numero // 100
        dezena = (numero - centena * 100) // 10
        unidade = (numero - centena * 100 - dezena * 10) // 1

        if unidade == 0:
            unidade = ""
            separador2 = ""
        elif unidade == 1:
            unidade = f"{unidade} unidade"
        else:
            unidade = f"{unidade} unidades"

        if dezena == 0:
            dezena = ""
            separador1 = ""
            separador2 = ""
        elif dezena == 1:
            dezena = f"{dezena} dezena"
        else:
            dezena = f"{dezena} dezenas"
        
        if centena == 0:
            centena = ""
            separador1 = ""
        elif centena == 1:
            centena = f"{centena} centena"
        else:
            centada = f"{centena} centenas"
        
        if centena != "" and unidade != "":
            separador2 = " e "
        elif centena != "" and dezena != "":
            separador1 = " e "

        print(f"{numero} = {centena}{separador1}{dezena}{separador2}{unidade}")
