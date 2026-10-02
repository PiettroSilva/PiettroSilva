# ENTRADA
nome = input("Digite seu nome: ")
valorHora = float(input("Valor recebido por hora: "))
horasMes = int(input("Horas trabalhadas no mês: "))

# SAÍDA
salarioTotal = valorHora*horasMes

print("\n=================================\n")

print(f"Seu salário total: R${salarioTotal:.2f}")