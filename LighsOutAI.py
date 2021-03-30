from sys import argv
from os import path


def main() :
    try :
        csv_file = argv[1]

        if path.isfile(csv_file) :
            print("Arquivo existe")

        else :
            print("Arquivo não existe, favor verificar o diretório.")

    except IndexError :
        print("Favor passar como primeiro parâmetro o diretório do csv com a configuração inicial do tabuleiro.")


if __name__ == "__main__" :
    main()

