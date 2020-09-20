"""Exercicio 07

Faça um programa que receba 10 idades e mostre a seguinte mensagem:

Para maiores de 18 anos: Ingreços da Rave liberado!
De 16 a 18 anos: Ingreços de cinema liberado 
De 13 a 16 anos: Ingreços para fliperama liberado
Menores de 13 anos: Psicina de bolinhas liberado
"""

idades=[]

for i in range(1,11):
    idades.append(int(input(f"Insira a idade do cliente {i}: ")))

for j in range(10):

    print(f"Você tem {idades[j]}.",end=" ")

    if idades[j]>=18:
         print("\033[1;32mIngressos da Rave liberados!\033[m")
    
    elif 16<=idades[j]<18:
        print("\033[1;33mIngressos de cinema liberados!\033[m")

    elif 13<=idades[j]<16:
        print("\033[1;35mIngressos para o fliperama liberados!\033[m")

    elif 0<=idades[j]<13:
        print("\033[1;36mIngressos para a piscina de bolinhas liberados!\033[m")

    else:
        print("\033[1;31mIdade Inválida\033[m")