def soma (a,b):
  soma = a+ b
  return soma

def subtracao (a,b):
  subtracao = a - b
  return subtracao

def multiplicacao (a,b):
  multiplicacao = a * b
  return multiplicacao

def divisao (a,b):
    if b == 0:
     print("Erro: Não pode dividir por zero.")
    else:
     divisao = a/b
     return soma,subtracao,multiplicacao,divisao 