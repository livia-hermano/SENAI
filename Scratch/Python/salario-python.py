#-*- coding: UTF-8-*-
print(' Me diga o valor do seu salário e a porcentagem do aumento que receberá')
salario= float(input('Digite o salário: '))
porc= float(input('Digite a porcentagem: '))
total= salario*(porc/100)
diferenca= total+salario
print('O total de aumento do salário é: ', total)
print ('O seu novo salário é: ',diferenca)
