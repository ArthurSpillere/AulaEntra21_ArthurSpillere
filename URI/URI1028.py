#Entrada
casos = int(input())

#Calcula o Máximo Divisor Comum entre os valores que serão inseridos
for i in range(casos):
    a, b = map(int, input().split())
    while b != 0:
        resto = a % b
        a = b
        b = resto

    print(a)
