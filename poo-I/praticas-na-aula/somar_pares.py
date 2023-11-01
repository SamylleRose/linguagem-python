import functools as ft

def pares(numero):
    if numero % 2 == 0 and numero != 0:
        return True
    
    else:
        return False

def soma(x, y):
    return x + y

lista = [1, 2, 3, 4, 5]
lista_dos_pares = filter(pares, lista)
resultado = ft.reduce(soma, lista_dos_pares)

print(resultado)