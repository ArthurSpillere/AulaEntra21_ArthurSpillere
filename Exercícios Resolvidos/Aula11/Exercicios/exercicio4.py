"""Exercício 4

(use o conhecimento que foi passado no curso)

Crie um programa com um menu interativo:

-----
Cadastro de pessoas v1.0

A) Cadastrar Pessoa
B) Ver todos os nomes cadastrados:
C) Ver cadastro pelo nome:
D) Apagar um cadastro pelo nome:
S) Sair

-----

Para A: Cadastre os dados do cliente (Nome, idade, sexo, telefone
Para B: Mostre todos os nomes dos clientes (só os nomes)
Para C: Digite o nome do cliente e mostre todos os dados dele.
Para D: Digite o nome do cliente e o apague do cadastro
Para S: Mostre uma mensagem de despedida e termine o programa
Para qualquer outro valor: Mostre "Opção invalida"
"""


lista_nome=[]
lista_idade=[]
lista_sexo=[]
lista_telefone=[]

while True:
    validador=0
    sexo="S" #Altera sexo para um valor que ativará o while no código
    resp="L" #Altera resp para um valor que ativará o while no código
    print("="*40)
    print(f"{'Cadastro de pessoas v1.0':^40}")
    print("="*40)
    print("""
    A) Cadastrar Pessoa
    B) Ver todos os nomes cadastrados:
    C) Ver cadastro pelo nome:
    D) Apagar um cadastro pelo nome:
    S) Sair
    """)

    opc=str(input("Escolha uma opção: "))

    if opc=="" or opc not in "AaBbCcSs":
        print("\033[1;31mOpção inválida!\033[m")
        continue 

    elif opc in "Aa":
        nome=str(input("Nome do cliente: "))
        idade=str(input("Idade do cliente: "))
        while sexo not in "MmFf":
            sexo=str(input("Sexo do cliente [M/F]: "))
            if sexo not in "MmFf":
                print("Insira somente M ou F!")
        telefone=str(input("Telefone do cliente: "))

        lista_nome.append(nome)
        lista_idade.append(idade)
        lista_sexo.append(sexo)
        lista_telefone.append(telefone)
        print("\n\033[1;32mCadastro efetuado com sucesso!\033[m\n")

        while resp not in "SsNn":
            resp=str(input("Gostaria de fazer outra operação? [S/N] "))

        if resp in "Ss":
            continue
        else:    
            print("\nObrigado por usar nossos serviços!")    
            break    

    elif opc in "Bb":

        print(f"\nHá \033[33m{len(lista_nome)}\033[m pessoas cadastradas!")

        for i in range(len(lista_nome)):
            print({lista_nome[i]},end=", ")

        print()
        while resp not in "SsNn":
            resp=str(input("Gostaria de fazer outra operação? [S/N] "))

        if resp in "Ss":
            continue
        else:    
            print("\nObrigado por usar nossos serviços!")    
            break  

    elif opc in "Cc":
        if len(lista_nome)==0:
            print("\033[1;31mNão há pessoas cadastradas para consultar!\033[m\n")
        
        else:
            busca_nome=input("Quem você está procurando? ")

            for j,k in enumerate(lista_nome):
                if k==busca_nome:
                    validador=1
                    print(f"""
                    Nome:{lista_nome[j]}
                    Idade: {lista_idade[j]}
                    Sexo: {lista_sexo[j]}
                    Telefone: {lista_telefone[j]}
                    """)

            if validador==0:    
                print("Usuário não encontrado ou não cadastrado!")

        while resp not in "SsNn":
            resp=str(input("Gostaria de fazer outra operação? [S/N] "))

        if resp in "Ss":
            continue
        else:    
            print("\nObrigado por usar nossos serviços!")    
            break 

    elif opc in "Dd":
        if len(lista_nome)==0:
            print("\033[1;31mNão há pessoas cadastradas para apagar!\033[m\n")
        
        else:
            busca_nome=input("Quem você está querendo apagar do cadastro? ")

            for j,k in enumerate(lista_nome): #Pode-se usar lista.index(busca_nome) para achar o 'ID' da pessoa
                if k==busca_nome:
                    validador=1
                    lista_nome.pop(j)
                    lista_idade.pop(j)
                    lista_sexo.pop(j)
                    lista_telefone.pop(j)

                    print(f"{busca_nome} apagado com sucesso!")

            if validador==0:
                print("Usuário não encontrado ou não cadastrado!")
            

        while resp not in "SsNn":
            resp=str(input("Gostaria de fazer outra operação? [S/N] "))

        if resp in "Ss":
            continue
        else:    
            print("\nObrigado por usar nossos serviços!")    
            break 
    
    elif opc in "Ss":
        print("\n\033[1;32mObrigado por usar nossos serviços!\033[m")    
        break
    