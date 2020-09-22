a, b, c = input().split()
a, b, c = float(a), float(b), float(c)

delta = (b**2 - (4 * a * c))**(1/2)
if delta < 0 or a == 0:
    print("Impossivel calcular")
else:
    raiz1 = (-b + delta)/(2*a)
    raiz2 = (-b - delta)/(2*a)
    print(f"{raiz1:.5f}")
    print(f"{raiz2:.5f}")
