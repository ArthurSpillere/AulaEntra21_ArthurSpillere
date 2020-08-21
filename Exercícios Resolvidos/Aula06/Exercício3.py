# """Execicios 03

# Escreva um programa que contenha um menu com 4 opções:
# A) soma
# B) média
# C) divisão
# D) Sair

# As opções podem ser escolhidas com as letras maiusculas ou minusculas.

# Para a opção soma, deve solicitar 2 números, fazer a soma e mostrar o resultado.

# Para a opção média, deve solicitar 4 números, fazer a média e mostrar os resultados.

# Para a opção divisão, deve solicitar 2 números, dividir o primeiro pelo segundo e montrar o resultado. Caso o segundo for igual a 0, então deve mostrar o a mensagem "Erro! Não pode dividir por ZERO!"

# Para a opção sair, deve aparecer a mensagem: "Muito Obrigado e Volte sempre!"
# """

print("-=-"*30)
print("""Bem vindo a calculadora Python!

A) soma
B) média
C) divisão
D) Sair
""")

opcao=str(input("Escolha uma das opções: "))

if opcao=="a" or opcao=="A":

    num1=int(input("Escolha um valor para somar: "))
    num2=int(input("Escolha um segundo valor para somar: "))
    resultado=num1+num2

    print(f"A soma dos número {num1} e {num2} é de: {resultado}")

elif opcao=="b" or opcao=="B":

    num1=int(input("Escolha um valor para tirar a média: "))
    num2=int(input("Escolha um segundo valor para tirar a média: "))
    
    resultado=(num1+num2)/2

    print(f"A média dos número {num1} e {num2} é de: {resultado}")

elif opcao=="c" or opcao=="C":

    num1=int(input("Escolha um valor para ser dividido: "))
    num2=int(input("Escolha um segundo valor para dividir o primeiro valor: "))
    
    if num2!=0:
    
        resultado=num1/num2

        print(f"A divisão de {num1} por {num2} é de: {resultado}")

    else:

        print("Divisor = 0, operação não é possível!")

elif opcao=="d" or opcao=="D":

    print("Muito Obrigado e Volte sempre!")

else:

    print("Você digitou um valor inválido. Tente Novamente.")

print("-=-"*30)