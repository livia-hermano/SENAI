# -*- coding: UTF-8 -*-

x=0
print('Digite alguns valores e direi quantos deles são entre 100 e 200. Para parar o programa, digite 0.')
while True:
    n=int(input('Digite aqui:'))
    if n==0:
        break
    elif n> 100 and n<200:
        x+=1
        print(x)
