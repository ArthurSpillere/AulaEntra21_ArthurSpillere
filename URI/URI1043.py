#recebe os valores para verificação
a, b, c = map(float, input().split())

#verifica se é triângulo
if a + b > c and a + c > b and b + c > a:
    print(f"Perimetro = {a + b + c:.1f}")
#Calcula area de um trapézio se não for triangulo
else:
    print(f"Area = {((a + b) * c)/2:.1f}")
