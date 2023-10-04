import math

cateto_opposite = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacent= float(input('Digite comprimento do cateto adjacente: '))
# hypotenuse = (cateto_opposite ** 2 + cateto_adjacent ** 2) ** (1/2) 
hypotenuse = math.hypot(cateto_opposite, cateto_adjacent)
print(f'A hipotenusa é {hypotenuse:.2f}')


