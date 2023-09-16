lista_valore = []

for c in range(0, 5):
    lista_valore.append(int(input('Digite o valor {}: '. format(c + 1 ))))

verificar_maior = lista_valore[0]
verificar_menor = lista_valore[0]
# posicao_maior = 1
# posicao_menor = 1

for c in range(5):
    if verificar_maior < lista_valore[c]:
        verificar_maior = lista_valore[c]
        posicao_maior = c 

    if verificar_menor > lista_valore[c]:
        verificar_menor = lista_valore[c]
        posicao_menor = c

print('O numero maior na lista é {} e esta na posição {}, o menor numero é {} e esta na posição {}'. format(verificar_maior, posicao_maior, verificar_menor, posicao_menor))