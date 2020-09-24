#Recebe os 3 números para comparação
a, b, c = map(int, input().split())
lista = [a, b, c]
lista2 = lista[:]
#Sorteia os números em ordem crescente
lista.sort()
for i in lista:
    print(i)
print()
for j in lista2:
    print(j)
