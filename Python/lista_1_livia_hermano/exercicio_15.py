#-*- coding: UTF-8-*-
print ('Me diga a temperatura atual e eu lhe direi o resultado de como o clima está.')
temp= int(input('Coloque a temperatura aqui: '))
if temp<=15:
    print('O clima está muito frio.')
elif temp>=16 and temp<23:
    print('O clima está frio.')
elif temp>=23 and temp<26:
    print('O clima está agradável.')
elif temp>=26 and temp<30:
    print ('Está calor.')
else:
    print('O clima está muito quente.')
