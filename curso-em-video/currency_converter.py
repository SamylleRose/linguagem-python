real_value = float(input('Quanto em real você possui? '))
converter= real_value / 4.97 
print(' Com R${:.2f} reais é possivel comprar US{:.2f} dolares'. format(real_value, converter))