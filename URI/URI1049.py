#Recebe as palavras para definir resultado
a = input().lower()
b = input().lower()
c = input().lower()

# #Verifica qual o animal corresponde à entrada dada

# if a == 'vertebrado':
#     if b == 'ave':
#         if c == 'carnivoro':
#             print('aguia')
#         elif c == 'onivoro':
#             print('pomba')
    
#     elif b == 'mamifero':
#         if c == 'onivoro':
#             print('homem')
#         elif c == 'herbivoro':
#             print('vaca')

# elif a == 'invertebrado':
#     if b == 'inseto':
#         if c == 'hematofago':
#             print('pulga')
#         elif c == 'herbivoro':
#             print('lagarta')
    
#     elif b == 'anelideo':
#         if c == 'hematofago':
#             print('sanguessuga')
#         elif c == "onivoro":
#             print('minhoca')

#############################################

#Resolvendo por dicionários

resultado = {'vertebrado': {'ave': {'carnivoro': 'aguia', 'onivoro': 'pomba'},
            'mamifero': {'onivoro': 'homem', 'herbivoro': 'vaca'}},
            'invertebrado': {'inseto': {'hematofago': 'pulga',
             'herbivoro': 'lagarta'}, 'anelideo': {'hematofago': 'sanguessuga',
             'onivoro': 'minhoca'}}}

print(resultado[a][b][c])