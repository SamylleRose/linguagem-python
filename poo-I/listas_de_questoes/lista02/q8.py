import random

gabarito = [random.randint(1, 3) for _ in range(13)]
cartão_de_aposta01 = [random.randint(1, 3) for _ in range(13)]
cartão_de_aposta02 = [random.randint(1, 3) for _ in range(13)]
cartão_de_aposta03 = [random.randint(1, 3) for _ in range(13)]
# print(gabarito)
# print(cartão_de_aposta01)
# print(cartão_de_aposta02)
# print(cartão_de_aposta03)


def verificacao_de_acertos(gabarito, cartão_do_apostador, numero_do_apostador):
    contador = 0
    acertos = 0
    for c in gabarito:
        if c == cartão_do_apostador[contador]:
            acertos += 1
        
        contador += 1 
    
    if acertos == 13:
        print(f'Parabéns o apostador {numero_do_apostador} é o ganhador!')
    
    else:
        print(f'O apostador {numero_do_apostador} acertou apenas {acertos} números.')
    

verificacao_de_acertos(gabarito, cartão_de_aposta01, 1)
verificacao_de_acertos(gabarito, cartão_de_aposta02, 2)
verificacao_de_acertos(gabarito, cartão_de_aposta03, 3)