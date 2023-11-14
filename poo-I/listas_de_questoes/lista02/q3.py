string = input("Digite uma palavra: ")
letra = input("Digite a letra que deseja encontra a posição: ")
contador = 0
for c in string:
    if letra == c:
        print(f' A letra "{letra}" está na posição {contador}.')
    contador += 1
