"""Exercicio 08

Faça um programa que pegue a lista e calcule a seguinte formula: 32x+125

Com o resultado desta formula mostre sómente os resultados maiores que 550. Para os resultados menores que 550 mostre "número invalido!"

lista = [1, 6, 9, 1, 5, 4, 8, 9, 15, 23, 14, 54, 82, 91, 45]
"""

lista = [1, 6, 9, 1, 5, 4, 8, 9, 15, 23, 14, 54, 82, 91, 45]
lista2=[]

for i in lista:
    resultado=32*i+125

    if resultado > 550:
        lista2.append(resultado)

    else:
        lista2.append(str(resultado)+"\033[1;31m Número Inválido! Resultado da equação é menor que 550.\033[m")

for j in range(len(lista)):

    print("Para X =",lista[j],end=" ")
    print("Resulta em:",end=" ")
    print(lista2[j])