def calcular_financiamento(valor_emprestimo, taxa_juros_anual, meses):
    taxa_juros_mensal = (taxa_juros_anual / 100) / 12
    parcela = valor_emprestimo * (taxa_juros_mensal / (1 - (1 + taxa_juros_mensal) ** -meses))

    print("\nTabela de Amortização (Sistema Price)")
    print(f"{'Mês':<5} {'Parcela':<10} {'Juros':<10} {'Amortização':<12} {'Saldo Devedor':<15}")

    saldo_devedor = valor_emprestimo
    total_pago = 0
    total_juros = 0

    for mes in range(1, meses + 1):
        juros = saldo_devedor * taxa_juros_mensal
        amortizacao = parcela - juros
        saldo_devedor -= amortizacao

        total_pago += parcela
        total_juros += juros

        print(f"{mes:<5} R${parcela:<10.2f} R${juros:<10.2f} R${amortizacao:<12.2f} R${saldo_devedor:<15.2f}")

    print("\nResumo:")
    print(f"Total pago: R$ {total_pago:.2f}")
    print(f"Total de juros pagos: R$ {total_juros:.2f}")

# Entrada do usuário
valor = float(input("Digite o valor do empréstimo: R$ "))
juros = float(input("Digite a taxa de juros anual (%): "))
meses = int(input("Digite o número de meses: "))

calcular_financiamento(valor, juros, meses)
