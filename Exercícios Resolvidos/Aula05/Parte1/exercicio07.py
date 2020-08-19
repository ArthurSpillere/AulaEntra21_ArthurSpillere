# Exercicio 7
# Faça um programa que peça 3 números inteiros e mostre o menor número.

x=int(input("Insira um primeiro valor: "))
y=int(input("Insira um segundo valor: "))
z=int(input("Insira um terceiro valor: "))

if x<y and x<z:
    print(f"O menor valor é: {x}")
elif y<x and y<z:
    print(f"O menor valor é: {y}")
else:
    print(f"O menor valor é: {z}")



