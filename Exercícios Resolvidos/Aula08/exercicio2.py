

# 2) Crie uma lista com 10 números qualquer.
# 
# Usando as funções da lista responda:
# 
# Quantos itens tem a lista?
# Qual é o número maior?
# Qual é o número menor?
# Qual é o resultado da soma da lista?

from random import randint
lista=[]
for i in range (1,11):
    lista.append(randint(1,50))

print(lista)
maxi=max(lista)
mini=min(lista)
soma=sum(lista)

print(f"""
Na lista acima criada temos como:
Maior número - {maxi}
Menor número - {mini}
Soma de todos - {soma}
""")


#Ou criar uma lista com números aleatórios pré determinados:
# # lista2=[2,7,10,4,5,6,2,25,12,30]
# print(lista)
# maxi=max(lista)
# mini=min(lista)
# soma=sum(lista)
