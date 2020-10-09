#--- Exercício 3  - Funções
#--- Crie uma função que leia três números float
#--- Armazene cada valor lido em uma variável
#--- Calcule a média entre os três números e armazene em uma quarta variável
#--- Imprima a média e uma mensagem usando f-string (módulo 3)

def media(num1, num2, num3):
    media = (num1 +num2 + num3)/ (3)

    print(f"""As notas do aluno foram:

N1 = {num1:.2f}
N2 = {num2:.2f}
N3 = {num3:.2f}

A média final foi de:
{media:.2f}""")

media(2.5, 6.0, 10)
media(10.0, 10.0, 10.0)
media(0, 0, 0)
