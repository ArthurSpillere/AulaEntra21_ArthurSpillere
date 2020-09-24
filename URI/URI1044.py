#Entrada de valores para comparação
a, b = map(int, input().split())

#Verifica se são múltiplos
if b % a == 0 or a % b == 0:
    print("Sao Multiplos")
else:
    print('Nao sao Multiplos')
