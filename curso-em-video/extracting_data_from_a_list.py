continua = "s"
lista = []
while continua == "s":
    valor_digitado = int(input("Digite um valor: "))
    lista.append(valor_digitado)
    lista.sort(reverse=True)
    continua = input("Deseja continuar:(s/n) ")

print(f"Os valores em ordem descrecente são {lista}.")
if 5 in lista:
    print("O valor 5 foi encontrado na lista!")
else:
    print("O valor 5 não foi encontrado!")
