
"""Exercicio 03

Faça um programa que peça 10 notas do aluno. Faça a média e mostre as seguintes mensagens:

Para 7 a 10 - Aprovado
Para 5.5 a 7 - Recuperação 
Para menor de 5.5 - Reprovado
"""
lista=[]
nota=-1
for i in range(1,11):

    # lista.append(float(input(f"Insira a nota {i}: "))) #Cria lista automática sem restrição de valor

    while not 0<=nota<=10: #Adiciona nota na lista com restrição de valor
        
        nota=float(input(f"Insira a nota {i}: "))

        if not 0<=nota<=10: #Mensagem opcional para inserção de valor inválido
            print("\033[1;31mVocê inseriu uma nota inválida! Tente novamente.\033[m")
    

    lista.append(nota)
    nota=-1


soma=sum(lista)
media=(soma/i)
if 7<=media<=10:
    print(f"Sua média foi de {media:.2f}")
    print("Parabéns! Você foi Aprovado!")

elif 5.5<=media<7:
    print(f"Sua média foi de {media:.2f}")
    print("Você ficou em recuperção! Estude bem para a prova final.")

else:
    print(f"Sua média foi de {media:.2f}")
    print("Você foi reprovado. Estude mais na próxima vez.")

