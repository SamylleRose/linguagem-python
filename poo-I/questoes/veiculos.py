# Quantos litros de combustivel cada um dos
#  carros cadastrados consome para percorrer
#  uma distância de 1000 quilômetros e quanto
#  isto custará, considerando um que a gasolina
#  custe R$ 2,25 o litro. Abaixo segue uma tela de
#  exemplo. O disposição das informações deve
#  ser o mais próxima possível ao exemplo. Os
#  dados são fic cios e podem mudar a cada
#  execução do programa.

veiculo1 = ['fusca', 7]
veiculo2 = ['gol', 10]
veiculo3 = ['uno', 12.5]
veiculo4 = ['vectra', 9]
veiculo5 = ['peugeout', 14.5]

carros = [veiculo1, veiculo2, veiculo3, veiculo4, veiculo5]

veiculo_mais_economico = veiculo1[0]
menor_gasto_combustivel = (1000 / veiculo1[1]) * 2.25
index = 1
for c in carros:
    litros = (1000 / c[1]) 
    custo = litros * 2.25

    print(f'{index} - {c[0]:<10}               - {c[1]:<6.1f} - {litros:<6.1f} litros - R$ {custo:<6.1f}')
    index += 1
    if custo < menor_gasto_combustivel:
        veiculo_mais_economico = c[0]
        menor_gasto_combustivel = custo

print(f'O menor consumo é do {veiculo_mais_economico}')


