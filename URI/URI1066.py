valores = []
pos = 0
neg = 0
par = 0
imp = 0

#Entrada
for i in range(5):
    valores.append(int(input()))

#Varre a lista para classificar os valores em positivos, negativos,
#pares e ímpares
for j in valores:
    if j > 0:
        pos += 1
    
    elif j < 0:
        neg += 1
    
    if j % 2 == 0:
        par += 1
    
    elif j % 2 != 0:
        imp += 1

print(f"""{par} valor(es) par(es)
{imp} valor(es) impar(es)
{pos} valor(es) positivo(s)
{neg} valor(es) negativo(s)""")
