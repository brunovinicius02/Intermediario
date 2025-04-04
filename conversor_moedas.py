import requests

# Dicionário com os códigos das moedas e seus nomes
MOEDAS_DISPONIVEIS = {
    "USD": "Dólar Americano",
    "EUR": "Euro",
    "BRL": "Real Brasileiro",
    "GBP": "Libra Esterlina",
    "JPY": "Iene Japonês",
    "CAD": "Dólar Canadense",
    "AUD": "Dólar Australiano",
    "CHF": "Franco Suíço",
    "CNY": "Yuan Chinês",
    "ARS": "Peso Argentino"
}

def mostrar_moedas_disponiveis():
    print("\n💰 Moedas disponíveis para conversão:")
    for codigo, nome in MOEDAS_DISPONIVEIS.items():
        print(f"🔹 {codigo} - {nome}")

def obter_taxa_de_cambio(moeda_origem, moeda_destino):
    url = f"https://api.exchangerate-api.com/v4/latest/{moeda_origem.upper()}"
    
    try:
        resposta = requests.get(url)
        dados = resposta.json()

        if moeda_destino.upper() in dados["rates"]:
            return dados["rates"][moeda_destino.upper()]
        else:
            print("\n❌ Moeda de destino não encontrada!")
            return None
    except Exception as e:
        print("\n❌ Erro ao acessar a API:", e)
        return None

def converter_moeda(valor, moeda_origem, moeda_destino):
    taxa = obter_taxa_de_cambio(moeda_origem, moeda_destino)

    if taxa:
        valor_convertido = valor * taxa
        print(f"\n💰 {valor:.2f} {moeda_origem.upper()} ({MOEDAS_DISPONIVEIS.get(moeda_origem.upper(), 'Desconhecido')})")
        print(f"➡️  equivale a {valor_convertido:.2f} {moeda_destino.upper()} ({MOEDAS_DISPONIVEIS.get(moeda_destino.upper(), 'Desconhecido')})")
    else:
        print("\n⚠️ Conversão não realizada.")

# Mostrando opções disponíveis
mostrar_moedas_disponiveis()

# Entrada do usuário
moeda_origem = input("\nDigite a moeda de origem (código, ex: USD, EUR, BRL): ").upper()
moeda_destino = input("Digite a moeda de destino (código, ex: USD, EUR, BRL): ").upper()
valor = float(input("Digite o valor a ser convertido: "))

converter_moeda(valor, moeda_origem, moeda_destino)
