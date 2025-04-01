#-*- coding: UTF-8-*-
print('Digite o valor do seu salário e da prestação que deseja fazer e lhe direi se pode fazer o empréstimo ou não. Caso passe de 30% do valor do salário, você não poderá realizar')
sal= float(input('Digite o valor do seu salário:'))
prest= float(input('Digite o valor da prestação:'))
sal_porc= sal*30/100
if prest<sal_porc:
    print('Você pode realizar o empréstimo.')
else:
    print('Você não pode realizar o empréstimo.')
