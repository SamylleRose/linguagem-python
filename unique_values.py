list_valores = []

list_valores.append(int(input('Digite um valor: '))) 
resposta = str(input('Deseja inserir mais um valor? s/n: '))

while resposta == 's':
    valor = int(input('Digite um valor: '))
    
    if valor not in list_valores:
        print('Novo valor adicionado!')
        list_valores.append(valor) 
    else:
        print('Valor já existe na lista!')        
            

    resposta = str(input('Deseja inserir mais um valor? s/n: '))

list_valores.sort()

print('Os valores digitados foram:\n {}'.format(list_valores))





