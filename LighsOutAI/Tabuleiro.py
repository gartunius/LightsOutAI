from LighsOutAI.Posicao import Posicao


class Tabuleiro:
    pecas = [[]]
    tamanhoTab: int
    posicao: Posicao
    ultimoClique = Posicao(None, None)
    filhos: list = []
    ultimaMudanca = [None, None]

    def __init__(self, pecas):
        self.pecas = pecas

    def __str__(self):
        res = ""
        for i in range(self.tamanhoTab):
            for j in range(self.tamanhoTab):
                res = res + str(self.pecas[i][j]) + " "
            res = res + "\n"
        return res

    def addFilhos(self, filho):
        self.filhos.append(filho)

    def getFilhos(self):
        return self.filhos

    def alternar_valor_do_quadrado(self, linha: int, coluna: int):
        if linha == self.ultimaMudanca[0] and coluna == self.ultimaMudanca[1]:
            return None

        self.ultimaMudanca[0] = linha
        self.ultimaMudanca[1] = coluna

        self._mudar_valor(linha, coluna)
        try:
            self._mudar_valor(linha + 1, coluna)
        except IndexError:
            pass
        if linha >= 1:
            self._mudar_valor(linha - 1, coluna)
        try:
            self._mudar_valor(linha, coluna + 1)
        except IndexError:
            pass
        if coluna >= 1:
            self._mudar_valor(linha, coluna - 1)

        return not None

    def setTamanhoTab(self, valor):
        self.tamanhoTab = valor

    def _mudar_valor(self, linha, coluna):
        if self.pecas[linha][coluna] == 0:
            self.pecas[linha][coluna] = 1
        elif self.pecas[linha][coluna] == 1:
            self.pecas[linha][coluna] = 0

    def getUltimoClique(self):
        return self.ultimoClique

    def setUltimoClique(self, novoClique: Posicao):
        self.ultimoClique.setPosicao(novoClique.getLinha, novoClique.getColuna)

