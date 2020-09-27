leds = {'1': 2, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6, '7': 3, '8': 7,
        '9': 6, '0': 6}
        
repeticoes = int(input())

for j in range(repeticoes):
    num = input()
    soma = 0
    for i in num:
        soma += leds[i]
        
    print(f"{soma} leds")
