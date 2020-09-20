# """Exercício 1

# (não usar o continue ou o break)

# Crie um programa que mostre um memu com as seguites opções:

# 1) Soma
# 2) Subtração
# 3) Multiplicação
# S) Para sair!

# Para número 1: Peça 2 números e mostre a soma deles
# Para número 2: Peça 2 númeors e mostre a subtração deles
# Para númeor 3: Peça 2 números e mostre a multiplicação deles
# Para S: Mostre uma mensagem de despedida e termine o programa.

# Para qualquer outra opção deve aparecer a mensagem "Opção Inválida"
# """

cores={'vermelho':'\033[1;31m','verde':'\033[1;32m', 'amarelo': '\033[1;33m', 'azul': '\033[1;34m', 'normal': '\033[m','invertido': '\033[7m'}

resp="0"
print("="*40)
print(f"{'Calculadora Python 1.0':^40}")
print("="*40)
while resp not in 'Ss':
    print("="*40)
    print("""    1) Soma
    2) Subtração
    3) Multiplicação
    S) Para sair!""")
    print("="*40)

    resp=str(input("""Escolha uma das opções acima: 
"""))

    if resp=="1":
        num1=int(input("\nInsira um valor para somar: "))
        num2=int(input("Insira um segundo valor para somar: "))
        print(f"\nA soma entre os números {cores['amarelo']}{num1}{cores['normal']} e {cores['amarelo']}{num2}{cores['normal']} é {cores['amarelo']}{num1+num2}{cores['normal']}")
    
    elif resp=="2":
        num1=int(input("\nInsira um valor para subtrair: "))
        num2=int(input("Insira um segundo valor para subtrair: "))
        print(f"\nA subtração entre os números {cores['azul']}{num1}{cores['normal']} e {cores['azul']}{num2}{cores['normal']} é {cores['azul']}{num1-num2}{cores['normal']}")
    
    elif resp=="3":
        num1=int(input("\nInsira um valor para multiplicar: "))
        num2=int(input("Insira um segundo valor para multiplicar: "))
        print(f"\nA multiplicação entre os números {cores['verde']}{num1}{cores['normal']} e {cores['verde']}{num2}{cores['normal']} é {cores['verde']}{num1*num2}{cores['normal']}")
    
    elif resp not in "Ss123":
        print(f"\n{cores['vermelho']}Resposta inválida!{cores['normal']}\n")


print(f"\n{cores['verde']}{'Obrigado por usar nossa calculadora!':^40}\n{'Adeus!':^40}{cores['normal']}")