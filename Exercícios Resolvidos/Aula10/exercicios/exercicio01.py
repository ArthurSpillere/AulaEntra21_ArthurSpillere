# '''
# Exercício 01

# Crie um programa que cadastre 5 clientes. 

# Cada cliente possui: Nome, sexo, Telefone
# (Guarde estes dados em listas separadas).

# Depois mostre os dados cadastrados no seguinte formato:



# ***********************************
# Relatório de clientes cadastrados 
# ***********************************
# Nome: 
# Sexo:
# Telefone:
# ***********************************
# """)

nome=[]
sexo=[]
telefone=[]
rang=5

for i in range(rang):
    nome.append(str(input(f"Insira o nome do cliente {i+1}: ")))
    sexo.append(str(input(f"Insira o sexo do clietne {i+1}: [M/F] ").strip().upper()[0]))
    telefone.append(str(input(f"Insira o telefone do cliente {i+1}: ")))

print("\n")
print("*"*40)
print(f"{'Relatório de Clientes Cadastrados':^40}")
print("*"*40)

for j in range(rang):

    print(f"Nome: {nome[j]}")
    print(f"Sexo: {sexo[j]}")
    print(f"Telefone: {telefone[j]}")
    print("")

print("*"*40)