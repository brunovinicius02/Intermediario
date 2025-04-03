import csv

FILE_NAME = "contatos.csv"

# Carrega a agenda do arquivo (se existir)
def carregar_contatos():
    try:
        with open(FILE_NAME, "r") as f:
            reader = csv.reader(f)
            return list(reader)
    except FileNotFoundError:
        return []

# Salva a agenda no arquivo
def salvar_contatos(contatos):
    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(contatos)

# Exibe o menu de opções
def menu():
    print("\n1. Adicionar contato")
    print("2. Remover contato")
    print("3. Buscar contato")
    print("4. Ver todos os contatos")
    print("5. Sair")

# Programa principal
agenda = carregar_contatos()

while True:
    menu()
    escolha = input("\nEscolha uma opção: ")

    if escolha == "1":
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("E-mail: ")
        agenda.append([nome, telefone, email])
        salvar_contatos(agenda)
        print(f"Contato '{nome}' adicionado!")

    elif escolha == "2":
        nome = input("Digite o nome do contato para remover: ")
        nova_agenda = [contato for contato in agenda if contato[0] != nome]
        if len(nova_agenda) != len(agenda):
            agenda = nova_agenda
            salvar_contatos(agenda)
            print(f"Contato '{nome}' removido!")
        else:
            print("Contato não encontrado.")

    elif escolha == "3":
        nome = input("Digite o nome do contato para buscar: ")
        encontrados = [contato for contato in agenda if nome.lower() in contato[0].lower()]
        if encontrados:
            for contato in encontrados:
                print(f"Nome: {contato[0]}, Telefone: {contato[1]}, E-mail: {contato[2]}")
        else:
            print("Contato não encontrado.")

    elif escolha == "4":
        print("\nLista de Contatos:")
        for contato in agenda:
            print(f"Nome: {contato[0]}, Telefone: {contato[1]}, E-mail: {contato[2]}")

    elif escolha == "5":
        print("Saindo...")
        break

    else:
        print("Opção inválida, tente novamente.")
