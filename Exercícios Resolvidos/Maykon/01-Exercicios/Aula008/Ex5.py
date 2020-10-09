#--- Exercício 5  - Funções
#--- Escreva um programa para cadastro de pessoas e endereços:
#---       o programa deve solicitar os dados de pessoa utilizados na função do ex1
#---       o programa deve solicitar os dados de endereços utilizados na função do ex2
#---       o programa deve passar o id obtido na função do ex1 para a função do ex2
#---       o programa deve mostrar ao final os dados de todos as pessoas cadastradas 
#---       com seus respectivos endereços utilizando as funções do ex3 e ex4


#Importa as funções e variáveis dos exercícios anteriores
from Ex1 import cadastrar, lista_cadastro
from Ex2 import endereco, lista_enderecos
from Ex3 import procurar_cadastro, listar_cadastros
from Ex4 import procurar_endereco, listar_enderecos

#Cria um loop para múltiplos cadastros
while True:

    #Entrada de dados
    print(f"{'Novo cadastro':=^50}")
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    idade = int(input("Idade: "))
    
    #Valida a entrada de dados e faz cadastro se estiver tudo correto
    if cadastrar(nome, sobrenome, idade) == False:
        continue

    id_pessoal = len(lista_cadastro) #cria um ID baseado nº de pessoas cadastradas

    #Cria loop no cadastro de endereço para não precisar voltar ao começo caso haja erro aqui
    while True:
        print("Dados do Endereço (favor preencher TODOS os campos!")
        rua = input("Rua: ")
        numero = int(input("Núemro: "))
        complemento = input("Complemento: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        
        #Valida a entrada de dados e faz cadastro se estiver tudo correto
        if (endereco(id_pessoal, rua, numero, complemento, bairro,
            cidade, estado) == False):
            continue
        break

    #Cria loop para validar entrada correta ao cadastrar outras pessoas
    while True:
                
        resp = input("Gostaria de adicionar"
                     "outra pessoa?[S/N]").upper().strip()[0]
        
        if resp in "SsNn" and resp != "":
            break
        
    if resp not in "Ss" and resp != "":
        break

#Executa funções para listar todas as pessaos cadastradas e mostra separadamente
print(f"\n{'Pessoas Cadastradas por ordem de ID!':=^50}\n")
listar_cadastros(lista_cadastro)

print(f"\n{'Endereços Cadastradas por ordem de ID!':=^50}\n")
listar_enderecos(lista_enderecos)

#Executa funções para listar todas as pessaos cadastradas e mostra cadastro e endereço juntos
for i in range(id_pessoal):
    procurar_cadastro(lista_cadastro, i)
    procurar_endereco(lista_enderecos, i)

# Listas testes
# lista_cadastro = [{'Nome': 'Arthur', 'Sobrenome': "Cordeiro", "Idade": 27}, {'Nome': 'Ana', 'Sobrenome': "Maria", "Idade": 40}]
# lista_enderecos = [{'Rua': "Dos bobos", "Número": 0, "Complemento": "Vazio", "Bairro": "Nobre", "Cidade": "Pobre", "Estado": "Inexistente"}, {'Rua': "Amadeu", "Número": 120, "Complemento": "Cheio", "Bairro": "Nobritude", "Cidade": "Rico", "Estado": "Existe"}]
