"""Exercicio 04

Faça um programa de cadastro de pessoas que receba 10 nomes, idades e e-mails e salve cada um em uma lista.

Depois mostre as listas separadamente 
(print (lista) já é o suficiente)
"""
nomes=[]
idades=[]
emails=[]

for i in range(1,11):
    nomes.append(str(input(f"Insira o nome do {i}º cliente: ")))
    idades.append(int(input(f"Insira a idade do {i}º cliente: ")))
    emails.append(str(input(f"Insira o e-mail do {i}º cliente: ")))

print("\n",nomes,"\n")
print(idades,"\n")
print(emails)

