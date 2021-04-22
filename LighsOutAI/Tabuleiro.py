from LighsOutAI.Posicao import Posicao


class Tabuleiro:
    pecas = [[]]
    tamanhoTab = int
    ultimoClique = Posicao

    def __init__ (self, pecas):
        self.pecas = pecas

    @property
    def getPecas(self):
        return self._pecas

    @pecas.setter
    def setPecas(self, posicao, valor):
        posicao = Posicao
        self.pecas[posicao.getLinha][posicao.getColuna] = valor

    @property
    def getTamanhoTab(self):
        return self._tamanhoTab

    @property
    def getUltimoClique(self):
        return self._ultimoClique

    @ultimoClique.setter
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

tabuleiro = Tabuleiro()

def inverteValores(valor):
    if valor == 0:
        valor = 1
        return valor
    elif valor == 1:
        valor = 0
        return valor
    else:
      return valor
