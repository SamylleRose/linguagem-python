def isPar(numero):
    if numero%2 == 0:
        return True
    else:
        return False
    
lista = [0, 1, 2, 3, 4, 5]
resultado = filter(isPar, lista)

print(list(resultado))