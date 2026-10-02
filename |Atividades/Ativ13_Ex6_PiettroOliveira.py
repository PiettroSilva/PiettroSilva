# ENTRADA DA NOTA
nota = float(input("Introduza a nota do aluno: "))

# SAÍDA DO ESTADO
if 0 <= nota <= 10:
    if nota >= 9.0:
        print("Excelente!")
    elif nota >= 7.0:
        print("Aprovado(a)!")
    elif nota >= 5.0:
        print("Em recuperação...")
    else:
        print("Reprovado.")
