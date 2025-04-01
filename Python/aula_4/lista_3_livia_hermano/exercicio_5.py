# -*- coding: UTF-8 -*

print('Digite um número e direi se ele é primo.')

def primo(num):
    cont=0
    for i in range (1,num):
        if num%i==0:
            cont+=1
    if cont==1:
        return print(num,'é primo.')
    else:
        return print(num,'não é primo.')
    
num=int(input('Digite o número aqui:'))
(primo(num))

        
    
