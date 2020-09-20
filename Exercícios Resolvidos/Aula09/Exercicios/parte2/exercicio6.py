
"""Exercicio 06

Faça um programa que peça ao usuário que digite o nome de 10 pessoas. Depois mostre cada nome em linhas separadas.
"""
lista=[]
for i in range(10):
    lista.append(str(input(f"Digite o nome da {i+1}º pessoa: "))) 

for j in range(10):
    print(lista[j])