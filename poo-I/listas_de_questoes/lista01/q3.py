def calcular_fatorial_recursivo(numero):
    if numero == 0:
        return 1
    else:
        return numero * calcular_fatorial_recursivo(numero - 1)

def combination(n, p):
    return calcular_fatorial_recursivo(n) / calcular_fatorial_recursivo(n-p)

def arrangement(n, r):
    return calcular_fatorial_recursivo(n) / (calcular_fatorial_recursivo(r) * calcular_fatorial_recursivo(n-r))

print(combination(5, 5))
print(arrangement(5, 5))