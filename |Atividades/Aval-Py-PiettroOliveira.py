# ENTRADA
salHora = float(input("Insira o valor ganho por hora, em reais:\n"))
horasMes = int(input("\nDigite o número de horas trabalhadas no mês:\n"))

# SAÍDA

salBruto = salHora*horasMes
impostoRenda = salBruto*0.11
iNSS = salBruto*0.08
sindicato = salBruto*0.05
salLiquido = salBruto - (impostoRenda+iNSS+sindicato)

print("========================SALÁRIO MENSAL========================")
print(f"+ Salário Bruto : R$ {salBruto:.2f}")
print(f"- IR(11%) : R$ {impostoRenda:.2f}")
print(f"iNSS (8%) : R$ {iNSS:.2f}")
print(f"Sindicato (5%) : R$ {sindicato:.2f}")
print("========================VOCÊ IRÁ RECEBER==============================")
print(f"= Salário Líquido : R$ {salLiquido:.2f}")
print("========================================================================")