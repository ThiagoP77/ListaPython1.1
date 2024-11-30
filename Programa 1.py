"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: Tendo como dados de entrada a altura
de uma pessoa, construa um algoritmo que calcule seu peso
ideal, usando a seguinte fórmula: (72.7*altura) - 58
Data: 16/09/21
"""
# Entrada de dados
print("============================================")
print("CALCULADORA DE PESO IDEAL A PARTIR DA ALTURA")
print("============================================")
print(" ")
altura = float(input("Informe a sua altura (em metros): "))
print(" ")               

# Processamento de dados
peso_ideal = float((72.7*altura)-58)

# Saída de dados
print("====================")
print("Resultado do Cálculo")
print("====================")
print(" ")
print("O peso ideal para uma altura de %.2fm é cerca de %.2fKg." %(altura, peso_ideal))
