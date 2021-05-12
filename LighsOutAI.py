from sys import argv
from os import path
from LighsOutAI.Gerente import Gerente


def main():
    csv_file = argv[1]
    if path.isfile(csv_file):
        Gerente(csv_file, argv[2])

    else:
        print("Arquivo não existe, favor verificar o diretório.")


if __name__ == "__main__":
    main()
