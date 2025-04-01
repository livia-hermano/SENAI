#-*- coding: UTF-8-*-
print ('Me diga dois números e os colocarei de forma crescente')
num1= float(input('Digite o primeiro número:'))
num2= float(input('Digite o segundo número:'))
if num1>num2:
    novo_1=num1
    novo_2=num2
    print('O primeiro número é ',novo_1, ' e o segundo número é ',novo_2, ',de forma crescente.')
else:
    novo_1=num1
    novo_2=num2
    print('O segundo número é ',novo_2, 'e o primeiro número é', novo_1,' ,de forma crescente.')
