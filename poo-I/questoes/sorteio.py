#   Faça um programa para sorteio de números inteiros:
#  1. Ousuário informa os limites dos números sorteados;
#  2. Ousuário informa quantos números serão sorteados;
#  3. Oprogramamostra os números sorteados;
#  4. Nãopodemostrarnúmeros já sorteados.

import random 

limite_inicial = int(input('Digite o inicio do limite: '))
limite_final = int(input('Digite o final do limite: '))
quantidade_sorteada = int(input('Digite a quantidade que deseja sortear: '))
numeros = []

for c in range(quantidade_sorteada):
    while True:
        numero =  random.randint(limite_inicial, limite_final)

        if numero not in numeros:
            numeros.append(numero)

            break

print(numeros)