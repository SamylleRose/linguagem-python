def somar_impares(numero):
    if numero % 2 == 1:
        return True
    else:
        return False
    
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8]
resultado = filter(somar_impares, lista)
soma = 0

for c in resultado:
    soma += c

print(soma)