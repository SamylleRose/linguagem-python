lista = []
for c in range(5):
    valor_digitado = int(input("Digite um valor:"))

    if c == 0 or valor_digitado > lista[len(lista) - 1]:
        lista.append(valor_digitado)
        print("Adicionado no final da lista.")
    else:
        posicao = 0

        while posicao < len(lista):
            if valor_digitado <= lista[posicao]:
                lista.insert(posicao, valor_digitado)
                print(f"Adicionado na posição {posicao} da lista.")
                break
            posicao += 1

print(f"Os valoress digitados em ordem foram {lista}")
