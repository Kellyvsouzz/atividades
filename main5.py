letra = input("Digite uma letra: ")

letra = letra.lower()

if letra.isalpha() and len(letra) == 1:
   
    if letra in 'aeiou':
        print(f"A letra '{letra}' é uma vogal.")
    else:
        print(f"A letra '{letra}' é uma consoante.")
else:
    print("Por favor, digite apenas uma letra do alfabeto.")