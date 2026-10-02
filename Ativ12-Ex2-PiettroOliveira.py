# ENTRADA
modeloVeiculo = input("Insira o modelo do veículo: ")
distanciaPercorrida = float(input("Digite a distância percorrida, em quilômetros: "))
combustivelGasto = int(input("Digite a quantidade de combustível gasto, em litros:"))

# SAÍDA
consumoMedio = distanciaPercorrida/combustivelGasto

print("\n=====================================\n")
print("O consumo médio é: ", consumoMedio, "km/l")