# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

dias_por_mes = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

data = input("Insira uma data no formato dd/mm/aaaa: ")

if len(data) != 10:
    print("Data no formato inválido.")
else:    
    dia = int(data[0:2])
    mes = int(data[3:5])
    ano = int(data[6:])
    
    if dia > 31 or dia < 0:
        print("Dia inválido.")
    elif mes > 12 or mes < 0:
        print("Mês inválido.")
    elif dia > dias_por_mes[mes - 1]:
        print("O mês tem menos de {} dias.".format(mes, dia))
    else:
        print("A data {} é valida.".format(data))
        