dicionario = {"fernando": [2, 6, 7], "paulo": [10, 8, 8], "maria": [3, 10, 8]}


def calcular_media(dicionario):
    medias = {}
    soma = 0
    quantidade_de_notas = 0

    for chave, valor in dicionario.items():
        soma = sum(valor)
        quantidade_de_notas = len(valor)
        media = soma / quantidade_de_notas
        medias[chave] = media

    return medias


def analise_de_nota(medias):
    nota_analisada = {}

    for chave, media in medias.items():
        if media >= 7:
            nota_analisada[chave] = "Aprovado"

        else:
            nota_analisada[chave] = "Reprovado"

    return nota_analisada


medias = {}
medias = calcular_media(dicionario)
nota_analisada = analise_de_nota(medias)

print(f"A media dos alunos:")
for chave, valor in medias.items():
    print(chave, valor)

print(f"\nAlunos aprovados e reprovados:")
for chave, valor in nota_analisada.items():
    print(chave, valor)
