#2.
def leia():
    try:
        arquivo = open("teste.txt","r")
        print(arquivo.read())
    except FileNotFoundError:
        print("O arquivo não foi encontrado.")
    finally:
        print("Fim da tentativa de acesso ao arquivo.")
leia()     