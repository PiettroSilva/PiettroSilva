# ENTRADA
peso = float(input("Informe o peso do produto, em kg, para ser calculado o frete: "))

# SAÍDA
print ("\n_________________________________________")

if peso <= 1:
    print("Frete: R$ 10,00")
elif peso <=5:
    print("Frete: R$ 20,00")
elif peso <=10:
    print("Frete: R$ 35,00")
else:
    print("Frete: R$ 60,00")