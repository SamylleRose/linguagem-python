dicionario = {}
dicionario["nome"] = input("Insira o seu nome: ")
dicionario["média"] = int(input("Insira sua média: "))


if dicionario["média"] >= 7:
    dicionario["situação"] = "Aprovado"

elif 5 <= dicionario["média"] < 7:
    dicionario["situação"] = "Recuperação"
else:
    situacao = "Reprovado"

for c, v in dicionario.items():
    print(f"{c} é igual a {v}")
