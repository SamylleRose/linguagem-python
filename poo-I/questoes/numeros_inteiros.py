lista = [0, 2, 0, 7, 4, 0, 6, 5, 9, -1, 18]

def isPar(numero):
    if numero > 0 and numero % 2 == 0:
        return True
    else:
        return False
    
def isImpar(numero):
    if numero > 0 and numero % 2 == 1:
        return True
    else:
        return False
        
def isZero(numero):
    return numero == 0
    
while True:
    numero = int(input('Digite um valor: '))

    if numero < 0:
        break

    lista.append(numero)

lista.sort()

lista_isPar = list(filter(isPar, lista))
lista_isImpar = list(filter(isImpar, lista))
lista_isZero = list(filter(isZero, lista))

print( lista_isPar + lista_isZero + lista_isImpar)
