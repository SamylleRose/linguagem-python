lista = [0, 1, [2, [3, 4]], 5]

def imprimir_lista(lista):
    for c in lista:
        if isinstance(c, list):
            imprimir_lista(c)
        else:
            print(c)

imprimir_lista(lista)