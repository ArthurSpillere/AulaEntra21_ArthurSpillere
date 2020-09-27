N = 1
Q = 1
cont = 0
N, Q = map(int, input().split())

while not N == Q == 0:

    cont += 1
    marbles = []
    queries = []
    for i in range(N):
        marbles.append(int(input()))

    marbles = sorted(marbles)

    for j in range(Q):
        queries.append(int(input()))
    
    print(f"CASE# {cont}:")

    #Busca Binária
    for palpite in queries:
        inicio = 0
        final = (len(marbles) - 1)
        
        while inicio <= final:
            meio = int((inicio + final)/2)

            if palpite == marbles[meio]:
                while palpite == marbles[meio]:
                    meio = meio - 1
                    if meio < 0 or palpite != marbles[meio]:
                        meio = meio + 1
                        break

                break

            else:
                if palpite  < marbles[meio]:
                    final = meio - 1
                    continue
                else:
                    inicio = meio + 1
                    continue

        if inicio > final:
            print(f"{palpite} not found")

        else:
            print(f"{palpite} found at {meio+1}")
            
    
    N, Q = map(int, input().split())
