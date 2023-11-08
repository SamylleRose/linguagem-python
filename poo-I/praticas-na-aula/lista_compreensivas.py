n = 13

divisores = [x for x in range(1, n + 1) if n % x == 0]

if len(divisores) <= 2:
    print("E primo")
else:
    print("ne primo n")
