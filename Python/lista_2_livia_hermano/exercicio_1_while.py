# -*- coding: UTF-8 -*-

x=0
soma=0
print('Digite números e direi a média desses números.Para parar o programa digite um número negativo.')
while True:
    n=int(input('Digite um número:'))
    if n>=0:
        x+=1
        soma+=n
    else:
        break
    media=soma/x
    print ('A média é:', media)
