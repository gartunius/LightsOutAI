import copy

from LighsOutAI.Tabuleiro import Tabuleiro
from LighsOutAI.Posicao import Posicao


class Gerente:

    def __init__(self, arquivo_tabuleiro_raiz):
        self.arquivo_tabuleiro_raiz = arquivo_tabuleiro_raiz
        self.estado_raiz: Tabuleiro
        self.estados_abertos = []
        self.estados_fechados = []

        self.main_loop()


    def main_loop(self):
        self.criar_estado_raiz()
        self.estados_abertos.append(self.estado_raiz)

        while True:
            estado = self.estados_abertos[0]

            if self._checar_estado(estado):
                self._mostrar_resultado(estado)
                break

            self._adicionar_aos_estados_abertos(self.criar_tabuleiro(estado))


    def _mostrar_resultado(self, estado: Tabuleiro):
        while True:
            try:
                estado_pai = estado.estado_pai
                if estado_pai is not None:
                    print(estado.ultimaMudanca)
                estado = estado_pai
            except AttributeError:
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

                # Se o valor do quadrado for alterado
                if estado_filho.alternar_valor_do_quadrado(linha, coluna) is not None:
                    estado_filho.ultimaMudanca = [linha, coluna]
                    estado_filho.tamanhoTab = self.tamanho_tabuleiro
                    estado_filho.estado_pai = estado_pai

                    if not self._checar_se_fechado(estado_filho):
                        estados_filhos.append(estado_filho)

        return estados_filhos


    def _checar_se_fechado(self, estado: Tabuleiro):
        for fechado in self.estados_fechados:
            for index_linha in range(self.tamanho_tabuleiro):
                for index_coluna in range(self.tamanho_tabuleiro):
                    if estado.pecas[index_linha][index_coluna] != fechado.pecas[index_linha][index_coluna]:
                        return False

        return True


    def _checar_estado(self, estado: Tabuleiro):
        for linha in estado.pecas:
            for coluna in linha:
                if coluna != 0:
                    if estado in self.estados_abertos:
                        self.estados_abertos.remove(estado)
                        self.estados_fechados.append(estado)
                    else:
                        raise Exception("o estado não esta na lista dos estados abertos")
                    return False

        return True

