"""Exercício 3

(use somente o while)

Faça um programa que peça o nome e a idade do cliente e mostre a seguinte mensagem:

Para mairores de 18 anos: Entrada Permitida
Para menores de 18 anos: Entrada proibida.

Depois mostre a lista dos nomes (somente os nomes) das pessoas com entrada permitida.

Regras:
- O programa não pode aceitar nomes em branco. Caso não se digite um nome o programa deve mostrar a mensagem "Nome em branco" e repetir o código.
- Caso o usuário deixe em branco a idade, o progama deve mostrar uma mensagem: "Obrigado pela preferência" e terminar logo em seguida.
"""

cores={'vermelho':'\033[1;31m','verde':'\033[1;32m', 'amarelo': '\033[1;33m', 'azul': '\033[1;34m', 'normal': '\033[m','invertido': '\033[7m'}

nomes=[]
idades=[]
nomes_aprovados=[]
idades_aprovados=[]

idade=2

while idade!="":
    nome=str(input("Insira o nome do cliente: "))
    while nome=="":
        print("Nome em branco.")
        nome=str(input("Insira o nome do cliente: "))

    idade=input("Insira a idade do cliente: (Deixe em branco para sair)")

    if idade=="":
        print(f"\n{cores['azul']}Obrigado pela preferência!{cores['normal']}")

    elif int(idade)>=18:
        print(f"\n{cores['verde']}Entrada Permitida!{cores['normal']}\n")
        nomes.append(nome)
        nomes_aprovados.append(nome)
        idades.append(int(idade))
        idades_aprovados.append(int(idade))
        print(f"As pessoas aprovadas até o momento foram: {nomes_aprovados}\n")
        

    elif int(idade)<18:
        print(f"\n{cores['vermelho']}Entrada Proibida!{cores['normal']}\n")
        nomes.append(nome)
        idades.append(int(idade))
        print(f"As pessoas aprovadas até o momento foram: {nomes_aprovados}\n")

