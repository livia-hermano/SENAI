#-*- coding: UTF-8-*-
print('Me diga sua média e lhe direi se está aprovado, de recuperação ou reprovado.')
media= int(input('Digite sua média:'))
if media>=7 and media<10:
    print('Você está aprovado')

elif media<3 and media>=0:
    print('Você está reprovado')

elif media>=3 and media<7:
    print('Você está de recuperação')

else:
    print('Você inseriu um valor inválido.')
