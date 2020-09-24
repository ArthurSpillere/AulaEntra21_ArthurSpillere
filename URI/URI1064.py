valores = []
soma = 0
pos = 0

#Entrada
for i in range(6):
    valores.append(float(input()))

#Procura na lista os valores positivos e soma eles para tirar a média
for j in valores:
    if j > 0:
        pos += 1
        soma += j

print(f"{pos} valores positivos")
print(f"{(soma/pos):.1f}")
