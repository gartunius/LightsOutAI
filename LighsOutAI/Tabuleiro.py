from LighsOutAI.Posicao import Posicao


class Tabuleiro:
    pecas = [[]]
    tamanhoTab: int = 3
    ultimoClique = Posicao(None, None)
    filhos = []

    def __init__(self, pecas):
        self.pecas = pecas

    def addFilhos(self, filho):
        self.filhos.append(filho)

    def getFilhos(self):
        return self.filhos

    def alternar_valor_do_quadrado(self, posicao: Posicao):
        linha = posicao.getLinha
        coluna = posicao.getColuna
        ultimo_clique = self.getUltimoClique
        if linha == ultimo_clique.getLinha and coluna == ultimo_clique.getColuna:
            return None

        self._mudar_valor(posicao)
        try:
            posicao.setLinha(linha+1)
            self._mudar_valor(posicao)
        except IndexError:
            pass
        if linha >= 1:
            posicao.setLinha(linha-1)
            self._mudar_valor(posicao)
        try:
            posicao.setColuna(coluna+1)
            self._mudar_valor(posicao)
        except IndexError:
            pass
        if coluna >= 1:
            posicao.setColuna(coluna - 1)
            self._mudar_valor(posicao)

    def _mudar_valor(self, posicao: Posicao):
        linha = posicao.getLinha
        coluna = posicao.getColuna
        if self.pecas[linha][coluna] == 0:
            self.pecas[linha][coluna] = 1
        elif self.pecas[linha][coluna] == 1:
            self.pecas[linha][coluna] = 0

    @property
    def getUltimoClique(self):
        return self.ultimoClique

    # @ultimoClique.setter
    def setUltimoClique(self, novoClique):
        novoClique: Posicao
        self.ultimoClique.setPosicao(novoClique.getLinha(), novoClique.getColuna())

    def __str__(self):
        res = ""
        for i in range(self.tamanhoTab):
            for j in range(self.tamanhoTab):
                res = res + str(self.pecas[i][j]) + " "
            res = res + "\n"
        return res
