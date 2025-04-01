#-*- coding: UTF-8-*-
print ('Vamos descobrir o tempo perdido de vida, fumando cigarros.')
cigarros= int(input('Digite a quantidade de cigarros fumados durante um dia: '))
anos_fumados= float(input('Digite a quantidade de anos e meses que passou fumando: '))
qtd_total_cigarros= cigarros*anos_fumados*365

tempo_minutos= qtd_total_cigarros*10
totald= tempo_minutos/60/24
print('O total de dias perdidos foi de: ', totald)
            
