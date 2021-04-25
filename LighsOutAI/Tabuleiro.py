from LighsOutAI.Posicao import Posicao


class Tabuleiro:
    pecas = [[]]
    tamanhoTabuleiro: int
    # ultimoClique = Posicao
    # linha,coluna
    ultimaMudanca = [None, None]

    def __init__ (self, pecas, tamanho_tabuleiro: int):
        self.pecas = pecas
        self.tamanhoTabuleiro = tamanho_tabuleiro

    def alternar_valor_do_quadrado(self, linha: int, coluna: int):
        if linha == self.ultimaMudanca[0] and coluna == self.ultimaMudanca[1]:
            return None

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

    def _mudar_valor(self, linha, coluna):
        if self.pecas[linha][coluna] == 0:
            self.pecas[linha][coluna] = 1
        elif self.pecas[linha][coluna] == 1:
            self.pecas[linha][coluna] = 0

    @property
    def getPecas(self):
        return self._pecas

    @property
    def getTamanhoTab(self):
        return self._tamanhoTab

    @property
    def getUltimoClique(self):
        return self._ultimoClique

    # @ultimoClique.setter
    def setUltimoClique(self, novoClique):
        novoClique = Posicao
        self.ultimoClique.setPosicao(novoClique.getLinha(), novoClique.getColuna())       

    def fazerAcao(self):
        auxiliar = self.getUltimoClique()
        novaCol = auxiliar.setColuna(auxiliar.getColuna+1)
        novaLinha = auxiliar.setLinah(auxiliar.setLinha+1)
        novaPos = Posicao

        if auxiliar.getLinha == self.tamanhoTab-1 and auxiliar.getColuna != self.tamanhoTab-1:
            novaPos.setColuna(novaCol)
        else:
            novaPos.setLinha(novaLinha)

        if auxiliar.getColuna+1 == 0 or auxiliar.getColuna > self.tamanhoTab:
            self.setPecas()

#tabuleiro = Tabuleiro()
#
#def inverteValores(valor):
#    if valor == 0:
#        valor = 1
#        return valor
#    elif valor == 1:
#        valor = 0
#        return valor
#    else:
#      return valor
