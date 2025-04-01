#-*- coding: UTF-8-*-
print ('Me diga dois números e irei somar eles.Caso o resultado da soma seja maior que 20, irei somar com mais 8. Caso seja menor ou igual a 20, irei subtrair com menos 5.')
valor1= float (input('Digite o primeiro número:'))
valor2=float(input('Digite o segundo número:'))
soma=valor1+valor2
if soma > 20:
    resultado1= soma+8
    print('O resultado foi maior que 20, então somei com mais 8 e ficou:',resultado1)
    
elif soma <= 20:
    resultado2= soma-5
    print('O resultado foi menor ou igual a 20, então subtrai 5 e ficou:', resultado2)
        
