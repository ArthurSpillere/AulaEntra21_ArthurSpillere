# Exercicio 3
# Faça um programa que peça a idade do cliente.
# 
# Se ele tiver 18 anos ou mais deve aparecer a mensagem "Entrada permitida"
# 
# Caso contrário deve aparecer a mensagem "Entrada Negada!"

idade=int(input("Informe a idade do cliente: "))
permissao=idade>=18

if permissao==True:
    print("Entrada Permitida!")
else:
    print("Entrada Negada!")
