#--- Exercício 3  - Funções
#--- Escreva uma função para listar pessoas cadastradas:
#---    a função deve exibir todas as pessoas cadastradas na função do ex1
#--- Escreva uma função para exibi uma pessoa específica:
#--- a função deve exibir uma pessoa cadastrada na função do ex1 filtrando por id

def listar_cadastros(lista_cadastrada):
        for pessoa in lista_cadastrada:
                for chave, valor in pessoa.items():
                        print(f"{chave}: {valor}")
                
                print()

#A função pode receber um ID ou não para ser procurado, se não receber o mesmo
#deverá ser informado dentro dentro da função
def procurar_cadastro(lista_cadastrada, id_pessoal = -1):
        if id_pessoal == -1:
                id_pessoal = int(input("Qual id você deseja procurar?\n"))

        try:
                for chave, valor in lista_cadastrada[id_pessoal-1].items():
                        print(f"{chave}: {valor}")
                        
        except:
                print("ID não cadastrado ou entrada inválida!")

