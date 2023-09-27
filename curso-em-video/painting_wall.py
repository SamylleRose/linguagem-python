width = float(input('Digite a largura: '))
height = float(input('Digite a altura: '))
area = width * height
amount_of_ink =  area / 2 
print('Sua parede tem a dimensão de {}x{} e sua área é de {:.2f}m².\nPara pintar essa parede, você precisa de {:.2f}l'. format(width, height, area, amount_of_ink))