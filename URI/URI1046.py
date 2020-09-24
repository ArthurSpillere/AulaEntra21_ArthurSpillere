#Entrada da hora de início e término do jogo
i, f = map(int, input().split())

#Verificação das horas jogadas (min 1h, max 24h)

if i == f:
    print ("O JOGO DUROU 24 HORA(S)")

else:
    if f - i < 0:
        horas = 24 + (f - i)
    
    else:
        horas = f - i
    print(f"O JOGO DUROU {horas} HORA(S)")
