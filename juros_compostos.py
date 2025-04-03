def calcular_juros_compostos(capital, taxa_juros_anual, tempo_meses, aporte=0):
    taxa_juros_mensal = (taxa_juros_anual / 100) / 12
    montante = capital

    print("\nMês   Saldo Inicial   Juros   Aporte   Saldo Final")
    
    for mes in range(1, tempo_meses + 1):
        juros = montante * taxa_juros_mensal
        montante += juros + aporte
        print(f"{mes:<5} R${montante - juros - aporte:<14.2f} R${juros:<8.2f} R${aporte:<8.2f} R${montante:<10.2f}")

    print("\nResumo:")
    print(f"Total investido: R$ {capital + (aporte * tempo_meses):.2f}")
    print(f"Total de juros ganhos: R$ {montante - (capital + (aporte * tempo_meses)):.2f}")
    print(f"Montante final: R$ {montante:.2f}")

# Entrada do usuário
capital = float(input("Digite o capital inicial: R$ "))
taxa_juros = float(input("Digite a taxa de juros anual (%): "))
tempo = int(input("Digite o tempo (em meses): "))
aporte_mensal = float(input("Digite o aporte mensal (ou 0 se não houver): R$ "))

calcular_juros_compostos(capital, taxa_juros, tempo, aporte_mensal)
