# ENTRADA DE VARIÁVEIS
peso = float(input("Seu peso, em quilos: "))
altura = float(input("Sua altura, em metros: "))

# SAÍDA
imc = peso/(altura*2)

if imc < 18.5:
    print("Abaixo do peso normal.")
elif imc < 25.0:
    print("Peso normal.")
elif imc < 30.0:
    print("Sobrepeso.")
else:
    print("Obesidade.")