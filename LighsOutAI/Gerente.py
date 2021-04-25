import copy

from LighsOutAI.Tabuleiro import Tabuleiro


class Gerente:
    def __init__(self, arquivo_tabuleiro_raiz) :
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
                break
            self._adicionar_aos_estados_abertos(self.criar_tabuleiro(estado))

    def _adicionar_aos_estados_abertos(self, estados):
        for estado in estados:
            self.estados_abertos.append(estado)

    def criar_estado_raiz(self):
        with open(self.arquivo_tabuleiro_raiz) as arquivo :
            tamanho_tabuleiro = int(arquivo.readline())
            conteudo_arquivo = []
            for linha in arquivo.readlines():
                conteudo_arquivo.append([int(caractere) for caractere in linha if caractere.strip() != ''])

            self.estado_raiz = Tabuleiro(conteudo_arquivo, tamanho_tabuleiro)

    def criar_tabuleiro(self, estado: Tabuleiro):
        estados_filhos = []
        for linha in range(estado.tamanhoTabuleiro):
            for coluna in range(estado.tamanhoTabuleiro):
                novo_estado = copy.deepcopy(estado)
                checagem_modicicacao = novo_estado.alternar_valor_do_quadrado(linha, coluna)
                if checagem_modicicacao is not None and novo_estado not in self.estados_fechados:
                    estados_filhos.append(novo_estado)

        return estados_filhos

    def _checar_estado(self, estado: Tabuleiro):
        print(estado)
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