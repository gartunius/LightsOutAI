import copy

from LighsOutAI.Tabuleiro import Tabuleiro


class Gerente:

    def __init__(self, arquivo_tabuleiro_raiz, log_file):
        self.arquivo_tabuleiro_raiz = arquivo_tabuleiro_raiz
        self.estado_raiz: Tabuleiro
        self.estados_abertos = []
        self.estados_fechados = []
        self.log_file = log_file

        self.main_loop()


    def main_loop(self):
        self.criar_estado_raiz()
        self.estados_abertos.append(self.estado_raiz)

        with open(self.log_file, 'w') as log_file:
            while True:
                estado = self.estados_abertos[0]
                print(f"\r[=] Running estados abertos: {len(self.estados_abertos)} / estados fechados: {len(self.estados_fechados)}", end="")

                log_file.write(f"{estado} estado_pai\n")
                if self._checar_estado(estado):
                    self._mostrar_resultado(estado)
                    break

                estados_filhos = self.criar_tabuleiro(estado)

                for estado_log in estados_filhos:
                    log_file.write(f"{estado_log}\n")

                log_file.write("\n")

                self._adicionar_aos_estados_abertos(estados_filhos)
                self._fechar_estado(estado)


    def _mostrar_resultado(self, estado: Tabuleiro):
        print("\n[linha, coluna] começando em 0")
        while True:
            estado_pai = estado.estado_pai
            if estado_pai is not None:
                print(f"{estado.ultimaMudanca}")
                estado = estado_pai
            else:
                print("===")
                break


    def _adicionar_aos_estados_abertos(self, estados):
        for estado in estados:
            self.estados_abertos.append(estado)


    def criar_estado_raiz(self):
        with open(self.arquivo_tabuleiro_raiz) as arquivo:
            self.tamanho_tabuleiro = int(arquivo.readline())
            conteudo_arquivo = []

            for linha in arquivo.readlines():
                conteudo_arquivo.append([int(caractere) for caractere in linha if caractere.strip() != ''])

            self.estado_raiz = Tabuleiro(conteudo_arquivo)
            self.estado_raiz.tamanhoTab = self.tamanho_tabuleiro


    def criar_tabuleiro(self, estado_pai: Tabuleiro):
        estados_filhos = []

        for linha in range(self.tamanho_tabuleiro):
            for coluna in range(self.tamanho_tabuleiro):
                estado_filho = copy.deepcopy(estado_pai)

                if linha != estado_pai.ultimaMudanca[0] or coluna != estado_pai.ultimaMudanca[1]:
                    estado_filho.alternar_valor_do_quadrado(linha, coluna)
                    estado_filho.estado_pai = estado_pai  # type: ignore

                    if not self._checar_se_fechado(estado_filho):
                        estados_filhos.append(estado_filho)

        return estados_filhos


    def _checar_se_fechado(self, estado: Tabuleiro):
        for estado_fechado in self.estados_fechados:
            if estado_fechado == estado:
                return True
        return False


    def _checar_estado(self, estado: Tabuleiro):
        for linha in estado.pecas:
            for coluna in linha:
                if coluna != 0:
                    return False
        return True

    def _fechar_estado(self, estado):
        if estado in self.estados_abertos:
            self.estados_abertos.remove(estado)
            self.estados_fechados.append(estado)
        else:
            raise Exception("o estado não esta na lista dos estados abertos")



