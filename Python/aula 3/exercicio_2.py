# -*- coding: UTF-8 -*-

x=0
print('Digite valores positivos e direi quantos valores foram digitados:')
while True:
    v=int(input('Digite um número:'))
    if v<0:
        break
    else:
        x+=1
    print(x)

