# ENTRADA
idade = int(input("Digite sua idade: "))

# SAÍDA
print("")
print("======================================")
if idade < 0:
    print("Você nem nasceu ainda")
elif idade < 12:
    print("Você participará da categoria infantil.")
elif idade < 18:
    print("Você participará da categoria juvenil.")
else:
    print("Você participará da categoria adulto.")