
# -*- coding: UTF-8 -*-

print('Digite números e direi qual o maior e o menor número entre eles. Quando tiver finalizado, digite um número negativo para obter o resultado.')
n=float(input('Digite um número:'))

maior=n
menor=n
while True:
    n=float(input('Digite um número:'))
    if n<0:
        break
    elif n> maior:
        maior=n
    elif n<menor:
        menor=n
print('O maior número é: ', maior)
print('O menor número é:', menor)
  
