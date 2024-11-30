"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: João Papo-de-Pescador, homem de bem, comprou um
microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido
pelo regulamento de pesca do estado de São Paulo (50 quilos)
deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável
peso (peso de peixes) e verifique se há excesso.
Se houver, gravar na variável excesso e na variável
multa o valor da multa que João deverá pagar.
Caso contrário mostrar tais variáveis com o conteúdo ZERO. 
Data: 16/09/21
"""

# Entrada de dados
print("======================================================")
print("CALCULADORA DE MULTA POR EXCESSO NA PESAGEM DOS PEIXES")
print("======================================================")
print(" ")
peixes_peso = float(input("Informe o peso dos peixes (em quilogramas): "))
print(" ")

# Processamento e saída de dados
if (peixes_peso > 50):
    excesso = (peixes_peso - 50)
    multa = (excesso*4)
    print("=========")
    print("Resultado")
    print("=========")
    print(" ")
    print("O peso dado apresenta um excesso de aproximadamente %.3fKg." %(excesso))
    print("A multa para esse excesso é de R$%.2f." %(multa))

else:
    print("=========")
    print("Resultado")
    print("=========")
    print(" ")
    excesso = 0
    multa = 0
    print("O peso dado apresenta um excesso de 0Kg.")
    print("Como não há excesso, a multa é nula, ou seja, de R$0.")
    




