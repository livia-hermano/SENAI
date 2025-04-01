# -*- coding: UTF-8 -*

print('Digite a temperatura atual e transformarei em Celsius ou Fahrenheit(Digite C para Celsius, e F para Fahrenheit).')

def conversao():
    temp=float(input('Digite aqui a temperatura:'))
    cf=input('C para F, ou F para C?:')
    
    if cf == 'C para F' or 'c para f' or 'C para f' or 'c para F':
        conta=temp*9/5+32
        print('A converção ficou:', conta)
    elif cf == 'F para C' or 'f para c' or 'F para c' or 'f para C':
        conta_= temp*1,8+32
        print('A converção ficou:', conta_)
        
conversao()
        
    
    
