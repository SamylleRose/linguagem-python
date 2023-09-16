speed = int(input('Digite a velocidade do veiculo: '))
if speed > 80:
    value_fine = (speed - 80 ) * 7
    print('MULTADO! Valor da multa é R$ {}'.format(value_fine))

else:
    print('Você não foi multado, tenha um bom dia.')