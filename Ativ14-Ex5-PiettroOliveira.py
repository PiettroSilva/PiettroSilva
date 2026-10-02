# ENTRADA
consumo = int(input("Introduza o consumo médio em kWh: "))

# SAÍDA
if consumo <= 0:
    print("Nem consumiu...")
elif consumo <= 100:
    valor = 0.4*consumo
    print("A pagar: R$ ", valor)
elif consumo <= 300:
    valor = 0.65*consumo
    print("A pagar: R$ ", valor)
else:
    valor = 0.9*consumo
    print("A pagar: R$ ", valor)