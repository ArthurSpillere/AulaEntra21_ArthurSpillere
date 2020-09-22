total = float(input())
total+=0.001
notas100 = total // 100
total = total % 100
notas50 = total // 50
total = total % 50
notas20 = total // 20
total = total % 20
notas10 = total //10
total = total % 10
notas5 = total // 5
total = total % 5
notas2 = total // 2
total = total % 2

moeda100 = total // 1
total = (total % 1) * 100
moeda50 = total // 50
total = total % 50
moeda25 = total // 25
total = total % 25
moeda10 = total // 10
total = total % 10
moeda5 = total // 5
total = total % 5
moeda1 = total // 1

print("NOTAS:")
print(f"{int(notas100)} nota(s) de R$ 100.00")
print(f"{int(notas50)} nota(s) de R$ 50.00")
print(f"{int(notas20)} nota(s) de R$ 20.00")
print(f"{int(notas10)} nota(s) de R$ 10.00")
print(f"{int(notas5)} nota(s) de R$ 5.00")
print(f"{int(notas2)} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{int(moeda100)} moeda(s) de R$ 1.00")
print(f"{int(moeda50)} moeda(s) de R$ 0.50")
print(f"{int(moeda25)} moeda(s) de R$ 0.25")
print(f"{int(moeda10)} moeda(s) de R$ 0.10")
print(f"{int(moeda5)} moeda(s) de R$ 0.05")
print(f"{int(moeda1)} moeda(s) de R$ 0.01")
