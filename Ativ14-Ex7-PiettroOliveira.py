# ENTRADA
num = int(input("Insira um número de 1 a 7 correspondente ao dia da semana\n"))

# SAÍDA
print("\n")

if num == 1:
    print("Segunda-feira")
    print("Dia útil")
elif num == 2:
    print("Terça-feira")
    print("Dia útil")
elif num == 3:
    print("Quarta-feira")
    print("Dia útil")
elif num == 4:
    print("Quinta-feira")
    print("Dia útil")
elif num == 5:
    print("Sexta-feira")
    print("Dia útil")
elif num == 6:
    print("Sábado")
    print("Final de semana")
elif num == 7:
    print("Domingo")
    print("Final de semana")
else:
    print("Número inválido!")