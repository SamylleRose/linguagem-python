numero_decimal = int(input('Digite um numero em decimal: '))
numero_binario = ''

if numero_decimal == 0:
    numero_binario = '0'
    
else:
    while numero_decimal > 0: 
        resto = numero_decimal  % 2
        numero_decimal  = numero_decimal // 2  
        numero_binario = str(resto) + numero_binario
    
print(numero_binario)    