print('Olá usuário. Digite um número e direi quais os números ímpares até chegar a esse número.')
n=int(input('Digite aqui:'))
for i in range (1,n):
    if i%2==1:
        print(i)
print(n)
