lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
   
    if lado1 == lado2 == lado3:
        print("É um triângulo Equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("É um triângulo Isósceles.")
    else:
        print("É um triângulo Escaleno.")
else:
    print("Os lados informados não formam um triângulo.")