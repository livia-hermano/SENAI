# -*- coding: UTF-8 -*-

num= int(input('Digite um número e direi os seus possíveis divisores:'))

for i in range (1,num +1):
    if num % i==0:
        print ('Os possíveis divisores são:',i)
