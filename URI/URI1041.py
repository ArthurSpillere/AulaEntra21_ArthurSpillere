#Entrada das coordenadas
x, y = map(float, input().split())

#Verifica onde está a coordenada no plano
if x == 0 and y == 0:
    print("Origem")

elif x == 0:
    print("Eixo Y")

elif y == 0:
    print("Eixo X")

else:
    if x > 0 and y > 0:
        print("Q1")
   
    elif x > 0 and y < 0:
        print("Q4")
    
    elif x < 0 and y < 0:
        print("Q3")
    
    else:
        print("Q2")