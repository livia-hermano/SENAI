# -*- coding: UTF-8 -*-

print('Me diga a base e altura de um triângulo e direi a sua área.')
def area():
    altura=int(input('Digite aqui a altura:'))
    base=int(input('Digite aqui a base:'))
    area= (altura*base)/2
    return area
print('A área é:',area())
