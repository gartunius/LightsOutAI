import copy

from LighsOutAI.Posicao import Posicao
from LighsOutAI.Tabuleiro import Tabuleiro


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

        try:
            while True:
                for estado in self.estados_abertos:
                    self._adicionar_aos_estados_abertos(self.criar_tabuleiro(estado))

        except KeyboardInterrupt:
            print(f"Encerrando\nestados abertos: {self.estados_abertos}\nestados fechados: {self.estados_fechados}")

    def _adicionar_aos_estados_abertos(self, estados):
        for estado in estados:
            self.estados_abertos.append(estado)

    def criar_estado_raiz(self):
        with open(self.arquivo_tabuleiro_raiz) as arquivo:
            tamanho_tabuleiro = int(arquivo.readline())
            conteudo_arquivo = []
            for linha in arquivo.readlines():
                conteudo_arquivo.append([int(caractere) for caractere in linha if caractere.strip() != ''])

            self.estado_raiz = Tabuleiro(conteudo_arquivo)

    def criar_tabuleiro(self, estado: Tabuleiro):
        estados_filhos = []
        for linha in range(estado.tamanhoTab):
            for coluna in range(estado.tamanhoTab):
                novo_estado = copy.deepcopy(estado)
                posicao = Posicao(linha, coluna)
                novo_estado.alternar_valor_do_quadrado(posicao)
                # self._return_pretty_pecas(novo_estado.pecas)
                estados_filhos.append(novo_estado)

        return estados_filhos

    def _return_pretty_pecas(self, pecas):
        for linha in pecas:
            print(linha)

    def _checar_tabuleiro(self, tabuleiro: Tabuleiro):
        for linha in tabuleiro.pecas:
            for coluna in linha:
                if coluna != 0:
                    return False
        return True