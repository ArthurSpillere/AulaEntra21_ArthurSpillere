#Entrada
rep = int(input())

for i in range(rep):
    texto2 = ''
    texto3 = ''
    texto = input()
    #Aletera todos os caracteres a-z A-Z para 3 caracteres pra frente
    for a, b in enumerate(texto):
        if ord(b) not in range(65, 90) and ord(b) not in range(97, 122):
            texto2 += texto[a]

        else:
            texto2 += texto[a].replace(chr(ord(b)), chr(ord(b) + 3))
    #Inverte a linha
    texto2 = texto2[::-1]

    tamanho = int(len(texto2)/2)
    #Muda os carecteres para 1 valor a menos a partir da metade da palavra
    for c, d in enumerate(texto2):
        if c < tamanho:
            texto3 += texto2[c]

        else:
            texto3  += texto2[c].replace(chr(ord(d)), chr(ord(d)-1))


    print(texto3)
