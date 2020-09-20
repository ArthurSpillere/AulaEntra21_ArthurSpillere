
"""Exercicio 02

Faça um programa que mostre a tabuada de 1, 2, 3 e 4
"""

for i in range(1,5):

    print(f"{'TABUADA DO ' + str(i):=^20}")
    for c in range(1,11):
        # print(f"{c:2} X {i:2} = {c*i:2}") #Sem formatação
        print(f"{str(c)+' X '+str(i) +' = '+str(c*i):^20}")

    print("="*20)
    print("")