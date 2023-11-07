nome_da_cidade = input('Digite o nome de uma cidade: ')

lista_da_cidade = list(nome_da_cidade)

for i in range(len(lista_da_cidade)):
    for j in range(len(lista_da_cidade) - 1):
        if lista_da_cidade[j] > lista_da_cidade[ j + 1]:
            letra_de_troca = lista_da_cidade[ j + 1]
            lista_da_cidade[j + 1] = lista_da_cidade[j]
            lista_da_cidade[j] = letra_de_troca

novo_nome_da_cidade = ''.join(lista_da_cidade)
print('O novo nome da cidade é:', novo_nome_da_cidade)