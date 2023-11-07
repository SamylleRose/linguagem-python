import random
import math

lista = []
lista = [random.randint(0, 100) for c in range(100)]

soma = 0
for c in lista:
    soma += c

media = soma / 100

lista.sort()
mediana = (lista[ 100 // 2 - 1] + lista[100 // 2]) / 2

soma_diferencas_quadradas = sum((x - media) ** 2 for x in lista)
variancia = soma_diferencas_quadradas / (100 - 1)

desvio_padrao = math.sqrt(variancia)

print(f'Média: {media:.2f}\nMediana: {mediana:.2f}\nVariância: {variancia:.2f}\nDesvio padrão: {desvio_padrao:.2f}')
