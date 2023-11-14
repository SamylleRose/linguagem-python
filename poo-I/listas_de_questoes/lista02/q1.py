def tamString():
    string = input("Digite uma palavra: ")
    contador = 0

    for c in string:
        contador += 1

    print(f"O tamanho da string:{contador}")


tamString()
