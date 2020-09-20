# """Exercício 02

# O id de um cliente é um código único (só aquela pessoa tem) composto por números inteiros que inicia do número 1 e vai aumentando de 1 em 1 enquanto for necessário.

# Exemplo:
# id: 1
# Nome: Dudu

# id: 2
# Nome: Marta

# id: 3
# Nome: Pedro


# ATENÇÃO!!!!
# O id é um número atribuido automáticamente! O cliente não escolhe o número. O seu programa deve fazer o cadastro deste id automaticamente.


# Com isso, crie um cadastro de clientes que receba o id, nome e idade. Depois mostre os dados dos clientes individualmente.
# (cadastre no minimo 4 clientes)
# """

ids=[]
nomes=[]
idades=[]
rang=4
for i in range(rang):
    ids.append(i+1)
    nomes.append(str(input(f"Insira o nome do cliente {i+1}: ")))
    idades.append(int(input(f"Insira a idade do cliente {i+1}:  ")))

print("="*30)
for j in range(rang):
    print(f"""
ID do usuário: {ids[j]}
Nome do usário: {nomes[j]}
Idade do usuário: {idades[j]}
""")
print("="*30)