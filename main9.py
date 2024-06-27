
def cadastrar_usuario():
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha (deve ter mais de 8 caracteres): ")

    if len(senha) > 8:
        print("Usuário cadastrado com sucesso!")

    else:
        print("Erro: A senha deve ter mais de 8 caracteres.")

cadastrar_usuario()
