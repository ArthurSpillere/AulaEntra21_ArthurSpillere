# Exercicio 13
# 
# Crie um programa que peça o nome do cliente, idade, endereço, email e telefone.
# 
# Depois crie um menu interativo com as seguintes opções: Dados, Endereço, Contato.
# 
# Se o usuário selecionar "Dados" deve aparecer o nome do cliente e a idade
# 
# Se o usuário selecionar "Endereço" deve aparecer o nome do cliente e o endereço
# 
# Se o usuário selecionar "Contato" deve aparecer o nome do cliente, email e o telefone

print("Bem vindo ao cadastro do cliente!\nPreencha as informações a seguir!")
nome=str(input("Nome: "))
idade=str(input("Idade: "))
endereco=str(input("Endereço: "))
email=str(input("E-mail: "))
telefone=str(input("Telefone:"))

opcao=int(input("""
Qual opção você gostaria de ver?

1- Dados do Cliente
2- Endereço do Cliente
3- Contato do Cliente
4- Sair

Insira aqui sua opção: """))

if opcao==1:
    print(f"Cliente: {nome}\nIdade:{idade}")
elif opcao==2:
    print(f"Cliente: {nome}\nEndereço: {endereco}")
elif opcao==3:
    print(f"Cliente:{nome}\nE-mail: {email}\nTelefone: {telefone}")
elif opcao==4:
    print("Operação Encerrada!")
else:
    print("Opção Inválida!")




