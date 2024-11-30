"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: Tendo como dados de entrada a altura e o sexo de
uma pessoa, construa um algoritmo que calcule seu
peso ideal, utilizando as seguintes fórmulas:
a.  Para homens: (72.7*h) - 58
b.  Para mulheres: (62.1*h) - 44.7 (h = altura)
c.  Peça o peso da pessoa e informe se ela está dentro,
acima ou abaixo do peso.
Data: 16/09/21
"""

# Entrada de dados
print("=========================")
print("CALCULADORA DE PESO IDEAL")
print("=========================")
print(" ")
print("-Informe os dados exigidos abaixo-")
print(" ")
sexo = str(input("Informe seu sexo (utilizando M para masculino e F para feminino): "))
altura = float(input("Informe sua altura (em metros): "))
peso = float(input("Informe seu peso (em quilogramas): "))
print(" ")

# Processamento de dados
if (sexo == "M") or (sexo == "m") or (sexo == "Masculino") or (sexo == "masculino"):
    peso_ideal = ((72.7*altura) - 58)
    
elif (sexo == "F") or (sexo == "f") or (sexo == "Feminino") or (sexo == "feminino"):
    peso_ideal = ((62.1*altura) - 44.7)

# Saída de dados
if  (sexo == "M") or (sexo == "m") or (sexo == "Masculino") or (sexo == "masculino"):
    print("=========")
    print("Resultado")
    print("=========")
    print(" ")
    print ("Seu peso ideal é de aproximadamente %.2fKg." %(peso_ideal))
    if (peso == peso_ideal):
        print("Você está exatamente no peso ideal para sua altura e sexo. Parabéns!")
    elif (peso > peso_ideal):
        print("Você está a cima do peso ideal para sua altura e sexo.")
    elif (peso < peso_ideal):
        print("Você está abaixo do peso ideal para sua altura e sexo.")

elif (sexo == "F") or (sexo == "f") or (sexo == "Feminino") or (sexo == "feminino"):
    print("=========")
    print("Resultado")
    print("=========")
    print(" ")
    print ("Seu peso ideal é de aproximadamente %.2fKg." %(peso_ideal))
    if (peso == peso_ideal):
        print("Você está exatamente no peso ideal para sua altura e sexo. Parabéns!")
    elif (peso > peso_ideal):
        print("Você está a cima do peso ideal para sua altura e sexo.")
    elif (peso < peso_ideal):
        print("Você está abaixo do peso ideal para sua altura e sexo.")

else:
    print("Parece que você preencheu os dados de forma diferente do que é pedido!")
    print("Por favor, reinicie o programa e insira os dados corretamente.")
