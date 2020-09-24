#Recebe DDD
ddd=str(input())
cont=0
dic_ddd = {'61': 'Brasilia', '71': 'Salvador', '11': 'Sao Paulo',
 '21': 'Rio de Janeiro', '32': 'Juiz de Fora', '19': 'Campinas',
 '27': 'Vitoria', '31': 'Belo Horizonte'}

#Verifica se DDD está na lista

for i in dic_ddd:
    if ddd == i:
        print(dic_ddd[i])
        cont+=1
        break

if cont==0:
    print('DDD nao cadastrado')
