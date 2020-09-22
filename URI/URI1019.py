x = int(input())
horas = x // 3600
x = x % 3600
minutos = x // 60
x = x % 60
print(f"{horas}:{minutos}:{x}")
