# """Exercício 2

# (não usar o continue ou o break)

# Crie um menu interativo com as seguintes opções:

# A) soma
# B) Média
# C) Taboada
# S) Sair


# Para A: Peça 2 números, some e mostr o resultado
# Para B: Peça 4 números, faça a média e mostre o resultado
# Para C: Peça um número e mostre a taboada dele
# Para S: Mostre uma mensagem de despidida e encerre o programa.
# Para qualquer outro valor: Mostre a mensagem "opção inválida"""

cores={'vermelho': '\033[1;31m','verde': '\033[1;32m', 'amarelo': '\033[1;33m',
       'azul': '\033[1;34m', 'normal': '\033[m','invertido': '\033[7m'}


print("="*40)
print(f"{'Matemática com Python!':^40}")
print("="*40)

resp = "0"
resp2 = "0"
while resp not in 'Ss' or resp == "":
    print("="*40)
    print("""    A) Soma
    B) Média
    C) Tabuada
    S) Para sair!""")
    print("="*40)

    resp = str(input("""Escolha uma das opções acima: 
"""))

    if resp not in "SsAaBbCc" or resp == "":
        print("\nResposta inválida!\n")

    elif resp in "Aa":
        num1=int(input("\nInsira um valor para somar: "))
        num2=int(input("Insira um segundo valor para somar: "))
        print(f"""\nA soma entre os números {cores['verde']}{num1}
        {cores['normal']} e {cores['verde']}{num2}{cores['normal']} é 
        {cores['verde']}{num1+num2}{cores['normal']}""")
        
        while resp2 not in "SsNn" or resp2 == "":
            resp2=str(input("""\nDeseja fazer outra operação?
"""))
            if resp2 == "S" or resp2 == "s":
                resp = "0"
            elif resp2 == "n" or resp2 == "N":
                resp = "s"
            else:
                print(f"{cores['vermelho']}Resposta inválida!{cores['normal']}")

    elif resp in "Bb":
        print("\nInsira 4 valores para tirar a média: ")
        
        num1 = int(input("Valor 1: "))
        num2 = int(input("Valor 2: "))
        num3 = int(input("Valor 3: "))
        num4 = int(input("Valor 4: "))

        print(f"""A média entre os números {cores['azul']}{num1}, {num2},
         {num3}, {num4}{cores['normal']} é {cores['azul']}
         {(num1+num2+num3+num4)/4}{cores['normal']}""")

        while resp2 not in "SsNn" or resp2 == "":
            resp2 = str(input("""\nDeseja fazer outra operação?"""))

            if resp2 == "S" or resp2 == "s":
                resp = "0"
            elif resp2 == "n" or resp2 == "N":
                resp = "s"
            else:
                print(f"{cores['vermelho']}Resposta inválida!{cores['normal']}")

    elif resp in 'Cc':
        num1=int(input("\nInsira um valor para ver a tabuada dele: "))
        print("")
        print("="*40)
        print(f"{'Tabuada do '+str(num1):^40}")
        print("="*40)
        print(f"{cores['amarelo']}",end="")
        i=0
        while i<10:
            i+=1
            print(f"{str(num1)+' x '+str(i)+' = '+str(num1*i):^40}")

        print(f"{cores['normal']}",end="")

        while resp2 not in "SsNn" or resp2=="":
            resp2=str(input("""\nDeseja fazer outra operação?
"""))
            if resp2=="S" or resp2=="s":
                resp="0"
            elif resp2=="n" or resp2=="N":
                resp="s"
            else:
                print(f"{cores['vermelho']}Resposta inválida!{cores['normal']}")

print(f"""\n{cores['verde']}{'Obrigado por usar nosso centro matemático!':^40}
{'Adeus!':^40}{cores['normal']}""")
