# ENTRADA
cor = input("Cor do semáforo:\n")

#   PERGUNTA ADICIONAL CASO SINAL VERDE
if cor.lower() == "verde":
    pedestre_presente = input("Pedestre presente (sim ou não):\n")

# SAÍDA

print("")
if cor.lower() == "verde" and (pedestre_presente.lower() == "não" or pedestre_presente.lower() == "nao"):
    print("Siga em frente.")

elif cor.lower() == "verde" and pedestre_presente.lower() == "sim":
    print("Atenção!\n  Pedestre na faixa - reduza a velocidade.")

elif cor.lower() == "amarelo":
    print("Atenção!\n   Prepare-se para parar.")

elif cor.lower() == "vermelho":
    print("Pare!\n  Aguarde o sinal abrir.")

else:
    print("Sinal com defeito!\n     Proceda com cautela.")