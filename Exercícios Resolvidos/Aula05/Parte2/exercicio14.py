# Exercicio 14
# Crie um programa que peça ao usuário digitar um número de 1 a 7 e mostre o dia da semana correspondente sendo que segunda feira é o numero 1 e domingo é 7.

numsemana=int(input("Insira um número de 1-7: "))

if numsemana==1:
    print("Segunda-Feira")
elif numsemana==2:
    print("Terça-Feira")
elif numsemana==3:
    print("Quarta-Feira")
elif numsemana==4:
    print("Quinta-Feira")
elif numsemana==5:
    print("Sexta-Feira")
elif numsemana==6:
    print("Sábado")
elif numsemana==7:
    print("Domingo")
else:
    print("Opção inválida")