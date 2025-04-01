#-*- coding: UTF-8-*-
print ('Me diga quantas horas você trabalha e lhe direi o seu salário líquido.')
horas= float(input('Digite as horas trabalhadas aqui:'))
sal= horas*19.50

if sal>1500.00:
    novo_sal= sal - sal *10/100
    print ('O seu salário  ficou: ',novo_sal)
else:
    print('O seu salário é de: ',sal)
