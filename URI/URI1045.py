#entrada de lados de possíveis triângulos
a, b, c = map(float, input().split())
lista = [a, b, c]
lista.sort(reverse = True)
a, b, c = lista[0], lista[1], lista[2]

#Verifica se é triângulo
if a >= b + c:
    print("NAO FORMA TRIANGULO")
#Verifica todas as possibilidades de triângulos
else:
    if a**2 == b**2 + c**2:
        print("TRIANGULO RETANGULO")
    
    if a**2 > b**2 + c**2:
        print("TRIANGULO OBTUSANGULO")
    
    if a**2 < b**2 + c**2:
         print("TRIANGULO ACUTANGULO")

    if a==b or a==c or b==c:
        
        if a==b==c:
            print("TRIANGULO EQUILATERO")

        else:
            print("TRIANGULO ISOSCELES")
