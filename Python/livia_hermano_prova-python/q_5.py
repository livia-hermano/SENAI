print ('Olá usuário! Me diga o valor de sua compra e lhe direi o desconto que receberá e quanto ficará a compra com este desconto.Para compras com valor maior que R$100 se dará um desconto de 10%; para compras com valores entre R$50 e R$100 se dará um desconto de 5%; para outros valores não se dará desconto.')
valor= float(input('Digite aqui: '))
if valor>100:
    total_de_dez=valor*(10/100)
    diferenca=valor-total_de_dez
    print ('O seu desconto é de 10% e sua compra ficará no valor de:', diferenca)
elif valor>=50 and valor<=100:
    total_de_cinco= valor*(5/100)
    diferir=valor-total_de_cinco
    print('O seu desconto é de 5% e ficará no valor de: ',diferir)
else:
    print('O valor não receberá desconto.')

