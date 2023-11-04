notas = {}

for c in range(2):
    nome = input('Digite o nome do aluno: ')
    nota01 = float(input('Digite a primeira nota: '))
    nota02 = float(input('Digite a segunda nota:'))

    notas[nome] = [nota01, nota02]

print('\nAs notas dos alunos são:\n')

for nome in notas.keys():
    print(nome, notas[nome])     

def media_das_notas():
    retorno = 'Aluno não encontrado!'
    nome_do_aluno = input('Qual aluno deseja calcular a média das notas? ')

    if nome_do_aluno in notas.keys():
        notas_do_aluno = notas[nome_do_aluno]
        soma_das_notas = 0

        for c in notas_do_aluno:
            soma_das_notas += c

        quantidade_de_notas = len(notas_do_aluno)
        media = soma_das_notas / quantidade_de_notas
        retorno = f'A média do aluno é: {media}'
        
    return retorno

media = media_das_notas()
print(media)
