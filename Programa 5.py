"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas
e o preço total.
Data: 18/09/21
"""

# Entrada de dados
print("=====================================================")
print("CALCULADORA: LATAS DE TINTA NECESSÁRIAS E PREÇO TOTAL")
print("=====================================================")
print(" ")
metros_pintados = float(input("Informe quantos metros quadrados devem ser pintados: "))
print(" ")

# Processamento de dados
litros_necessarios = (metros_pintados/3)
latas_compradas = int(litros_necessarios/18)

if(litros_necessarios%18 != 0):
    latas_compradas = (latas_compradas + 1)
    
preço_total = (latas_compradas*80)

# Saída de dados
print("=========")
print("Resultado")
print("=========")
print(" ")
print("São necessárias %d latas de tinta para pintar %.2fm²." %(latas_compradas, metros_pintados))
print("O preço total é de R$%.2f." %(preço_total))
