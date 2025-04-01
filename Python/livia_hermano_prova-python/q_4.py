print('Olá usuário. Digite um número e direi se ele é primo ou não.')

def primo(n):
    cont=0
    for i in range (1,n):
        if n%i==0:
            cont+=1
    if cont==1:
        print(f'''O número {n} é primo.''')
    else:
        print(f'''O número {n} não é primo.''')
n=int(input('Digite o número aqui:'))
primo(n)
