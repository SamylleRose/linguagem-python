value = int(input('Digite o número para ver sua tabuada: '))
print('=' * 12)
for c in range(1,10):
    multiplier = value * c
    print('{} x {} = {}'.format(value, c, multiplier))
    
print('=' * 12)