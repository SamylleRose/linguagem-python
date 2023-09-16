variable = input('Digite algo: ')
print('O tipo primitivo desse valor é: ',type(variable))
print('Só tem espaço? {}\nÉ um numero? {}\nÉ alfabético? {}\nÉ alfanumérico? {}\nEstá em maiúsculo? {}\nEstá em minúsculo? {}\nEstá capitalizada? {}\n '.format(variable.isspace(), variable.isnumeric(), variable.isalpha(), variable.isalnum(), variable.isupper(), variable.islower(), variable.istitle()))