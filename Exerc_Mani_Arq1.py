def leia():
    try:
        arquivo = open("poema.txt","r")
        print(arquivo.read())
    except FileNotFoundError:
        print("O arquivo não foi encontrado.")
    finally:
        print("Fim da tentativa de acesso ao arquivo.")
leia()     