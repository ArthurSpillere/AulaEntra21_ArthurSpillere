a, b, c = input().split()
x, y, z = int(a), int(b), int(c)
maiorXY = (x+y+abs(x-y))/2
maior = int((maiorXY+z+abs(maiorXY-z))/2)
print(f"{maior} eh o maior")
