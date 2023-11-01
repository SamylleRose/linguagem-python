agenda = {}

def menu():
    print('1 - Cadrastrar')
    print('2 - printar')
    print('3 - finalizar\n')

    codigo = int(input('Digite um codigo: '))
    return codigo

while True:
    codigo = menu()

    if codigo == 1:
        nome = input('\nDigite o seu nome: ')
        telefone = int(input('Digite o número de telefone: '))

        if nome in agenda.keys():
         print('\nJá está cadastrado!')

        else:
            agenda[nome] = telefone

    if codigo == 2:
        for nome in agenda.keys():
            print(nome, agenda[nome])     
            print('\n')

    if codigo == 3:
        break


