# Exercicio 2
# Faça um programa que peça um número.
# 
# Mostre na tela se este número é negativo ou positivo. (lembrando que números positivos são maiores que zero!)

valor=float(input("Insira um valor positivo ou negativo: "))

if valor>0:
    print("O número é positivo!")
elif valor==0:
    print("O valor é 0")
else:
    print("O valor é negativo")