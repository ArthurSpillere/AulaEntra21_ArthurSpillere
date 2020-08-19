# Exercicio 12
# 
# Crie um programa que peça 2 números.
# 
# Depois mostre um menu interativo contendo 5 operações matemáticas do python
# (adição, subtração, multiplicação, divisão e expoente)
# 
# Peça para o usuário escolher uma destas opções e mostre o resultado da operação escolhida.

x=float(input("Insira um primeiro valor:"))
y=float(input("Insira um segundo valor:"))

opcao=int(input("""
Qual operação você gostaria de realizar?

1- Adição
2- Subtração
3- Multiplicação
4- Divisão
5- Potência
6- Sair

Digite aqui a opção:"""))

if opcao==1:
    print(f"{x} + {y} = {x+y}")
elif opcao==2:
    print(f"{x} - {y} = {x-y}")
elif opcao==3:
    print(f"{x} * {y} = {x*y}")
elif opcao==4:
    print(f"{x} / {y} = {x/y}")
elif opcao==5:
    print(f"{x} ^ {y} = {x**y}")
elif opcao==6:
    print("Operação Encerrada")
else:
    print("Opção inválida!")


