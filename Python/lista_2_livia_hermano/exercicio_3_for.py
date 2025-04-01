# -*- coding: UTF-8 -*-

num=int(input('Digite um número e direi o seu fatorial:'))
fatorial=1

for i in range (1, num +1):
    fatorial=i*fatorial
print('O fatorial é:', fatorial)
