#Recebe total de testes a fazer
rep = int(input())

for casos in range(rep):    
    #Recebe informação da dieta, café e almoço
    dieta = input()
    dieta2 = sorted(list(dieta))
    cafe = input()
    almoco = input()
    total = (cafe + almoco)
    total2 = sorted(list(total))
    janta = ''
    cheater = 0
    #Verifica se é "CHEATER"
    for j, i in enumerate(total):
        if j != len(total)-1:
            if total[j] == total[j+1]: #Verifica se há letras repetidas
                print("CHEATER")
                cheater = 1
                break

        if dieta.find(i) == -1: #Verifica se há letra fora da lista da dieta
            print("CHEATER")
            cheater = 1
            break

    #Verifica quais itens falta comer na janta
    for a, b in enumerate(dieta2):
        comeu = total.find(b)

        if comeu == -1:
            janta += dieta2[a]
            
        else:
            continue
    #Saída
    if cheater != 1:
        print(janta)
