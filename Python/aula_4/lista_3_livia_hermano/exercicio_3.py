# -*- coding: UTF-8 -*-

print('Digite um número e direi sua tabuada.')

def tabuada(num):
    for i in range (1,11):
        print(num,'*', i, '=', num*i)

num=int(input('Digite o número aqui:'))
tabuada(num)

        
