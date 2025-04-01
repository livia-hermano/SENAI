#-*- coding: UTF-8-*-
print('Me diga três valores reais e te direi se ele forma um triângulo e qual seria ele.')
num1= float(input('Digite o primeiro valor:'))
num2= float(input('Digite o segundo valor:'))
num3= float(input('Digite o terceiro valor:'))
if num3>num1+num2 or num1>num2+num3 or num2>num1+num3:
    print('Esses valores não podem formar um triângulo')

elif  num1==num3 or num3==num2 or num2==num1:
    print ('Esses valores formam um triângulo equilátero.')
elif  num1!=num3 or num3!=num2 or num2!=num1:
    print ('|Esses valores formam um triângulo escaleno.')
else:
    print ('Esses valores forma um triânugulo isósceles.')
