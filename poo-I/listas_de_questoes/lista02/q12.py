voltas_dos_corredores = {}

for c in range(2):
    print(f"Voltas do {c + 1}° corredor:")
    nome_do_corredor = input("Nome do corredor: ")
    volta01 = float(input("Primeira volta: "))
    volta02 = float(input("Primeira volta: "))
    volta03 = float(input("Primeira volta: "))

    voltas_dos_corredores[nome_do_corredor] = [volta01, volta02, volta03]


print(voltas_dos_corredores)

nome_dos_corredores = list(voltas_dos_corredores.keys())
nome_do_corredor_da_melhor_volta = nome_dos_corredores[0]

voltas_do_corredor01 = voltas_dos_corredores[nome_do_corredor_da_melhor_volta]
tempo_da_melhor_volta = min(voltas_do_corredor01)
a_melhor_volta_do_corredor = voltas_do_corredor01.index(tempo_da_melhor_volta) + 1

for nome_do_corredor, voltas_do_corredor in voltas_dos_corredores.items():
    if min(voltas_do_corredor) < tempo_da_melhor_volta:
        tempo_da_melhor_volta = min(voltas_do_corredor)
        nome_do_corredor_da_melhor_volta = nome_do_corredor
        melhor_volta_do_corredor = voltas_do_corredor.index(tempo_da_melhor_volta) + 1

print(
    f"A melhor volta da prova foi do corredor {nome_do_corredor_da_melhor_volta} na {a_melhor_volta_do_corredor}° volta."
)

media_tempos = {}
for corredor, tempos in voltas_dos_corredores.items():
    media = sum(tempos) / len(tempos)
    media_tempos[corredor] = media

# Encontrar o corredor com a menor média (o campeão)
campeao = min(media_tempos, key=media_tempos.get)

# Imprimir os resultados
print(
    f"O campeão da prova é {campeao} com uma média de {media_tempos[campeao]:.2f} segundos."
)
