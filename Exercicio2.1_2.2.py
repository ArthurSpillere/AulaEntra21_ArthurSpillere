#Exercício 2.1
#n = 42 #Funciona
#42 = n #Não funciona - SyntaxError: cannot assign to literal
#
#x = y = 1 #Atribui o valor um para x e y. Funciona
#
#print("oi"); #Usar o ';' não impede a execução do programa

#print("oi"). #Usar o '.' impede a execução do programa - SyntaxError: invalid syntax

# escrever 'xy' para tentar uma multiplicação resultará em erro, pois o programa
# vai ler 'xy' como uma variável ainda não declarada. - NameError:name 'xy' is not defined

# Exercício 2.2

#1) 
R=5
volume = (4.0/3.0)*3.141596*R**3
print(f"{volume:.2f}")

#2)
preco_livro = 24.95
transp1 = 3
transp2 = 0.75
num = 60
desconto = (1 - 0.4)
total = num*preco_livro*desconto + transp1 + transp2 * (num - 1)
print(f"{total:.2f}")

#3
inicio = 6 * 60 + 52 #transforma tudo em minutos
rota1 = 8 + 15 / 60 
rota2 = 3 * (7 + 12 / 60)
rota3 = 8 + 15 / 60
final = inicio + rota1 + rota2 + rota3
chegada_hora = final // 60
chegada_minutos = final % 60
print(f"{int(chegada_hora)}:{int(chegada_minutos)}")