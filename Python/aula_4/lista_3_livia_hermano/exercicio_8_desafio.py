# -*- coding: UTF-8 -*-

print('Digite um número e direi quantos dígitos ele tem.')
num=int(input('Digite o número aqui:'))
def digitos(num):
    cont=0
    while num>=1:
        num=num/10
        cont+=1
    return cont

print(f"O seu número tem {digitos(num)} dígitos!")
