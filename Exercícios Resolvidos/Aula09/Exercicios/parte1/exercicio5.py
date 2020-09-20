"""Exercicio 05

Faça um programa que peça ao usuário digitar a quantidade de vendas do dia. Cadastre cada venda separadaemnte e depois mostre a média e o valor total vendido no dia.
"""
vendas=[]
total=int(input("Quantas vendas fora realizadas hoje? "))
print("\nCadastre o que foi vendido abaixo.\n")

for i in range(total):
    venda_add=vendas.append(float(input(f"Qual o valor vendido do produto {i+1}? ")))

soma=sum(vendas)
media=soma/total
print(f"""
Foram vendidos \033[7m{total:^3}\033[m produtos.
A média do valor das vendas foi de \033[1;32mR${media}\033[m
O total vendido foi de \033[1;32mR${soma}\033[m""")
    
