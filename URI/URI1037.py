x = float(input())
if 0 <= x <= 25:
    print(f'Intervalo [0,25]')
elif 25< x <= 50:
    print(f'Intervalo (25,50]')
elif 50 < x <= 75:
    print(f'Intervalo (50,75]')
elif 75 < x <= 100:
    print(f'Intervalo (75,100]')
else:
    print(f'Fora de intervalo')
