# Vimos em sala de aula o método find e index que retornam a posição de um caracter dentro 
# de uma string. Por exemplo: “Teste”.find(“T”), a saída será 0. Implemente sua solução de 
# procurar um caracter em uma string sem utilizar os métodos find ou o index.

string = input('Digite uma palavra: ')
letra = input('Digite a letra que deseja encontra a posição: ')
contador = 0
for c in string:
    if letra == c:
        print(f' A letra "{letra}" está na posição {contador}.')
    contador += 1