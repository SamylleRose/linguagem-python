# . Escreva um programa que cria uma lista de 10 posições e mostre-a. Em seguida, troque o 
# primeiro elemento pelo o último, o segundo com o penúltimo, o terceiro com o antepenúltimo 
# e, assim, sucessivamente. Mostre a nova lista após todas as trocas.

lista = [1,4,7,9,5,2,3]
contador = 0
tamanho_da_lista = len(lista) - 1
for c in range(len(lista) // 2):
    numero_de_troca = lista[c]
    lista[c] = lista[tamanho_da_lista - contador]
    lista[tamanho_da_lista - contador] = numero_de_troca
    contador += 1
print(lista)
    
 