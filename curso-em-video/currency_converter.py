valor_em_real = float(input('Quanto em real você possui? '))
convertor = valor_em_real / 4.97 
print(' Com R${:.2f} reais é possivel comprar US{:.2f} dolares'. format(valor_em_real, convertor))