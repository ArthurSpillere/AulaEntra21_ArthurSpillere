# """Exercício 03

# 3.1) Crie um programa que cadastre o id, nome, sexo e a idade de 5 clientes.

# 3.2) Depois mostre os dados dos 5 clientes.

# 3.3) Peça para que o usuário escolha um id de um cliente e mostre as informações deste cliente.

# 3.4) Crie um filtro que ao digitar um id de um cliente mostre as seguintes informações:
# - Para menores de 17 anos: Entrada Proibida
# - Para maiores de 17 anos: Entrada Liberada
# - Para o sexo Feminino: 50% de desconto
# - Para o sexo Masculino: 5% de desconto
# """
##############################################################################

#CADASTRO DO CLIENTE:

ids=[]
nomes=[]
sexos=[]
idades=[]
rang=5
for i in range(rang):
    ids.append(i+1)
    nomes.append(str(input(f"Insira o nome do {i+1}º cliente: ").title()))
    while True:
        sexo_cliente=str(input(f"Insira o sexo do {i+1}º cliente: [M/F] ").strip().upper()[0])
        if sexo_cliente in "MF":
            sexos.append(sexo_cliente)
            break
               
    idades.append(int(input(f"Insira a idade do {i+1}º cliente: ")))

#APRESENTAÇÃO DOS USUÁRIOS CADASTRADOS

print("\n")
print("=+"*20)
print(f"{'Usuários Registrados':^40}")
print("=+"*20)

for j in range(rang):
    print(f"""
Usuário: {nomes[j]}
ID: {ids[j]}
Sexo: {sexos[j]}
Idade: {idades[j]}""")

#OPÇÃO DE ESCOLHER UM ID
print("")
while True:

    while True:
        print(f"Escolha uma ID para mais informações: [IDs: {min(ids)}-{max(ids)}] ")
        resp=int(input())
        if min(ids)<=resp<=max(ids):
            break
        
    print(f"""\033[1;34m
    Usuário: {nomes[resp-1]}
    ID: {ids[resp-1]}
    Sexo: {sexos[resp-1]}
    Idade: {idades[resp-1]}\033[m""")
    
    #FILTRO - MENSAGEM FINAL PARA O USUÁRIO

    if idades[resp-1]<17:
        print("\n\033[1;31mEntrada Proibida!\033[m\n")

    else:
        print("\n\033[1;32mEntrada Liberada!\033[m\n")
        
        if sexos[resp-1] == "M":
            print("Você ganhou 5% de desconto!\n")

        elif sexos[resp-1] == "F":
            print("Você ganhou 50% de desconto!\n")
    
    resp2="L"
    while resp2 not in "SN":
        resp2=str(input("Você gostaria de ver outro ID? [S/N] ").strip().upper()[0])

    if resp2=="N":
        break


