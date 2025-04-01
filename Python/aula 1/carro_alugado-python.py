#-*- coding: UTF-8-*-
print ('Me diga a quantidade de km percorrido por um carro alugado e a quantidade de dias que ficou com o carro e e eu lhe direi o total a pagar')
km= float(input('Digite a quantidade de km: '))
d= int(input('Digite a quantidade de dias: '))
vd= d*60
vkm= km*0.15
total= vd+vkm
print('O total a pagar será: R$',total)
