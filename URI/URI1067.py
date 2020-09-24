#Entrada
a = int(input())

#Mostra todos os ímpares após número de entrada (ele inclusive)

for i in range(a+1):
    if i % 2 != 0:
        print(i)
