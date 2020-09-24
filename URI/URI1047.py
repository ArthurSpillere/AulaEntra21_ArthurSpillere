#recebe dados de hora e minuto iniciais e finais
hi, mi, hf, mf = map(int,input().split())

#Calcula tempo jogado (minimo de 1 min e max de 24h)

if hi == hf == mi == mf:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")

else:
#Verifica-se se o tempo inicial e hora final são diferentes
    if hf == hi:
        if mi > mf:
            horas = 23
            minutos = 60 + mf - mi
        
        else:
            hora = 0
            minutos = mf - mi
        
    elif hf > hi:
        hora = hf - hi

        if mi > mf:
            minutos = 60 + mf - mi
            hora-=1

        else:
            minutos = mf - mi
    
    else:
        hora = 24 + hf - hi

        if mi > mf:
            minutos = 60 + mf - mi
            hora-=1

        else:
            minutos = mf - mi

    print(f"O JOGO DUROU {hora} HORA(S) E {minutos} MINUTO(S)")
