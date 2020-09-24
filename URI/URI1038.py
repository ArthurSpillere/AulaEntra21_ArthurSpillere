preços = [4.00, 4.50, 5.00, 2.00, 1.50]
num, qtde = input().split()
num , qtde = int(num), int(qtde)
print(f"Total: R$ {(preços[num-1]*qtde):.2f}")
