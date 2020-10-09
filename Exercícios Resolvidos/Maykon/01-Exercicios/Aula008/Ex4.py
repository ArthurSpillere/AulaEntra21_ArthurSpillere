#--- Exercício 4  - Funções
#--- Escreva uma função para listar endereços cadastrados:
#---    a função deve exibir todos os endereços cadastrados na função do ex2
#--- Escreva uma função para exibir um endereço específico:
#---    a função deve exibir um endereço cadastrado na função do ex2 filtrando por 
#---    id da pessoa

def listar_enderecos(lista_enderecos):
    for endereco in lista_enderecos:
        for chave, valor in endereco.items():
            print(f"{chave}: {valor}")

        print()


def procurar_endereco(lista_enderecos, id_pessoal = -1):
    if id_pessoal == -1:
        id_pessoal = int(input("Qual id você deseja procurar?\n"))

    try:
        for chave, valor in lista_enderecos[id_pessoal-1].items():
            print(f"{chave}: {valor}")
    
    except:
        print("ID não cadastrado ou entrada inválida!")



