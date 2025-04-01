# -*- coding: UTF-8 -*-
print('Digite um número para realizar uma contagem regressiva!')
def contagem(num):
    for i in range (num,0,-1):
        print(i)
    print('Feliz ano novo!')

tempo=int(input('Digite o número:'))
contagem(tempo)

