# -*- coding: UTF-8 -*-

print('Digite a altura e raio de um cilindro e direi o seu volume')
def volume():
    raio=int(input('Digite o raio aqui:'))
    altura=int(input('Digite a altura aqui:'))
    volume=3.14*(raio*raio)*altura
    return volume
print('O volume do cilindro é:', volume())
    
