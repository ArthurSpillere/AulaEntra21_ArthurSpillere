# Exercicio 18
# Peça para o usuário digitar os valores de a, b e c
# 
# Calcule o delta "delta = (b**2)-(4*a*c)"
# 
# Se o delta der negativo, então deve aparecer a seguinte mensagem: "Delta negativo! Equação não pode ser resolvida!"
# 
# Se o delta der igual a zero, então deve aparecer a seguinte mensagem: "Delta igual a zero!"
# 
# Se o delta der positivo, então deve aparecer a seguinte mensagem: "A equação pode ser resolvida!"

a=int(input("Insira o valor de a: "))
b=int(input("Insira o valor de b: "))
c=int(input("Insira o valor de c: "))

delta=(b**2)-(4*a*c)

if delta<0:
    
    print("Delta negativo! Equação não pode ser resolvida!")

elif delta==0:
    
    print("Delta igual a zero!")

else:

    print("A equação pode ser resolvida!")