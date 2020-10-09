#--- Exercício 5 - Funções
#--- Crie uma função para calculo de raiz
#--- A função deve ter uma variável que deternine qual é o indice da raiz(raiz quadrada, raiz cubica...)
#--- Leia um número do console, armazene em uma variável e passe para a função
#--- Realize o calculo da raiz e armazene em uma segunda variável e retorne 
#--- Imprima o resultado e uma mensagem usando f-string, fora da função

def raiz(valor, indice):
    return (valor)**(1/indice), indice

num = float(input("Insira um número para tirar a raíz:\n"))
indice_raiz = int(input("Insira o índice da raiz:\n"))
resultado_raiz = raiz(num, indice_raiz)

print(f"A raíz de índice {resultado_raiz[1]} de {num:.1f}"
      f" é {resultado_raiz[0]:.1f}")
