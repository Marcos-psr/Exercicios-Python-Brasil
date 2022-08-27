"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em
Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""

tamanho_arquivo = float(input("Insira o tamanho de um arquivo para download em MB: "))
velocidade_link = float(input("Insira a velocidade de um link de internet em Mbps: "))
tempo_download = tamanho_arquivo / (velocidade_link / 8)
tempo_download_minutos = tempo_download / 60
print("Um arquivo de {} MB vai demorar cerca de {} segundos ou {} minutos.".format(tamanho_arquivo, tempo_download,
                                                                                   tempo_download_minutos))
