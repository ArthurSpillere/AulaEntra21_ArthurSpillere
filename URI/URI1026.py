while True:
    try:
        #Entrada dos valores
        a, b = map(int, input().split())

        resultado = ''
        bin_a = bin(a)[2:]
        bin_b = bin(b)[2:]

        while len(bin_a) != len(bin_b):
            if len(bin_a) > len(bin_b):
                bin_b = '0' + bin_b

            elif len(bin_a) < len(bin_b):
                bin_a = '0' + bin_a

        bin_a = list(bin_a[::-1])
        bin_b = list(bin_b[::-1])

        #Calcula a soma dos binários com erro no carry 
        for i, j in enumerate(bin_a):
            if j == bin_b[i]:
                resultado += '0'
            
            else:
                resultado += '1'

        #Saída
        resultado = '0b' + resultado[::-1]
        print(int(resultado, 2))

    except EOFError:
        break
