# Exercicio 6
# Escreva um programa que peça 2 números e mostre eles em ordem crescente

valor1=float(input("Insira um valor: "))
valor2=float(input("Insira um outro valor: "))

if valor1>valor2:
    print(valor2,valor1)
else:
    print("Os valores em ordem crescente: ",valor1,valor2)