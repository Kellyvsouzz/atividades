nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

# Calcula a média das notas
media = (nota1 + nota2 + nota3 + nota4) / 4

# Determina o status do aluno com base na média
if media >= 70:
    print(f"Aluno aprovado com média {media:.2f}.")
elif media >= 50:
    print(f"Aluno em recuperação com média {media:.2f}.")
else:
    print(f"Aluno reprovado com média {media:.2f}.")