#Entrada
a = int(input())
b = int(input())
soma = 0

#Calcula a soma dos números impares entre os valores
if b < a:
    troca = b
    b = a
    a = troca

for i in range(a+1, b):
    if i % 2 != 0:
        soma += i

print(soma)
