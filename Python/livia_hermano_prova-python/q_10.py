print('Olá usuário! Digite o valor inicial a sua compra, sua taxa de juros e número de períodos e te direi o valor final com juros compostos da sua compra.')
vi=float(input('Digite o valor inicial da sua compra:'))
i=float(input('Digite a taxa de juros por período:'))
n=float(input('Digite o número de períodos:'))
if vi<0 and i<0 and n<0:
    ('Valores inválidos foram inseridos, portanto não há como realizar o cálculo.')
else:
    vf=vi*(1+i)/n
print('O valor final da sua compra será:',vf)
