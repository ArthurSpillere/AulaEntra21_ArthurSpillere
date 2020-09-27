# #COM LIB

# from math import gcd
# #Entrada
# #Recebe quantidade de testes a fazer
# casos = int(input())

# for i in range(casos):
#     #Separa os termos do teste imputado
#     N1, ignora1, D1, sinal, N2, ignora2, D2 = input().split()

#     N1 = int(N1)
#     D1 = int(D1)
#     N2 = int(N2)
#     D2 = int(D2)

#     #Verifica a operação que será realizada no teste e resolve o teste
#     if sinal == '+':
#         numerador = (N1 * D2 + N2 * D1)
#         denominador = (D1 * D2)
        
#     elif sinal == '-':
#         numerador = (N1 * D2 - N2 * D1)
#         denominador = (D1 * D2)
#     elif sinal == '*':
#         numerador = (N1 * N2)
#         denominador = (D1 * D2)
#     elif sinal == '/':
#         numerador = (N1 * D2)
#         denominador = (N2 * D1)

#     #Verifica se é possível simplificar
#     simplificador = gcd (numerador, denominador)
#     if simplificador > 1:
#         numerador_simp = int(numerador / simplificador)
#         denominador_simp = int(denominador / simplificador)

#     else:
#         numerador_simp = numerador
#         denominador_simp = denominador

#     print(f"{numerador}/{denominador} = {numerador_simp}/{denominador_simp}")
# #######################################################

# #Sem Lib

# #Entrada
# #Recebe quantidade de testes a fazer
casos = int(input())

for i in range(casos):
    #Separa os termos do teste imputado
    N1, ignora1, D1, sinal, N2, ignora2, D2 = input().split()

    N1 = int(N1)
    D1 = int(D1)
    N2 = int(N2)
    D2 = int(D2)

    #Verifica a operação que será realizada no teste e resolve o teste
    if sinal == '+':
        numerador = (N1 * D2 + N2 * D1)
        denominador = (D1 * D2)

    elif sinal == '-':
        numerador = (N1 * D2 - N2 * D1)
        denominador = (D1 * D2)
    elif sinal == '*':
        numerador = (N1 * N2)
        denominador = (D1 * D2)
    elif sinal == '/':
        numerador = (N1 * D2)
        denominador = (N2 * D1)

    #Verifica se é possível simplificar
    b = denominador
    a = numerador
    while (b != 0):
        r = a % b
        a = b
        b = r
    
    print(f"{numerador}/{denominador}",
          f"= {int((numerador / a))}/{int((denominador / a))}")
