#-*- coding: UTF-8-*-
print ('Digite o preço de sua mercadoria e o porcentual de desconto e eu direi o valor do desconto e qual será o total a pagar')
merc= float(input('Digite o preço da mercadoria: '))
desc= float(input('Digite o porcentual de desconto: '))
vd= merc*desc/100
tp= merc-vd
print('O valor de desconto é: ', vd)
print('O total a pagar será de: ',tp)
