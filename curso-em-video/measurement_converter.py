value_meters = int(input('Digite uma valor em metros: '))
Kilometer = value_meters / 1000
hectometer = value_meters / 100
decameter = value_meters / 10
decimeter = value_meters * 10
centimeter = value_meters * 100
millimeter = value_meters * 1000

print('Medida de {:.2f}m em:'.format(value_meters))
print('{}km'.format(Kilometer))
print('{}hm'.format(hectometer))
print('{}dam'.format(decameter))
print('{}dm'.format(decimeter))
print('{}cm'.format(centimeter))
print('{}mm'.format(millimeter))
