# ENTRADA
temp = float(input("Insira a temperatura ambiente: "))

# SAÍDA
if temp < 0:
    print("Congelamento! Temperatura crítica.")
else:
    if temp < 15:
        print("Frio intenso no laboratório.")
    else:
        if temp < 25:
            print("Temperatura agradável.")
        else:
            print("Temperatura alta! Ligar refrigeração.")