# -*- coding: UTF-8 -*-
print('Digite dois valores e direi qual o maior entre eles.')
def maior_num():
    num1=int(input('Digite o primeiro valor:'))
    num2=int(input('Digite o segundo valor:'))
    if num1>num2:
        return num1
    else:
        return num2


print('O maior número é:',maior_num ())
