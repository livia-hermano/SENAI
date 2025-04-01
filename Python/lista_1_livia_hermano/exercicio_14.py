#-*- coding: UTF-8-*-
print ('Me diga o valor de um produto e te direi o valor de venda para o produto.')
valor= float(input('Coloque o valor do produto aqui:'))
if valor<20:
 um_novo_valor= valor+valor*45/100
 print('O valor de venda é',um_novo_valor)
else:
    outro_novo_valor= valor+valor*30/100
    print ('O valor da venda é', outro_novo_valor)
