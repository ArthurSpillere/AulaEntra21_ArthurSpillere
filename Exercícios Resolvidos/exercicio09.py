
# Exercicio 9
# Faça um programa que peça o nome do cliente, a quantidade do produto (inteiro) e o preço (float).
# 
# Mostre o nome do cliente e o valor total da venda.

cliente=str(input('Insira o nome do cliente: '))
qtde_produtos=int(input('Insira a quantidade de produtos comprada pelo cliente: '))
preco=float(input('Insira o valor a ser pago: '))

print(f'Nome do cliente: {cliente}\nProdutos comprados: {qtde_produtos}\nValor total: R${preco}')


