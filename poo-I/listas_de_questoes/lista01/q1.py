while True: 
    objeto = input('Qual forma geometrica deseja calcular a area?(triangulo, quadrado ou circulo) ')

    if objeto == 'triangulo':
        base = float(input('Informe a tamanho da base do triangulo: '))
        altura = float(input('Informe a tamanho da altura do triangulo: '))
        area_triangulo = (base * altura) / 2
        print(f'Área do triangulo é {area_triangulo:.2f}cm²')

    elif objeto == 'quadrado':
        lado = float(input('Informe o tamanho da lateral do quadrado: '))
        area_quadrado = lado * lado
        print(f'Área do quadrado é {area_quadrado:.2f}cm²')

    elif objeto == 'circulo':
        raio = float(input('Informe o tamanho do raio do circulo: '))
        area_circulo = 3.14159265359 * (raio ** 2) 
        print(f'Área do circulo é {area_circulo:.2f}cm²')

    resposta = input('Deseja finalizar o código?(s/n) ')
    
    if resposta == 's':
        break
