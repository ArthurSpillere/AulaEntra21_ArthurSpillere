valores = []
dentro = 0
fora = 0

#Entrada
a = int(input())

for i in range(a):
    valores.append(int(input()))


for j in valores:
    if 10 <= j <= 20:
        dentro += 1

    else:
        fora += 1

print(f"{dentro} in")
print(f"{fora} out")
