dinheiro = int(input())
print(dinheiro)
notas100 = dinheiro // 100
print(f"{notas100} nota(s) de R$ 100,00")
dinheiro = dinheiro % 100
notas50 = dinheiro //50
print(f"{notas50} nota(s) de R$ 50,00")
dinheiro = dinheiro % 50
notas20 = dinheiro // 20
print(f"{notas20} nota(s) de R$ 20,00")
dinheiro = dinheiro %20
notas10 = dinheiro // 10
print(f"{notas10} nota(s) de R$ 10,00")
dinheiro = dinheiro % 10
notas5 = dinheiro // 5
print(f"{notas5} nota(s) de R$ 5,00")
dinheiro = dinheiro % 5
notas2 = dinheiro // 2
print(f"{notas2} nota(s) de R$ 2,00")
dinheiro = dinheiro % 2
notas1 = dinheiro // 1
print(f"{notas1} nota(s) de R$ 1,00")
