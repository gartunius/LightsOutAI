from sys import argv
from os import path
from LighsOutAI.Gerente import Gerente


def main() :
    try :
        csv_file = argv[1]

        if path.isfile(csv_file) :
            gerente = Gerente(csv_file)

        else :
            print("Arquivo não existe, favor verificar o diretório.")

    except IndexError :
        print("Favor passar como primeiro parâmetro o diretório do csv com a configuração inicial do tabuleiro.")


if __name__ == "__main__" :
    main()

