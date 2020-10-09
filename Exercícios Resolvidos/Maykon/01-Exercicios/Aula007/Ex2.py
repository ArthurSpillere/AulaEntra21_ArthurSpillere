
#--- Exercício 2  - Funções
#--- Escreva uma função que leia dois números do console
#--- Armazene cada número em uma variável
#--- Realize a divisão entre os dois números e armazene o resultado em uma terceira variável
#--- Imprima o resultado e uma mensagem usando f-string

def divisao(num1, num2):
    if num2 == 0:
        return "Impossível divisão por 0!"
        
    else:
        return round(num1 / num2, 2)
    
print(divisao(float(input("Insira um número para ser dividido: ")),
              float(input("Insira um número para dividir: "))))

print()

a = float(input("Insira um número para ser dividido:\n"))
b = float(input("Insira um número para dividir:\n"))
print(divisao(a, b))

print()

print(divisao(10, 3))

print()

print(divisao(10, 0))
