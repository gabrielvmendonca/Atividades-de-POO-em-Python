class idadeInvalidaError(Exception):
    pass

   
#3.
def processar_dado(idade):
    if idade < 0:
        raise idadeInvalidaError("Digite uma Idade correta. ")
    elif idade >= 18:
        print("Maior de idade.")
    else:
        print("Menor de idade.")
try:
    processar_dado(int(input("Digite sua Idade: ")))
except idadeInvalidaError as e:
    print(f"Erro:{e}")
