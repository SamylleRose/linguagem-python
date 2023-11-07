agenda = []

for c in range(10):
    print(f'Dados da {c + 1}° pessoa:\n')
    nome = input('Nome: ')
    endereço = input('Endereço: ')
    cep = int(input('CEP: '))
    bairro = input('Bairro: ')
    telefone = int(input('telefone: '))

    pessoa = [nome, endereço, cep, bairro, telefone]
    agenda.append(pessoa)

agenda.reverse()

for c in range(10):
    print(agenda[c])



