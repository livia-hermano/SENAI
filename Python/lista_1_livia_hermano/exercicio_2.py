#-*- coding: UTF-8-*-
import math
print ('Me diga um número. Se ele for positivo ou igual a 0 lhe direi sua raiz quadrada, mas se ele for negativo lhe direi o quadrado do número.')
num= float(input('Digite o número aqui: '))
if num>=0:
    r=math.sqrt (num)
    print ('O seu número foi positivo ou igual a 0, então sua raiz quadrada ficou:%.2f '%r)
else: 
    q= num**2
    print ('O seu número foi negativo, então o quadrado do número ficou: %.2f '%q)
