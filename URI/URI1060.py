valores = []
cont = 0

#Recebe valores positivos e negativos
for i in range(6):
    valores.append(float(input()))

#Mostra quantos valores positivos há na entrada informada
for j in valores:
    if j > 0:
        cont += 1
    
print(f"{cont} valores positivos")
