#-*- coding: UTF-8-*-
print('Digite suas 3 notas e quantas faltas você teve e lhe direi sua situação final.')
nota1=float(input('Digite a primeira nota:'))
nota2=float(input('Digite a segunda nota:'))
nota3=float(input('Digite a terceira nota:'))
falta=int(input('Digite sua quantidade de faltas:'))
media= (nota1+nota2+nota3)/3
falta_max= 80*25/100
if media>=7 and falta<=falta_max and media<10:
    print('Você está aprovado')
elif media<7 and media>0:
    print ('Você está reprovado por média')
elif falta>falta_max:
    print('Você foi reprovado por faltas')
else:
    print('Você inseriu algum valor inválido')
