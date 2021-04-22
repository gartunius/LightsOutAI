from Tabuleiro import Tabuleiro

class Gerente :
    def __init__(self, arquivo_tabuleiro_raiz) :
        self.arquivo_tabuleiro_raiz = arquivo_tabuleiro_raiz
        self.estados_abertos = []
        self.estados_fechados = []

    def _ler_arquivo(self):
        with open(self.arquivo_tabuleiro_raiz) as arquivo :
            arquivo.readline()
            conteudo_arquivo = []
            for linha in arquivo.readlines():
                conteudo_arquivo.append([caractere for caractere in linha if caractere.strip() != ''])

        return conteudo_arquivo

    def criar_tabuleiro(self):
        pass

    def gerar_novos_tabuleiros(self):
        pass

    def checar_novo_tabuleiro(self):
        pass

