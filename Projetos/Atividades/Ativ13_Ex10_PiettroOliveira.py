# ENTRADA NOME E SENHA
tentativas = int(3)
while tentativas > 0:
    nome = str(input("Nome do usuário: "))
    senha = str(input("Senha: "))

    # SAÍDA
    if nome == "admin":
        if senha == "1234":
            print(" > Acesso liberado. Bem-vindo, admin!")
        else:
            print(" > Senha incorreta.")
            tentativas -=1
            print("Tentativas restantes: ", tentativas, "\n")
    else:
        print(" > Usuário não encontrado.")