#-*- coding: UTF-8-*-
print('Me diga sua idade e direi qual a faixa etária correspondente a ela')
idade= float(input('Coloque a idade aqui:'))
if idade<2:
    print('A faixa etária é: bebê.')
elif idade>=2 and idade<12:
    print('A faixa etária é: criança.')
elif idade>=12 and idade<23:
    print('A faixa etária é: adolescente.')
elif idade>=23 and idade<70:
    print('A faixa etária é: adulto.')
else:
    print('A faixa etária é: idoso.')
