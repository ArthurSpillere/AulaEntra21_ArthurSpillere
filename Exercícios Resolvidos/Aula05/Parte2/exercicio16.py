# Exercicio 16
# 
# Crie um programa para uma promoção de um posto de combustivel.
# 
# O programa deve pedir ao usuário quantos litros ele quer abastecer e qual combustivel: álcool, diessel ou gasolina
# 
# A promoção é a seguinte:
#  - Para gasolina: Até 20 litros 0% de desconto e acima de 20 litros 10% de desconto
#  - Para diessel: Até 10 litro 1.5% de desconto e acima de 10 litros 5% de desconto
#  - para álcool: Até 10 litros 5% de desconto e acima de 10 litros 10% de desconto.
#  
# Mostre o combustivel que ele selecionou, o total abastecido e a porcentagem de desconto a ser aplicada.
# 
# Não precisa calcular o valor do combustivel!
# 

opcao=int(input("""
Bem vindo ao posto Python!
Com qual o combustível você deseja abastecer?

1- Gasolina
2- Diesel
3- Álcool
4- Sair

Entre com a opção aqui: 
"""))


if opcao==1:

    qtdecombu=int(input("Quantos litros você gostaria de abastecer? "))
    
    if 0< qtdecombu <=20:
        print(f"Você abasteceu {qtdecombu} litros de Gasolina e não recebeu desconto.")
    elif qtdecombu>20:
        print(f"Você abasteceu {qtdecombu} litros de Gasolina e recebeu 10% de desconto.")
    else:
        print("Você entrou com um valor inválido.")

elif opcao==2:

    qtdecombu=int(input("Quantos litros você gostaria de abastecer? "))

    if 0<qtdecombu<=10:
        print(f"Você abasteceu {qtdecombu} litros de Diesel e recebeu 1.5% de desconto.")
    elif qtdecombu>10:
        print(f"Você abasteceu {qtdecombu} litros de Diesel e recebeu 5% de desconto.")
    else:
        print("Você entrou com um valor inválido.")

elif opcao==3:

    qtdecombu=int(input("Quantos litros você gostaria de abastecer? "))

    if 0<qtdecombu<=10:
        print(f"Você abasteceu {qtdecombu} litros de Álcool e recebeu 5% de desconto.")
    elif qtdecombu>10:
        print(f"Você abasteceu {qtdecombu} litros de Álcool e recebeu 10% de desconto.")
    else:
        print("Você entrou com um valor inválido.")

elif opcao==4:
    print("Operação Encerrada")

else:
    print("Valor inválido")