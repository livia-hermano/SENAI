print ('Olá usuário! Digite os lados de um triângulo e te direi se ele é equilátero.')
def triangulo_equilatero (lado):
    if lado>0:
        if lado_um==lado_dois and lado_um==lado_tres and lado_dois==lado_tres:
            print('O triângulo é equilátero.')
        else:
            print('O triângulo não é equilátero.')
    else:
        print('Inseriu valor inválido e portanto não há como dar a informação.')

lado_um=int(input('Digite o primeiro lado:'))
lado_dois=int(input('Digite o segundo lado:'))
lado_tres=int(input('Digite o terceiro lado:'))
lado=lado_um+lado_dois+lado_tres
triangulo_equilatero(lado)

