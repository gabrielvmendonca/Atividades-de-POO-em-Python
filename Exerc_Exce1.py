#1.
try:
    resultado = 10/0
    print(resultado)
except ZeroDivisionError:
    print("Erro: Divisõa por zero não é permitido")