# Exercicio 10
# Faça um programa que peça o nome de 2 produtos, a quantidade comprada de cada produto (inteiro) e o valor (float) de cada um.
# 
# Mostre o nome a quantidade, preço por unidade e o total de cada produto.

prod1=str(input('Insira o nome do primeiro produto: '))
qtde1=int(input('Qual quantidade do primeiro produto? '))
preco=float(input('Informe o preço do primeiro produto:'))
prod2=str(input('Insira o nome do segundo produto: '))
qtde2=int(input('Qual a quantidade do segundo produto?'))
preco2=float(input('Informe o preço do segundo produto'))
print(f"""
O produto 1 é:{prod1}
Foram compradas {qtde1} unidades
O custo unuitário é de R${preco:.2f}

O produto 2 é: {prod2}
Foram compradas {qtde2} unidades
O custo unitário é de R${preco2:.2f}""")