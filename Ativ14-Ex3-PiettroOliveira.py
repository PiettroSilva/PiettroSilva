# ENTRADA
senha = str(input("Digite a senha a ser analisada: "))

# SAÍDA
print("")
if len(senha) > 8:
    print("Senha forte por tamanho!")
else:
    print("Senha fraca por tamanho...")