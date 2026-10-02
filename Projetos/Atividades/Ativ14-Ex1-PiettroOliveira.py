# ENTRADA
pontuacao = float(input("Insira a pontuação obtida no vestibular: "))

# SAÍDA
if pontuacao < 0:
    print("Nota Inválida!")
elif pontuacao >= 600:
    print("Parabéns! Você foi aprovado(a).")
else:
    print("Infelizmente, você não atingiu a pontuação mínima.")
