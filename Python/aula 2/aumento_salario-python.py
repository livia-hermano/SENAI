print ('Me diga o valor do seu salário e lhe direi o valor do aumento')
sal= float(input('Digite aqui: '))
if sal>1250:
    dp=sal*10/100
    print ('O seu salário aumentou em 10% e ficará no valor de: ', dp)
elif sal<1250:
    qp= sal*15/100
    print('O seu salário aumentou em 15% e ficará no valor de: ',qp)
