#Listas com reajustes e salario maximo da categoria de aumento
reajuste = [15, 12, 10, 7, 4]
faixas = [400, 800, 1200, 2000]

#Recebe o salário do funcionário
salario = float(input())

#Verifica em que categoria o salário se encontra
if salario > 2000:
    novo_salario = salario * (1 + reajuste[4]/100)
    ganho = salario * (reajuste[4]/100)
    print(f"""Novo salario: {novo_salario:.2f}
Reajuste ganho: {ganho:.2f}
Em percentual: {reajuste[4]} %""")

else:
    for i,j in enumerate(faixas):
        if salario <= j:
            novo_salario = salario * (1 + reajuste[i]/100)
            ganho = salario * (reajuste[i]/100)
            print(f"""Novo salario: {novo_salario:.2f}
Reajuste ganho: {ganho:.2f}
Em percentual: {reajuste[i]} %""")
            break
