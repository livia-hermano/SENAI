# -*- coding: UTF-8 -*-

x=1
soma=0
while True:
    n=int(input('Digite valores e lhe direi a média entre eles. Para parar a entrada de valores e fazer a média, digite um número negativo.'))
    if n < 0:
        break
    soma_1=soma+n
    quant=x+1
    media= soma/quant
    print('Média: %5.2f' % media)
