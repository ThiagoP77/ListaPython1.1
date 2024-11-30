"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: Faça um Programa para uma loja de tintas. O programa
deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros
quadrados e que a tinta é vendida em latas de 18 litros, que custam
R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
a.  Informe ao usuário as quantidades de tinta a serem compradas
e os respectivos preços em 3 situações:
b.  comprar apenas latas de 18 litros;
c.  comprar apenas galões de 3,6 litros;
d.  misturar latas e galões, de forma que o preço seja o menor.
Acrescente 10% de folga nas misturas (se necessário)
e sempre arredonde os valores para cima, isto é, considere latas cheias.
Data: 19/09/21
Atualização: 20/09/21
"""

# Entrada de dados
print("============================================================")
print("CALCULADORA: LATAS/GALÕES DE TINTA NECESSÁRIOS E PREÇO TOTAL")
print("============================================================")
print(" ")
metros_quadrados = float(input("Informe quantos metros quadrados devem ser pintados: "))
print(" ")

# Processamento de dados
litros_necessarios = (metros_quadrados/6)
latas_tinta = int(litros_necessarios/18)

if(litros_necessarios%18 != 0):
    latas_tinta = (latas_tinta + 1)

galoes_tinta = int(litros_necessarios/3.6)

if(litros_necessarios%3.6 != 0):
    galoes_tinta = (galoes_tinta + 1)

preco_latas = (latas_tinta*80)
preco_galoes = (galoes_tinta*25)

combinacao_lata = int(litros_necessarios/18)
combinacao_galao = int((litros_necessarios%18)/3.6)

if (((litros_necessarios%18)%3.6) != 0):
    combinacao_galao = (combinacao_galao + 1)

preco_combinacao = ((combinacao_lata*80)+(combinacao_galao*25))

if (preco_combinacao>preco_latas) and (preco_combinacao<preco_galoes):
    combinacao_galao = 0
    combinacao_lata = (latas_tinta)
    preco_combinacao = preco_latas
    
if (preco_combinacao>preco_galoes) and (preco_combinacao<preco_latas):
    combinacao_lata = 0
    combinacao_galao = (galoes_tinta)
    preco_combinacao = preco_galoes
    
# Saída de dados
print("=======================")
print("Resultados dos Cálculos")
print("=======================")
print(" ")
print("São necessários %.2fL de tinta para pintar %.2fm²."%(litros_necessarios, metros_quadrados))
print("Só latas: Serão necessárias %d lata(s) de tinta, custando R$%.2f."%(latas_tinta, preco_latas))
print("Só galões: Serão necessários %d galão(s) de tinta, custando R$%.2f."%(galoes_tinta, preco_galoes))
print("Combinação: Serão necessários %d lata(s) e %d galão(s), custando R$%.2f."%(combinacao_lata, combinacao_galao, preco_combinacao))
if (preco_combinacao<preco_galoes) and (preco_combinacao<preco_latas):
    print(" ")
    print("A opção que sai mais barata é a de combinação!")
elif (preco_combinacao==preco_galoes) and (preco_combinacao<preco_latas):
    print(" ")
    print("As opções que saem mais baratas são a de combinação e a de somente galões!")
elif (preco_combinacao==preco_latas) and (preco_combinacao<preco_galoes):
    print(" ")
    print("As opções que saem mais baratas são a de combinação e a de somente latas!")
