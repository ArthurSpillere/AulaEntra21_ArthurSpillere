#Entrada
num = int(input())

#Mostra os quadrados de todos os números pares de 0 até o número de entrada

for i in range(1, num+1):
    if i % 2 == 0:
        print(f"{i}^2 = {i**2}")
