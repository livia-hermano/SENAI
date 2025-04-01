#-*- coding: UTF-8-*-
print('Me diga três valores reais e te direi se eles formam um triângulo escaleno.')
num1= float(input('Digite o primeiro valor:'))
num2= float(input('Digite o segundo valor:'))
num3= float(input('Digite o terceiro valor:'))
if num1!=num3 and num3!=num2 and num2!=num1:
    print ('Esses valores formam um triângulo escaleno.')
else:
    print('Esses valores não formam um triângulo escaleno.')
