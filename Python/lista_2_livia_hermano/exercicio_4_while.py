# -*- coding: UTF-8 -*-


print('Digite alguns números e direi a soma dos números pares e a soma dos números impares que forem colocados. Para parar o programa, digite um número maior que 1000.')

par=0
impar=0

while True:
    n=int(input('Digite o número aqui:'))
    if n>1000:
        break
    elif n %2==0:
        par+=n
    elif n%2!=0:
        impar +=n
print('A soma dos números pares é:', par)
print('A soma dos números impares é:', impar)
        
        
        
