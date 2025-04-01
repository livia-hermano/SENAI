print ('Qual a velocidade do seu carro?')
vel= float(input('Digite aqui: '))
if vel>80:
    multa= (vel-80)*5
    print ('Você ultrapassou o limite de velocidade e será multado no valor de: ',multa)
else:
    print ('Está dentro do limite.')
