from LighsOutAI.Posicao import Posicao


class Tabuleiro:
    pecas = [[]]
    tamanhoTabuleiro: int
    # TODO: converter de lista para objeto 'Posicao'
    # linha,coluna
    ultimaMudanca = [None, None]


    def __init__(self, pecas, tamanho_tabuleiro: int):
        self.pecas = pecas
        self.tamanhoTabuleiro = tamanho_tabuleiro

    def __str__(self):
        return str(self.pecas)

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

    def _mudar_valor(self, linha, coluna):
        if self.pecas[linha][coluna] == 0:
            self.pecas[linha][coluna] = 1
        elif self.pecas[linha][coluna] == 1:
            self.pecas[linha][coluna] = 0

    def getPecas(self):
        return self._pecas

    def setPecas(self, posicao, valor):
        posicao = Posicao
        self.pecas[posicao.getLinha][posicao.getColuna] = valor

    def getTamanhoTab(self):
        return self._tamanhoTab

    def getUltimoClique(self):
        return self._ultimoClique

    def setUltimoClique(self, novoClique):
        novoClique = Posicao
        self.ultimoClique.setPosicao(novoClique.getLinha(), novoClique.getColuna())       

