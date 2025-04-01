L=[]
soma=0

for i in range(10):
    c = str(input('Digite a letra aqui:'))
    L.append(c)
    if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
        soma += 0
    else:
        soma = soma + 1
print(soma)
        
