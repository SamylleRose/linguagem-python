lista_values = []

for c in range(0, 5):
    lista_values.append(int(input('Digite o valor {}: '. format(c + 1 ))))

check_bigger = lista_values[0]
check_minor = lista_values[0]

for c in range(5):
    if check_bigger < lista_values[c]:
        check_bigger = lista_values[c]
        posicao_maior = c 

    if check_minor > lista_values[c]:
        check_minor = lista_values[c]
        posicao_menor = c

print('O numero maior na lista é {} e esta na posição {}, o menor numero é {} e esta na posição {}'. format(check_bigger, posicao_maior, check_minor, posicao_menor))