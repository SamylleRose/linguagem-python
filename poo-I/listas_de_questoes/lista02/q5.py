import random

def gerar_numero_aleatorio():
    return random.randint(0, 100)

def jogo_de_adivinhacao():
    print('Bem-vindo ao jogo de adivinhação\n')

    tentativa = 10
    ganhou = False

    while tentativa > 0:
        numero_aleatorio = gerar_numero_aleatorio()
        # print(numero_aleatorio)
        palpite = int(input('Digite seu palpite: '))

        if palpite == numero_aleatorio:
            print('\nParabéns, você acertou!!')
            ganhou = True
            break

        tentativa -= 1
        if tentativa > 0:
            print(f'\nVocê errou, tente novamente! Restam {tentativa} tentativas.')
        else:
            print('\nVocê excedeu o número máximo de tentativas. O número era', numero_aleatorio)

    return ganhou

continuacao = 's'

while continuacao == 's':
    if jogo_de_adivinhacao():
        continuacao = input('\nDeseja continuar a jogar: s/n ')
    else:
        break
