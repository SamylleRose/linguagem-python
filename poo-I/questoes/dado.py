import random

contador = [0, 0, 0, 0, 0, 0]

for c in range(100):
    numero =  random.randint(1, 6)
    contador[numero - 1] += 1

print(f'O dado caiu no 1, {contador[0]} vezes  \nO dado caiu no 2, {contador[1]} vezes \nO dado caiu no 3, {contador[2]} vezes \nO dado caiu no 4, {contador[3]} vezes \nO dado caiu no 5, {contador[4]} vezes \nO dado caiu no 6, {contador[5]} vezes')

