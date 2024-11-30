"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: Faça um Programa que pergunte quanto você ganha
por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
Data: 16/09/21
"""
# Entrada de dados
print("==============================")
print("CALCULADORA DE SALÁRIO LÍQUIDO")
print("==============================")
print(" ")
print("-Informe os dados exigidos abaixo-")
print(" ")
horas_mensais = float(input("Digite quantas horas você trabalhou nesse referido mês: "))
ganho_hora = float(input("Digite o valor pago por hora: "))
print(" ")

# Processamento de dados
salario_bruto = (horas_mensais * ganho_hora)
imposto_renda = ((salario_bruto/100)*11)
inss = ((salario_bruto/100)*8)
sindicato = ((salario_bruto/100)*5)
salario_liquido = (salario_bruto - imposto_renda - inss - sindicato)

# Saída de dados
print("=======================")
print("Resultados dos Cálculos")
print("=======================")
print(" ")
print("Seu salário bruto é de R$%.2f." %(salario_bruto))
print("O valor descontado pelo Imposto de Renda é de R$%.2f." %(imposto_renda))
print("O valor descontado pelo INSS é de R$%.2f." %(inss))
print("O valor descontado pelo sindicato é de R$%.2f." %(sindicato))
print("Seu salário líquido é de aproximadamente R$%.2f." %(salario_liquido))


