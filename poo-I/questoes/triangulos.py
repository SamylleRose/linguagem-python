# Dado três lados de um triângulo verifique se é possível formar um triângulo. Em
#  seguida diga se ele é equilátero, isóseles ou escaleno.
#  Lembre-se: Não é possível formar triângulo quando um lado é maior que a soma dos
#  outros dois!
#  Lembrete:
#  Equilátero: todos lados iguais;
#  Isóceles: um lado diferente;
#  Escaleno: todos os lados diferentes.

lado_A = int(input('Digite o lado A: '))
lado_B = int(input('Digite o lado B: '))
lado_C = int(input('Digite o lado C: '))

if lado_A >= (lado_B + lado_C) or lado_B >= (lado_A + lado_C) or lado_C >= (lado_A + lado_B):
    print('Não é possível formar triângulo quando um lado é maior que a soma dos outros dois!')

elif lado_A == lado_B and lado_B == lado_C:
    print('Triangulo é equilátero!')

elif lado_A != lado_B and lado_B != lado_C and lado_A != lado_C:
    print('Triangulo é escaleno!')

else:
    print('Triângulo é isóceles! ')