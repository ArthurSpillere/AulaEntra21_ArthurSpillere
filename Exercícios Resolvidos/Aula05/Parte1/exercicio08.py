# Exercicio 8
# Faça um programa que peça 3 números inteiros e mostre o número maior.

x=int(input("Insira um primeiro valor: "))
y=int(input("Insira um segundo valor: "))
z=int(input("Insira um terceiro valor: "))

if x>y and x>z:
    print(f"O maior valor é: {x}")
elif y>x and y>z:
    print(f"O maior valor é: {y}")
else:
    print(f"O maior valor é: {z}")



