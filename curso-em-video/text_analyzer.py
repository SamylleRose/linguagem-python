name = str(input('Digite seu nome completo: ')).strip()

print('Seu nome em maiúsculo: {}'.format(name.upper()))
print('Seu nome em minúsculo: {}'.format(name.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(name) - name.count(' ')))
separate = name.split()
print('o seu primeiro nome é {} e tem {} letras.'.format(separate[0], len(separate[0])))