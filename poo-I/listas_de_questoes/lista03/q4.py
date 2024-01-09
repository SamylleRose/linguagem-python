class Televisao:
    def __init__(self) -> None:
        self._volume = 5
        self._canal = 6

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, novo_volume):
        self._volume = novo_volume

    @property
    def canal(self):
        return self._canal

    @canal.setter
    def canal(self, novo_canal):
        self._canal = novo_canal


class Controle_remoto:
    def __init__(self, televisao) -> None:
        self._televisao = televisao

    def aumentar_volume(self):
        if self._televisao.volume >= 100:
            print("\nVolume máximo atingido!\n")
        else:
            self._televisao.volume += 1
            print("\nVolume aumentado!\n")

    def diminuir_volume(self):
        if self._televisao.volume <= 0:
            print("\nVolume mínimo atingido!\n")
        else:
            self._televisao.volume -= 1
            print("\nVolume diminuido!\n")

    def aumentar_canal(self):
        if self._televisao.canal >= 30:
            print("\nSua televisão tem apenas 30 canais!\n")
        else:
            self._televisao.canal += 1
            print("\nCanal aumentado!\n")

    def diminuir_canal(self):
        if self._televisao.canal == 1:
            print("\nVocê não pode mais diminuir, pois jáestá no primeiro canal.\n")
        else:
            self._televisao.canal -= 1
            print("\nCanal diminuido!\n")

    def trocar_canal_indicado(self, canal_indicado):
        if canal_indicado > 0 and canal_indicado <= 30:
            self._televisao.canal = canal_indicado
            print("\nCanal alterado!\n")
        else:
            print("\nEsse canal não existe!\n")

    def consulta(self):
        print(
            f"\nVolume da televisão: {self._televisao.volume}\nCanal da televisão: {self._televisao.canal}\n"
        )

    def menu(self):
        opcao = -1

        while opcao != 7:
            print("1 - Aumentar volume")
            print("2 - Diminuir volume")
            print("3 - aumentar canal")
            print("4 - diminuir canal")
            print("5 - Indicar canal")
            print("6 - consultar volume e canal")
            print("7 - sair")

            opcao = int(input("Digite o código: "))

            if opcao == 1:
                self.aumentar_volume()

            elif opcao == 2:
                self.diminuir_volume()

            elif opcao == 3:
                self.aumentar_canal()

            elif opcao == 4:
                self.diminuir_canal()

            elif opcao == 5:
                canal_indicado = int(input("Qual canal deseja? "))
                self.trocar_canal_indicado(canal_indicado)

            elif opcao == 6:
                self.consulta()

            elif opcao != 7:
                print("\nOpção inválida!\n")


if __name__ == "__main__":
    televisao = Televisao()
    controle_remoto = Controle_remoto(televisao)
    controle_remoto.menu()
