#Entrada das notas do aluno
n1, n2, n3, n4 = map(float, input().split())

#Calcula a média ponderada das notas de acordo com o peso de cada nota
media = round((n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1)/10,1)
print(f"Media: {media:.1f}")

#Verifica em que categoria a média do aluno se encontra
if media >= 7.0:
    print("Aluno aprovado.")

elif media < 5.0:
    print("Aluno reprovado.")

elif 5.0 <= media < 7.0:
    print("Aluno em exame.")
    #Lê a nota de exame do aluno e recalcula sua média
    nota_exame = round(float(input()),1)
    media_nova = round((media + nota_exame)/2,1)
    print(f"Nota do exame: {nota_exame:.1f}")

    if media_nova >= 5.0: 
        print("Aluno aprovado.")
    
    elif media_nova < 5.0:
        print("Aluno reprovado.")
    
    print(f"Media final: {media_nova:.1f}")
