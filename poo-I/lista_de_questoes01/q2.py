def calcular_fatorial_iterativo(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

def calcular_fatorial_recursivo(numero):
    if numero == 0:
        return 1
    else:
        return numero * calcular_fatorial_recursivo(numero - 1)
    

numero = int(input('Digite um numero: '))

resultado_interativo = calcular_fatorial_iterativo(numero)
resultado_recursivo = calcular_fatorial_recursivo(numero)
print(f'O fatorial de {numero} calculado de forma interativa é {resultado_interativo}')
print(f'O fatorial de {numero} calculado de forma recursiva é {resultado_recursivo}')