# TABELA DE PREÇOS
print("Tipo 1 - Moto -> R$ 2,50")
print("Tipo 2 - Carro -> R$ 5,00")
print("Tipo 3 - Caminhão -> R$ 10,00")

# ENTRADA
tipo = int(input("Forneça o tipo do seu veículo conforme a tabela acima: "))

# SAÍDA
if 1<=tipo<=3:
    if tipo == 1:
        print("Valor a ser pago: R$ 2,50.")
    elif tipo == 2:
        print("Valor a ser pago: R$ 5,00.")
    elif tipo == 3:
        print("Valor a ser pago: R$ 10,00.")
else:
    print("Tipo de veículo inválido!")