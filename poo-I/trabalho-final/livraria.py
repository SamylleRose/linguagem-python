from cliente import Cliente
from bibliotecario import Bibliotecario
from livro import Livro
from historico import Historico
from documentacao import Documentacao

from random import choice
from datetime import datetime


Documentacao.register(Cliente)
Documentacao.register(Bibliotecario)
Documentacao.register(Livro)
Documentacao.register(Historico)


class Livraria:
    numero_codigos = [str(numero).zfill(5) for numero in range(0, 100000)]

    def __init__(
        self, porcentagem_aluguel=3, tempo_aluguel_dias=-2, multa_atraso_aluguel=2.50
    ) -> None:
        self._receitas = 0
        self._clientes = []
        self._bibliotecarios = [Bibliotecario("usuário padrão", "1", "1")]
        self._livros = []
        self._historico = Historico()
        self._alugueis = {}
        self._porcentagem_aluguel = porcentagem_aluguel
        self._tempo_aluguel_dias = tempo_aluguel_dias
        self._multa_atraso_aluguel = multa_atraso_aluguel

    @property
    def dispesas(self):
        return self._dispesas

    @dispesas.setter
    def dispesas(self, valor):
        self._dispesas = valor

    @property
    def receitas(self):
        return self._receitas

    @receitas.setter
    def receitas(self, valor):
        self._receitas = valor

    @property
    def clientes(self):
        return self._clientes

    @clientes.setter
    def cliente(self, valor):
        self._clientes = valor

    @property
    def bibliotecarios(self):
        return self._bibliotecarios

    @bibliotecarios.setter
    def bibliotecarios(self, valor):
        self._bibliotecarios = valor

    @property
    def livros(self):
        return self._livros

    @livros.setter
    def livros(self, valor):
        self._livros = valor

    @property
    def historico(self):
        return self._historico

    @historico.setter
    def historico(self, valor):
        self._historico = valor

    @property
    def alugueis(self):
        return self._alugueis

    @alugueis.setter
    def alugueis(self, valor):
        self._alugueis = valor

    @property
    def porcentagem_aluguel(self):
        return self._porcentagem_aluguel

    @porcentagem_aluguel.setter
    def porcentagem_aluguel(self, valor):
        self._porcentagem_aluguel = valor

    @property
    def tempo_aluguel_dias(self):
        return self._tempo_aluguel_dias

    @tempo_aluguel_dias.setter
    def tempo_aluguel_dias(self, valor):
        self._tempo_aluguel_dias = valor

    @property
    def multa_atraso_aluguel(self):
        return self._multa_atraso_aluguel

    @multa_atraso_aluguel.setter
    def multa_atraso_aluguel(self, valor):
        self._multa_atraso_aluguel = valor

    @classmethod
    def criar_numero_codigo(cls):
        numero_codigo = -1

        if cls.numero_codigos:
            numero_codigo = choice(cls.numero_codigos)
            cls.numero_codigos.remove(numero_codigo)

        return numero_codigo

    @staticmethod
    def verificar_cpf(cpf, lista):
        gatilho = False

        for i in lista:
            if cpf == i.cpf:
                gatilho = True
                break

        return gatilho

    @staticmethod
    def entrada_float(messagem="\nDigite um preço: R$ "):
        entrada_float = None
        while entrada_float == None:

            try:
                numero = float(input(messagem))

                entrada_float = numero
            except:
                print("\nvalor invalido!\n")

        return entrada_float

    @staticmethod
    def retornar_instancia_pelo_cpf(cpf, lista):
        instancia = None

        for i in lista:
            if cpf == i.cpf:
                instancia = i
                break

        return instancia

    @staticmethod
    def retornar_instancia_pelo_codigo(codigo, lista):
        instancia = None

        for i in lista:
            if codigo == i.codigo:
                instancia = i
                break

        return instancia

    def verificar_codigo(self, codigo):
        gatilho = False

        for livro in self.livros:
            if codigo == livro.codigo:
                gatilho = True
                break

        return gatilho

    def historico_cliente(self):
        cpf = input("Digite o CPF do cliente: ")
        cpf_verificado = self.verificar_cpf(cpf, self.clientes)

        if cpf_verificado:
            cliente = Livraria.retornar_instancia_pelo_cpf(cpf, self.clientes)

            historico_cliente = cliente.historico.mostrar()

            if len(historico_cliente.split("\n")) <= 2:
                print("Histórico do cliente está vazio.")
            else:
                print(historico_cliente)

        else:
            print("Cliente não encontrado!")

    def login(self):
        gatilho = False

        cpf = input("Digite seu CPF: ")
        senha = input("Digite sua senha: ")

        for bibliotecario in self.bibliotecarios:
            if cpf == bibliotecario.cpf and senha == bibliotecario.senha:
                self.historico.adicionar(
                    f"Bibliotecario {bibliotecario.nome} acessou o sistema."
                )
                gatilho = True

        return gatilho

    def cadastrar_bibliotecario(self):
        nome = input("Digite o nome: ")
        cpf = input("Digite o cpf: ")
        senha = input("Digite a senha: ")

        cpf_verificado = Livraria.verificar_cpf(cpf, self.bibliotecarios)

        if cpf_verificado:
            print("\nEste cliente já possui uma conta no sistema.")

        else:
            novo_bibliotecario = Bibliotecario(nome, cpf, senha)
            self.bibliotecarios.append(novo_bibliotecario)
            print("\nnovo cadastro adicionado!")

    def cadastrar_cliente(self):
        nome = input("Digite o nome: ")
        cpf = input("Digite o cpf: ")

        cpf_verificado = Livraria.verificar_cpf(cpf, self.clientes)

        if cpf_verificado:
            print("\nEste cliente já possui uma conta no sistema.")

        else:
            novo_cliente = Cliente(nome, cpf)
            self.clientes.append(novo_cliente)
            print("\nnovo cadastro adicionado!")

    def cadastrar_livro(self):
        codigo = Livraria.criar_numero_codigo()
        preco = self.entrada_float()
        titulo = input("Digite o titulo: ")
        autor = input("Digite o nome do autor: ")
        genero = input("Dídite o gênero: ")

        # codigo_verificado = self.verificar_codigo(codigo)

        # if codigo_verificado:
        #     print("\nEste livro já está no sistema.")

        # else:
        novo_livro = Livro(codigo, preco, titulo, autor, genero)
        self.livros.append(novo_livro)
        print("\nnovo livro adicionado!")

    def listar_bibliotecarios(self):

        print(f"\nPossui {len(self.bibliotecarios)} bibliotecarios\n")
        for bibliotecario in self.bibliotecarios:
            print(f"=" * 50)
            print(f"Nome: {bibliotecario.nome}")
            print(f"CPF: {bibliotecario.cpf}")

    def listar_clientes(self):
        if len(self.clientes) == 0:
            print("Não possui nenhum cliente no sistema.")

        else:
            print(f"Possui {len(self.clientes)} bibliotecarios\n")
            for cliente in self.clientes:
                print(f"=" * 50)
                print(f"Nome: {cliente.nome}")
                print(f"CPF: {cliente.cpf}")

    def listar_livros(self):
        if len(self.livros) == 0:
            print("Não possui nenhum livro no sistema.")
            return False

        else:
            print(f"\n Possui {len(self.livros)} livros\n")
            for livro in self.livros:
                print(f"=" * 50)
                print(f"Código: {livro.codigo}")
                print(f"Preço: {livro.preco}")
                print(f"Titulo: {livro.titulo}")
                print(f"autor: {livro.autor}")
                print(f"genero: {livro.genero}")

        return True

    def vender_livro(self):
        possui_livros = self.listar_livros()
        if possui_livros:
            codigo = input("\nDigite o código do livro para realizar a venda: ")
            cpf = input("Digite o cpf do cliente: ")

            codigo_verificado = self.verificar_codigo(codigo)
            cpf_verificado = Livraria.verificar_cpf(cpf, self.clientes)

            if codigo_verificado and cpf_verificado:
                for indice, livro in enumerate(self.livros):
                    if codigo == livro.codigo:
                        if livro.disponivel == False:
                            print("O livro está alugado no momento.")
                            break

                        livro_vendido = self.livros.pop(indice)

                        cliente = Livraria.retornar_instancia_pelo_cpf(
                            cpf, self.clientes
                        )

                        cliente.historico.adicionar(
                            f"Comprou o livro {livro_vendido.titulo}"
                        )

                        self.receitas += livro_vendido.preco
                        self.historico.adicionar(
                            f"O livro {livro_vendido.titulo} foi vendido para {cliente.nome} de CPF {cliente.cpf}."
                        )

                        print("\nVenda realizada com sucesso.")
            else:
                print("\nCódigo ou CPF invalido!")

    def mostrar_livros_alugados(self):
        if len(self.alugueis) == 0:
            print("Nenhum livro alugado no momento.")

        for cpf_cliente, codigos_livros_alugados_cliente in self.alugueis.items():
            cliente = Livraria.retornar_instancia_pelo_cpf(cpf_cliente, self.clientes)

            print(f"Cliente nome: {cliente.nome} cpf: {cliente.cpf}")
            print("Livros alugados:")
            for codigo_livro_alugado in codigos_livros_alugados_cliente:
                livro = Livraria.retornar_instancia_pelo_codigo(
                    codigo_livro_alugado, self.livros
                )
                print(f"Livro codigo: {livro.codigo} titulo: {livro.titulo}")

            print()

    def alugar_livro(self):
        possui_livros = self.listar_livros()
        if possui_livros:
            codigo = input("\nDigite o código do livro para realizar o aluguel: ")
            cpf = input("Digite o cpf do cliente: ")

            codigo_verificado = self.verificar_codigo(codigo)
            cpf_verificado = Livraria.verificar_cpf(cpf, self.clientes)

            if codigo_verificado and cpf_verificado:
                for livro in self.livros:
                    if codigo == livro.codigo:
                        if not livro.disponivel:
                            print("\nLivro não está disponível para aluguel.")
                            break

                        cliente = Livraria.retornar_instancia_pelo_cpf(
                            cpf, self.clientes
                        )

                        livro.disponivel = False
                        livro.data_aluguel = datetime.now()

                        cliente.historico.adicionar(f"Alugou o livro {livro.titulo}")

                        self.receitas += livro.preco / self.porcentagem_aluguel

                        if cliente.cpf in self._alugueis:
                            self._alugueis[cliente.cpf].append(livro.codigo)
                        else:
                            self._alugueis[cliente.cpf] = [livro.codigo]

                        self.historico.adicionar(
                            f"O livro {livro.titulo} foi alugado para {cliente.nome} de CPF {cliente.cpf}."
                        )

                        print("\nAluguel realizado com sucesso.")
                        break

                else:
                    print("\nCódigo do livro não encontrado.")
            else:
                print("\nCódigo ou CPF inválido.")
        else:
            print("\nNão há livros disponíveis para aluguel.")

    def devolver_livro(self):
        possui_livros = self.listar_livros()
        if possui_livros:
            codigo = input("\nDigite o código do livro para realizar a devolução: ")
            cpf = input("Digite o cpf do cliente: ")

            codigo_verificado = self.verificar_codigo(codigo)
            cpf_verificado = Livraria.verificar_cpf(cpf, self.clientes)

            if codigo_verificado and cpf_verificado:
                for livro in self.livros:
                    if codigo == livro.codigo:
                        if livro.disponivel == True:
                            print("O Livro não está alugado.")
                            break

                        if (
                            cpf not in self.alugueis.keys()
                            or codigo not in self.alugueis[cpf]
                        ):
                            print(f"O cliente de cpf {cpf} nâo alugou este livro.")
                            break

                        cliente = Livraria.retornar_instancia_pelo_cpf(
                            cpf, self.clientes
                        )

                        multa = self.calcular_multa(livro.data_aluguel)

                        if multa > 0:
                            print(f"\nLivro devolvido com multa de R${multa:.2f}")
                            self.receitas += multa
                        else:
                            print("\nLivro devolvido sem multa")

                        self.alugueis[cpf].remove(livro.codigo)
                        livro.disponivel = False

                        cliente.historico.adicionar(
                            f"Devolveu o livro {livro.titulo} (Multa: R${multa:.2f})"
                        )

                        self.historico.adicionar(
                            f"O livro {livro.titulo} foi devolvido pelo {cliente.nome} de CPF {cliente.cpf} (Multa: R${multa:.2f})."
                        )

                        print("\nDevolução realizada com sucesso.")
            else:
                print("\nCódigo ou CPF inválido!")
        else:
            print("\nNão há livros disponíveis para devolução.")

    def calcular_multa(self, data_aluguel):
        multa = 0

        dias_de_aluguel = (datetime.now() - data_aluguel).days

        if dias_de_aluguel > self.tempo_aluguel_dias:
            dias_a_mais = dias_de_aluguel - self.tempo_aluguel_dias
            print(
                f"O livro demorou mais de {dias_a_mais} para ser devolvido. Máximo de {self.tempo_aluguel_dias} dias."
            )

            multa = dias_a_mais * self.multa_atraso_aluguel

        return multa

    def caixa(self):
        print(f"Valor do caixa: R${self.receitas:.2f}")

    @staticmethod
    def mostrar_documentacao():
        documentacao = "Documentacao:\n"

        if issubclass(Cliente, Documentacao):
            documentacao += Cliente.documentacao() + "\n"

        if issubclass(Bibliotecario, Documentacao):
            documentacao += Bibliotecario.documentacao() + "\n"

        if issubclass(Livro, Documentacao):
            documentacao += Livro.documentacao() + "\n"

        if issubclass(Historico, Documentacao):
            documentacao += Historico.documentacao() + "\n"

        documentacao += (
            "A classe Livraria é a classe principal e utiliza as demais classes para fornecer as funcionalidades necessárias."
            + "\n"
        )
        print(documentacao)

    def menu_login(self):
        while True:
            print("=" * 20, "LOGIN", "=" * 20)
            result = self.login()
            if result:
                print("\nLogin acessado com sucesso!")
                break

            else:
                print("\nCPF ou senha estão incorretos!")

    def menu_bibliotecario(self):

        opcao = 0

        while True:

            print("=" * 20, "LIVRARIA", "=" * 20)
            print(" 1 - Cadatrar Bibliotecario")
            print(" 2 - Cadastrar Cliente")
            print(" 3 - Cadastrar Livros")
            print(" 5 - Listar Bibliotecarios")
            print(" 6 - Listar Clientes")
            print(" 7 - Listar livros")
            print(" 8 - Listar livros alugados")
            print(" 9 - Realizar Vendas")
            print("10 - Realizar Aluguel")
            print("11 - Realizar Devolução")
            print("12 - Historico do Cliente")
            print("13 - historico da livraria")
            print("14 - caixa")
            print("15 - Documentação")
            print("16 - Sair da conta")

            opcao = input("\nDigite a opção que deseja: ")

            if opcao == "1":
                self.cadastrar_bibliotecario()

            elif opcao == "2":
                self.cadastrar_cliente()

            elif opcao == "3":
                self.cadastrar_livro()

            elif opcao == "5":
                self.listar_bibliotecarios()

            elif opcao == "6":
                self.listar_clientes()

            elif opcao == "7":
                self.listar_livros()

            elif opcao == "8":
                self.mostrar_livros_alugados()

            elif opcao == "9":
                self.vender_livro()

            elif opcao == "10":
                self.alugar_livro()

            elif opcao == "11":
                self.devolver_livro()

            elif opcao == "12":
                self.historico_cliente()

            elif opcao == "13":

                print(self.historico.mostrar())
            elif opcao == "14":
                self.caixa()

            elif opcao == "15":
                Livraria.mostrar_documentacao()

            elif opcao == "16":
                break

    def menu_principal(self):
        while True:
            self.menu_login()
            self.menu_bibliotecario()

            opcao = input("1 - trocar de conta 2 - Sair")
            if opcao == "2":
                break
