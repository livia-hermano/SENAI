# -*- coding: UTF-8 -*-

soma21=0
soma50=0

print('Digite a idade de pessoas e direi quantas pessoas estão abaixo de 21 anos e o total de pessoas com mais de 50 anos. Para finalizar, digite -99.')
while True:
    idade=int(input('Digite a idade aqui:'))
    if idade == -99:
        break
    elif idade<=21 and idade<50:
        soma21 +=1
    elif idade >=50:
        soma50 +=1
print('A quantidades de pessoas com idade abaixo de 21 anos é:', soma21)
print('A quantidades de pessoas com idade acima de 50 anos é:', soma50)

