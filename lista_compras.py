import json
import os

FILE_NAME = "lista_compras.json"

# Detecta o sistema operacional para limpar o terminal corretamente
def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")

# Carrega a lista de compras do arquivo (se existir)
def carregar_lista():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Salva a lista de compras no arquivo
def salvar_lista(lista):
    with open(FILE_NAME, "w") as f:
        json.dump(lista, f, indent=4)

# Exibe o menu de opções
def menu():
    print("\n1. Adicionar item")
    print("2. Remover item")
    print("3. Ver lista")
    print("4. Sair")

# Programa principal
lista_compras = carregar_lista()

while True:
    limpar_terminal()
    menu()
    escolha = input("\nEscolha uma opção: ")

    limpar_terminal()  # Limpa a tela antes de executar a opção

    if escolha == "1":
        item = input("Digite o nome do item: ")
        lista_compras.append(item)
        salvar_lista(lista_compras)
        print(f"'{item}' foi adicionado à lista!")

    elif escolha == "2":
        item = input("Digite o nome do item para remover: ")
        if item in lista_compras:
            lista_compras.remove(item)
            salvar_lista(lista_compras)
            print(f"'{item}' foi removido da lista!")
        else:
            print("Item não encontrado.")

    elif escolha == "3":
        print("\nLista de Compras:")
        for i, item in enumerate(lista_compras, start=1):
            print(f"{i}. {item}")
        input("\nPressione Enter para continuar...")  # Aguarda antes de limpar a tela

    elif escolha == "4":
        print("Saindo...")
        break
