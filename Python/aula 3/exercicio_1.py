# -*- coding: UTF-8 -*-


print('Para parar o programa insira o número -999')
while True:
    num=int(input('Digite um número e lhe direi o triplo dele.'))
    if num == -999:
        break
    v=num*3
    print(v)
