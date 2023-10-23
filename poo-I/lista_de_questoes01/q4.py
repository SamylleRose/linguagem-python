
def verificar_numero_primo(numero_inteiro):

    contador_de_divisao = 0

    for c in range(numero_inteiro - 1, 1, -1):
        if numero_inteiro % c == 0:
            contador_de_divisao += 1

    if contador_de_divisao == 0:
        return True

    else:
        return False


numero1 = int(input())
numero2 = int(input())

if numero1 > numero2:
    [numero1, numero2] = [numero2, numero1]

nao_ha_primos = 1

for i in range(numero1, numero2 + 1):
    if(verificar_numero_primo(i)):
        print(i)
        nao_ha_primos = 0


if nao_ha_primos:
    print('Não existe nenhum número primo dentro desse intervalo')