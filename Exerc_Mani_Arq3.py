import csv
import os

alunos = [
    ["Nome", "Idade", "Nota"],
    ["Gabriel", 30, 5],
    ["Luis", 19, 8],
    ["Aline", 18, 10]
]
FILE_NAME = "alunos.csv"

def mostrar_menu():
    print("\n" + "="*25)
    print("   PAINEL DE CONTROLE")
    print("="*25)
    print("1 - Adicionar Aluno (Create)")
    print("2 - Listar Alunos (Read)")
    print("3 - Atualizar Nota (Update)")
    print("4 - Excluir Aluno (Delete)")
    print("5 - Sair")

def painel_controle():
    while True:
        mostrar_menu()
        try:
            opcao = int(input("\nEscolha uma opção: "))
        except ValueError:
            print("⚠ Entrada inválida! Digite um número.")
            continue

        if opcao == 1:
            nome = input("Nome: ")
            idade = input("Idade: ")
            nota = input("Nota: ")
            with open(FILE_NAME, "a", newline="") as arquivo:
                escritor = csv.writer(arquivo)
                escritor.writerow([nome, idade, nota])
            print("✅ Aluno adicionado!")

        elif opcao == 2:
            print("\n--- Lista de Alunos ---")
            if not os.path.exists(FILE_NAME):
                print("Arquivo vazio.")
                continue
            with open(FILE_NAME, "r") as arquivo:
                leitor = csv.reader(arquivo)
                for linha in leitor:
                    print(f"Nome: {linha[0]} | Idade: {linha[1]} | Nota: {linha[2]}")

        elif opcao == 3:
            # Lógica de Update: Lê tudo, altera na memória e sobrescreve o arquivo
            busca = input("Nome do aluno para atualizar a nota: ")
            rows = []
            found = False
            if os.path.exists(FILE_NAME):
                with open(FILE_NAME, "r") as arquivo:
                    leitor = csv.reader(arquivo)
                    for linha in leitor:
                        if linha[0].lower() == busca.lower():
                            linha[2] = input(f"Nova nota para {linha[0]}: ")
                            found = True
                        rows.append(linha)
                
                if found:
                    with open(FILE_NAME, "w", newline="") as arquivo:
                        escritor = csv.writer(arquivo)
                        escritor.writerows(rows)
                    print("✅ Nota atualizada!")
                else:
                    print("❌ Aluno não encontrado.")

        elif opcao == 4:
            # Lógica de Delete: Filtra a lista removendo o alvo
            busca = input("Nome do aluno para excluir: ")
            rows = []
            if os.path.exists(FILE_NAME):
                with open(FILE_NAME, "r") as arquivo:
                    leitor = csv.reader(arquivo)
                    rows = [linha for linha in leitor if linha[0].lower() != busca.lower()]
                
                with open(FILE_NAME, "w", newline="") as arquivo:
                    escritor = csv.writer(arquivo)
                    escritor.writerows(rows)
                print(f"✅ Se existia um aluno chamado '{busca}', ele foi removido.")

        elif opcao == 5:
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    painel_controle()