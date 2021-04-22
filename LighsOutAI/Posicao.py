class Posicao:
    linha = int
    coluna = int
    def __init__(self, linha, coluna):
        self.linha = linha
        self.coluna = coluna

    @property
    def getLinha(self):
        return self._linha
    
    @property
    def getColuna(self):
        return self._coluna

    @linha.setter
    def setLinha(self, novaLinha):
        self._linha = novaLinha
    
    @coluna.setter
    def setColuna(self, novaColuna):
        self._coluna = novaColuna

    def setPosicao(self, novaLinha, novaColuna):
        self.setLinha(novaLinha)
        self.setColuna(novaColuna)