# -*- coding: UTF-8 -*-

print('Digite dois números e qual o tipo de operação("+" para adição,"-" para subtração, "/" para divisão e "*" para a multiplicação.) que deseja realizar.')
def calcular():
    operador=input('Digite o operador que deseja realizar:')
    if operador == '+':
        print('Escolheu fazer uma conta de adição.')
        calcular=num1+num2
    elif operador=='-':
        calcular=num1-num2
    elif operador== '*':
        calcular=num1*num2
    elif operador=='/':
        calcular=num1/num2
    return print (calcular)
   
num1=int(input('Digite o primeiro valor:'))
num2=int(input('Digite o segundo valor:'))
calcular()
        
        
        
