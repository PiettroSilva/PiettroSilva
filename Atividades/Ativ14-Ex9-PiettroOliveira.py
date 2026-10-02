# ENTRADA DE DISPONIBILIDADE DE QUARTO
disponibilidade = str(input("Informe se há quartos disponíveis: "))

# SAÍDA

diaria = 250,00

if disponibilidade.lower() == "sim":
    socio_bool = str(input("Responda com sim ou não se você é sócio do clube da fidelidade: "))
    noites = int(input("Quantas noites ficará?\n"))

    if socio_bool.lower() == "sim":
        print("Valor final: ", diaria*0,8*noites)
    if socio_bool.lower() == "não":
        print("Valor final: ", diaria*noites)
elif disponibilidade.lower() == "não":
    print("Desculpe, não há quartos disponíveis.")
else:
    print(" Responda sim ou não!!")