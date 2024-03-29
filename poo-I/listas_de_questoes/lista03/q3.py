class Elevador:
    def __init__(self) -> None:
        self._andar_atual = 0
        self._total_andares_predio = 0
        self._capacidade_elevador = 0
        self._quantidade_pessoas = 0

    @property
    def andar_atual(self):
        return self._andar_atual

    @andar_atual.setter
    def andar_atual(self, andar_atual):
        self._andar_atual = andar_atual

    @property
    def total_andares_predio(self):
        return self._total_andares_predio

    @total_andares_predio.setter
    def total_andares_predio(self, total_andares_predio):
        self._total_andares_predio = total_andares_predio

    @property
    def capacidade_elevador(self):
        return self._capacidade_elevador

    @capacidade_elevador.setter
    def capacidade_elevador(self, capacidade_elevador):
        self._capacidade_elevador = capacidade_elevador

    @property
    def quantidade_pessoas(self):
        return self._quantidade_pessoas

    @quantidade_pessoas.setter
    def quantidade_pessoas(self, quantidade_pessoas):
        self._quantidade_pessoas = quantidade_pessoas

    def inicializar(self, capacidade_elevador, total_andares_predio):
        self._andar_atual = 0
        self._quantidade_pessoas = 0
        self._capacidade_elevador = capacidade_elevador
        self._total_andares_predio = total_andares_predio

    def entrar(self):
        if self._quantidade_pessoas == self._capacidade_elevador:
            print("\nCapacidade do elevador chegou no máximo.\n")

        else:
            self._quantidade_pessoas += 1

    def sair(self):
        if self._quantidade_pessoas == 0:
            print("\nNão é possivel remover, pois não existe ninguém no elevador.\n")

        else:
            self._quantidade_pessoas -= 1

    def subir(self):
        if self._andar_atual == self._total_andares_predio:
            print("\nNão é possivel subir, você está no ultimo andar.\n")

        else:
            self._andar_atual += 1

    def descer(self):
        if self._andar_atual == 0:
            print("\nNão é possivel descer, você está no térreo.\n")

        else:
            self._andar_atual -= 1

    def mostrar_elevador(self):
        print("Elevador")
        print("Andar atual: ", self._andar_atual)
        print("Quantidade de pessoas: ", self._quantidade_pessoas)

    def menu(self):
        opcao = -1

        while opcao != 6:
            self.mostrar_elevador()

            print("1 - Inicializar")
            print("2 - Entrar")
            print("3 - Sair")
            print("4 - Subir")
            print("5 - Descer")
            print("6 - Sair")

            opcao = int(input("\nInsira uma opção: "))
            if opcao == 1:
                capacidade_elevador = int(input("Capacidade do elevador: "))
                total_andares_predio = int(input("Total de andares do predio: "))

                self.inicializar(capacidade_elevador, total_andares_predio)

            elif opcao == 2:
                self.entrar()

            elif opcao == 3:
                self.sair()

            elif opcao == 4:
                self.subir()

            elif opcao == 5:
                self.descer()

            elif opcao != 6:
                print("Opção inválida!\n")


if __name__ == "__main__":
    elevador = Elevador()
    elevador.menu()
