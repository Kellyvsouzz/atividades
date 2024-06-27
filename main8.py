def verificar_login():
    email = input("Digite o seu email: ")
    senha = input("Digite a sua senha: ")

    if email == "admin" and senha == "123":
        print("Usuário logado!")
    else:
        print("Usuário ou senha incorretos.")

verificar_login()
