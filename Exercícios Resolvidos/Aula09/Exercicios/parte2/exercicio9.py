
"""Exercicio 09

Faça um programa que pegue uma lista de valores e separe em 2 listas. Uma com valores menores que 500.00 e outra com maiores ou igual.

Depois motre o maior e o menor valor da cada lista.

vandas = [100.00, 500.00, 258.50, 710.00, 50.50,750.00, 10.00, 1050.00, 859.75, 199.05, 500.50,750.00, 568.60, 950.00, 950.00, 89.90, 2500.00, 1750.00,500.00]
"""
vandas = [100.00, 500.00, 258.50, 710.00, 50.50,750.00, 10.00, 1050.00, 859.75, 199.05, 500.50,750.00, 568.60, 950.00, 950.00, 89.90, 2500.00, 1750.00,500.00]
listamenor=[]
listamaior=[]

for i in range(len(vandas)):
    if vandas[i] < 500:
        listamenor.append(vandas[i])

    else:
        listamaior.append(vandas[i])

print(f"""
\033[1;4;36mLista com valores menores que 500:\033[m
{listamenor}
Maior valor: \033[33m{max(listamenor)}\033[m
Menor valor: \033[32m{min(listamenor)}\033[m

\033[1;4;36mLista com valores maiores o iguai a 500:\033[m
{listamaior}
Maior valor: \033[33m{max(listamaior)}\033[m
Menor valor: \033[32m{min(listamaior)}\033[m""")
    

