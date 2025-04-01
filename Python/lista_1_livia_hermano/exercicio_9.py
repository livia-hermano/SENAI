#-*- coding: UTF-8-*-
print('Digite o seu peso e a sua altura e lhe direi se seu peso está favorável.')
peso= float(input('Digite o seu peso: '))
altura= float(input('Digite a sua altura:'))
imc= peso/altura**2
if imc<20:
    print('Você está abaixo do peso.')
elif imc>20 and imc<=25:
    print('Você está com o peso normal.')
elif imc>25 and imc<=30:
    print('Você está com sobre peso.')
elif imc>30 and imc<=40:
    print('Você está obeso.')
else:
    print ('Você está obeso mórbido.')
