rental_days = int(input('Quantos dias alugados? '))
travelled_distance = float(input('Quanto km rodados? '))
value = (rental_days * 60) + (0.15 * travelled_distance)
print(f'O total a pagar pelo aluguel é R${value:.2f} reais.')