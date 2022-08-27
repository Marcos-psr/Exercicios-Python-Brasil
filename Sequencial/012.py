# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal.
# Usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input("Insira uma altura em metros: "))
peso_ideal = 72.7 * altura - 58

print("O peso ideal para a altura {:.2f}m é {:.2f} kg.".format(altura, peso_ideal))
