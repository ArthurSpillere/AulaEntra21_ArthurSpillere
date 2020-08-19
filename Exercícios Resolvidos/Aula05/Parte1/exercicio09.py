# Exercicio 9
# Faça um programa que peça 3 números inteiros e mostre o os tês em ordem crescente.
# 
#
valor1=int(input("Insira um primeiro valor: "))
valor2=int(input("Insira um segundo valor: "))
valor3=int(input("Insira um terceiro valor: "))

if valor1==valor2 or valor1==valor3 or valor2==valor3:
    if valor1==valor2==valor3:
        print(f"Os valores na ordem crescente são: {valor1}, {valor2}, {valor3}")
    elif valor1==valor2>valor3:
        print(f"Os valores na ordem crescente são: {valor3}, {valor2}, {valor1}")
    elif valor1==valor2<valor3:
        print(f"Os valores na ordem crescente são: {valor1}, {valor2}, {valor3}")
    elif valor1==valor3>valor2:
        print(f"Os valores na ordem crescente são: {valor2}, {valor3}, {valor1}")
    elif valor1==valor3<valor2:
        print(f"Os valores na ordem crescente são: {valor1}, {valor3}, {valor2}")
    elif valor3==valor2>valor1:
        print(f"Os valores na ordem crescente são: {valor1}, {valor2}, {valor3}")
    elif valor3==valor2<valor1:
        print(f"Os valores na ordem crescente são: {valor3}, {valor2}, {valor1}")
else:
    
    if valor1>valor2 and valor1>valor3:
        maior=valor1
    elif valor2>valor1 and valor2>valor3:
        maior=valor2
    else:
        maior=valor3

    if valor1<valor2 and valor1<valor3:
        menor=valor1
    elif valor2<valor1 and valor2<valor3:
        menor=valor2
    else:
        menor=valor3

    if menor==valor1 and maior==valor2:
        meio=valor3
    elif menor==valor1 and maior==valor3:
        meio=valor2
    elif menor==valor2 and maior==valor3:
        meio=valor1
    elif menor==valor2 and maior==valor1:
        meio=valor3
    elif menor==valor3 and maior==valor1:
        meio=valor2
    else:
        meio=valor1

    print(f"Os valores na ordem crescente são: {menor}, {meio}, {maior}")
