#Entrada
a = int(input())

#Mostra os 6 números ímpares após número recebido (inclui o número de entrada)

for i in range(6):
    if a % 2 == 0:
        print(a+1)
        a += 3
    
    else:
        print(a)
        a += 2
