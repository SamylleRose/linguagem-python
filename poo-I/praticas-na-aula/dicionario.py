dicionario = {'pessoa': '1345', 'nome': ' samylle'}

nome = input('Digite a sua busca: ')
if nome in dicionario:  
    print(dicionario[nome])

else:
    print('Não encontrado!')