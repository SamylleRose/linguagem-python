# Dada a lista=[12,-2,4,8,29,45,78,36,-17,2,12,8,3,3,-52] faça um 
# programa que: 
# ▫ imprima o maior elemento
#  ▫ imprima o menor elemento
#  ▫ imprima os números pares 
# ▫ imprima o número de ocorrências do primeiro elemento da lista
#  ▫ imprima a média dos elementos
#  ▫ imprima a soma dos elementos de valor negativoS

lista=[12,-2,4,8,29,45,78,36,-17,2,12,8,3,3,-52]
numero_maior = lista[0]
numero_menor = lista[0]
numeros_pares = []
numeros_de_ocorrencia = 0
soma_dos_valores = 0
media_dos_valores = 0
soma_dos_valores_negativos = 0 

for c in lista:
    if c > numero_maior:
        numero_maior = c

for c in lista:
    if c < numero_menor:
        numero_menor = c

for c in lista:
    if c % 2 == 0:
        numeros_pares.append(c)

for c in lista:
    if c == lista[0]:
        numeros_de_ocorrencia += 1 

for c in lista:
   soma_dos_valores += c
   
quantidade_de_valores = len(lista)
media_dos_valores = soma_dos_valores / quantidade_de_valores

for c in lista:
    if c < 0:
        soma_dos_valores_negativos += c

print(f'Número maior da lista: {numero_maior} \nNúmero menor da lista: {numero_menor} \nNúmeros pares da lista: {numeros_pares} \nNúmero de ocorrência do primeiro valor da lista: {numeros_de_ocorrencia} \nMédia dos valores: {media_dos_valores:.2f} \nA soma dos valores negativos: {soma_dos_valores_negativos}')