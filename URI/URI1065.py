valores = []
par = 0

#Entrada
for i in range(5):
    valores.append(int(input()))

for j in valores:
    if j % 2 == 0 :
        par += 1

print(f"{par} valores pares")
