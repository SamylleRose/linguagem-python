# c. excluirTelefone – essa função exclui um telefone de uma pessoa que já está na
# agenda. Se a pessoa tiver apenas um telefone, ela deve ser excluída da agenda.

# d. excluirNome – essa função exclui uma pessoa da agenda.

# e. consultarTelefone – essa função retorna os telefones de uma pessoa na agenda.
# f. Quando o usuário digitar um número negativo o programa é encerrado

agenda = {}


def incluirNovoNome(nome, telefones):
    if nome not in agenda:
        agenda[nome] = telefones
    else:
        agenda[nome].extend(telefones)


def incluirTelefone(nome, telefone):
    if nome in agenda:
        agenda[nome].append(telefone)
    else:
        resposta = input(f"{nome} não está na agenda. Deseja incluí-lo? (s/n): ")
        if resposta.lower() == "s":
            incluirNovoNome(nome, [telefone])


def excluirTelefone(nome, telefone):
    if nome in agenda:
        if telefone in agenda[nome]:
            agenda[nome].remove(telefone)
            if len(agenda[nome]) == 0:
                del agenda[nome]


def excluirNome(nome):
    if nome in agenda:
        del agenda[nome]


def consultarTelefone(nome):
    if nome in agenda:
        return agenda[nome]
    else:
        return []


while True:
    print("\n--------Menu---------")
    print("1. Incluir Novo Nome")
    print("2. Incluir Telefone")
    print("3. Excluir Telefone")
    print("4. Excluir Nome")
    print("5. Consultar Telefone")
    print("6. Sair")

    escolha = int(input("\nEscolha uma opção: "))

    if escolha == 1:
        nome = input("\nDigite o nome: ")
        telefones = input("Digite os telefones separados por espaço: ").split(" ")
        incluirNovoNome(nome, telefones)
    elif escolha == 2:
        nome = input("\nDigite o nome: ")
        telefone = input("Digite o telefone: ")
        incluirTelefone(nome, telefone)
    elif escolha == 3:
        nome = input("\nDigite o nome: ")
        telefone = input("Digite o telefone: ")
        excluirTelefone(nome, telefone)
    elif escolha == 4:
        nome = input("\nDigite o nome: ")
        excluirNome(nome)
    elif escolha == 5:
        nome = input("\nDigite o nome: ")
        telefones = consultarTelefone(nome)
        if telefones:
            print(f"\nTelefones de {nome}: {' '.join(telefones)}")
        else:
            print(f"\n{nome} não está na agenda.")
    elif escolha == 6:
        break
    else:
        print("Opção inválida. Tente novamente.")

print("Agenda encerrada.")
