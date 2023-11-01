import functools as ft

def soma(x, y):
    return x + y

lista = [1, 2, 3, 4, 5]
resultado = ft.reduce(soma, lista)

print(resultado)

