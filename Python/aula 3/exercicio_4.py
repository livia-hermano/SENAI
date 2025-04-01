# -*- coding: UTF-8 -*-

x=0
soma=0
print('Digite valores e lhe direi a média entre eles. Para parar, digite um número negativo.')
while True:
    n=int(input('Digite um número:'))
    if n >= 0:
        x +=1
        soma+=n
    else:
         break
    media= soma/x
    print('Média:',media)
