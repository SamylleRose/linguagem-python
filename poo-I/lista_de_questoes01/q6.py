ingresso = 120
lucro_maior = 0
quantidade_vendidos = 0
preco_do_ingresso = 0

for i in range(10, 1, -1):
    value = i / 2.0 
    lucro = (value * ingresso) - 200

    print(f'Preço do ingresso: {value:.2f}, Quantidade vendida: {ingresso:.2f}, Lucro: {lucro:.2f}')
    
    if lucro > lucro_maior:
        lucro_maior = lucro
        preco_do_ingresso = value
        quantidade_vendidos = ingresso
    
    ingresso += 26 
    
    if i == 2:
        print()
        print(f'Lucro máximo: {lucro_maior:.2f}')
        print(f'Preço do ingresso: {preco_do_ingresso:.2f}')
        print(f'Quantidade vendidas: {quantidade_vendidos}')