# -*- coding: UTF-8 -*-

cont=0

print('Envie o sexo de pessoas e direi quantas delas são do gênero masculino.')

quant= int(input('Quantas pessoas quer enviar:'))

for i in range (quant):
    sexo=input('Qual o sexo? (M ou m para masculino e F ou f para feminino):')
    if sexo=='M' or sexo== 'm':
        cont+=1
print('A quantidade de pessoas do gênero masculino é:',cont)
