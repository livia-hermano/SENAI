print('Me diga uma quantidade de dias, horas, minutos e segundos, e lhe direi esses valores juntos em segundos')
dia= int(input('Digite a quantidade de dias: '))
horas= int(input('Digite a quantidde de horas: '))
minu= int(input('Digite a quantidade de minutos: '))
segs= int(input( 'Digite a quantidade de segundos: '))
ds= (dia*24)*60*60
hs= (horas*60)*60
ms= (minu*60)
ss= segs
total= ds+hs+ms+ss
print('Os segundos são: ', total)
