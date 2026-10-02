# ENTRADA
valorCompra = float(input("Digite o valor da compra: "))

# SAÍDA
if valorCompra > 150:
    valorDesconto = valorCompra*0.85
    print(valorDesconto)
else:
    print(valorCompra)