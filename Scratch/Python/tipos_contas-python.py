print ('Que tipo de conta deseja realizar? (+)para soma,(-) para subtração, (*) para multiplicação e (/) para divisão)')
conta= int(input('Digite aqui: '))
if conta == 'soma':
    print ('Você escolheu realizar uma conta de soma.')
    pvs= int(input('Digite o primeiro valor para a soma: '))
    svs= int(input('Digite o segundo valor para a soma: '))
    ts= pvs+svs
    print('O total da soma é: ',ts)
elif conta == 'subtração':
    print('Você escolheu realizar uma conta de subtração.')
    pvsub= int(input('Digite o primeiro valor para a subtração: '))
    svsub= int(input(' Digite o segundo valor para a subtração: '))
    tsub= pvsub-svsub
    print('O total da subtração é: ', tsub)
 elif conta == 'multiplicação':
     print('Você escolheu realizar uma conta de multiplicação.')
     pvm=int(input('Digite o primeiro valor para a multiplicação: '))
     svm= int(input('Digite o segundo valor para a multiplicação: '))
     tm= pvm*svm
     print ('O total da multiplicação é de: ', tm)
elif conta == 'divisão':
    print ('Você escolheu realizar uma conta de divisão')
    pvd=int(input('Digite o primeiro valor para a divisão: '))
    svd=int(input('Digite o segundo valor para a divisão: '))
    td= pvd/svd
    print('O total da divisão é de: ',td)
                
                       
        
