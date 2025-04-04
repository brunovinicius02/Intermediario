import os

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        self.historico = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.append(f"Depósito: +R$ {valor:.2f}")
            print(f"\n✅ Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("\n❌ Valor inválido para depósito.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.historico.append(f"Saque: -R$ {valor:.2f}")
            print(f"\n✅ Saque de R$ {valor:.2f} realizado com sucesso!")
        elif valor > self.saldo:
            print("\n❌ Saldo insuficiente!")
        else:
            print("\n❌ Valor inválido para saque.")

    def ver_saldo(self):
        print(f"\n💰 Saldo atual: R$ {self.saldo:.2f}")

    def ver_extrato(self):
        print("\n📜 Extrato da Conta:")
        if not self.historico:
            print("Nenhuma transação realizada.")
        else:
            for transacao in self.historico:
                print(transacao)
        print(f"💰 Saldo atual: R$ {self.saldo:.2f}")

def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")

# Criando a conta
titular = input("Digite o nome do titular da conta: ")
conta = ContaBancaria(titular)

while True:
    print("\n==== Menu Banco ====")
    print("1️⃣  Depositar")
    print("2️⃣  Sacar")
    print("3️⃣  Ver Saldo")
    print("4️⃣  Ver Extrato")
    print("5️⃣  Sair")

    opcao = input("Escolha uma opção: ")
    limpar_terminal()

    if opcao == "1":
        valor = float(input("Digite o valor do depósito: R$ "))
        conta.depositar(valor)
    elif opcao == "2":
        valor = float(input("Digite o valor do saque: R$ "))
        conta.sacar(valor)
    elif opcao == "3":
        conta.ver_saldo()
    elif opcao == "4":
        conta.ver_extrato()
    elif opcao == "5":
        print("\n🏦 Obrigado por usar o Banco Simulado!")
        break
    else:
        print("\n❌ Opção inválida! Tente novamente.")
