# ENTRADA
indUV = int(input("Introduza o índice UV abaixo:\n"))

# SAÍDA
print("\nRisco de exposição solar:")

if indUV < 3:
    print(" Baixo - sem proteção necessária.")
elif indUV <= 5:
    print(" Moderado - use protetor FPS 30.")
elif indUV <= 7:
    print(" Alto - use protetor FPS 50 e óculos.")
elif indUV <= 10:
    print(" Muito alto - evite exposição entre 10h e 16h.")
else:
    print(" Extremo - não saia ao sol!")