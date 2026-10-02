# ENTRADA
valor = float(input("Insira o valor da conta: "))
avaliacao = str(input("Qual a avaliação do serviço?: "))

# SAÍDA
avaliacao_lower = avaliacao.lower()

print("")
if avaliacao_lower == ("bom"):
    valor_final = valor*1.1
    print(f"Valor total: R${valor_final:.2f}")
elif avaliacao_lower == ("ótimo"):
    valor_final = valor*1.15
    print(f"Valor total: R${valor_final:.2f}")
else:
    valor_final = valor
    print(f"Valor total: R${valor_final:.2f}")