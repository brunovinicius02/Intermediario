def detectar_bandeira(numero_cartao):
    """Detecta a bandeira do cartão com base nos primeiros dígitos (BIN)."""
    numero_cartao = numero_cartao.replace(" ", "")  # Remove espaços

    if numero_cartao.startswith("4"):
        return "Visa"
    elif numero_cartao[:2] in ["51", "52", "53", "54", "55"] or (2221 <= int(numero_cartao[:4]) <= 2720):
        return "Mastercard"
    elif numero_cartao[:2] in ["34", "37"]:
        return "American Express"
    elif numero_cartao[:3] in ["300", "301", "302", "303", "304", "305", "36", "38"]:
        return "Diners Club"
    elif numero_cartao[:4] in ["6011"] or numero_cartao[:2] in ["65"] or (644 <= int(numero_cartao[:3]) <= 649):
        return "Discover"
    elif numero_cartao[:4] in ["5067", "6363", "4389"]:  # Alguns BINs do Elo
        return "Elo"
    elif numero_cartao[:4] in ["6062"]:
        return "Hipercard"
    else:
        return "Bandeira desconhecida"

def validar_cartao(numero_cartao):
    """Valida um cartão de crédito pelo Algoritmo de Luhn."""
    numero_cartao = numero_cartao.replace(" ", "")
    
    if not numero_cartao.isdigit():
        return "Número de cartão inválido! Deve conter apenas dígitos."

    soma = 0
    num_invertido = numero_cartao[::-1]

    for i, digito in enumerate(num_invertido):
        n = int(digito)

        if i % 2 == 1:  # Dobra os números nas posições pares
            n *= 2
            if n > 9:
                n -= 9

        soma += n

    if soma % 10 == 0:
        return f"Cartão VÁLIDO ✅ ({detectar_bandeira(numero_cartao)})"
    else:
        return "Cartão INVÁLIDO ❌"

# Entrada do usuário
numero = input("Digite o número do cartão de crédito: ")
resultado = validar_cartao(numero)
print(resultado)
