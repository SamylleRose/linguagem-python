def metade(numero):
    return numero/2

lista = [0, 1, 2, 3, 4, 5]
resultado = map(metade, lista)

print(list(resultado))