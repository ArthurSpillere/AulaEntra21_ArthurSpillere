# Exercicio 17
# crie um programa que peça 4 notas de um aluno e calcule a média "(nota1+nota2+nota3+nota4)/4" e retorne:
# 
# Pra média igual a 10 apareça a mensagem "Aprovado com louvor"
# Pra média maior igual a 7 apareça a mensagem "Aprovado"
# Pra média menor que 7 apareça a mensagem "Reprovado"
# 
nota1=float(input("Insira a nota 1: "))
nota2=float(input("Insira a nota 2: "))
nota3=float(input("Insira a nota 3: "))
nota4=float(input("Insira a nota 4: "))

media=(nota1+nota2+nota3+nota4)/4

if media==10.0:

    print(f"Aprovado com louvor! Média:{media}")

elif media>=7.0 and media<10.0:

    print(f"Aprovado! Média:{media}")

else:

    print(f"Reprovado. Média: {media}")