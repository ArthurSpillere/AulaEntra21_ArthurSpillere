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

def linha_bloco(texto=""):
    print(f"{texto:=^40}\n")

while True:
    linha_bloco("Cadastrum Pythonicum 2.0")
    print(f"{'':^10}{'1 - Novo Cadastro':<30}")
    print(f"{'':^10}{'2 - Listar Cadastro':<30}")
    print(f"{'':^10}{'3 - Salvar Cadastros':<30}")
    print(f"{'':^10}{'4 - Importar Cadastros':<30}")
    print(f"{'':^10}{'5 - Sair':<30}\n")
    linha_bloco()
    
    while True:
        opcao = input("Escolha uma opção[1-5]:\n")
        
        if opcao not in "1 2 3 4 5" or opcao == "" or opcao == None:
            print("Opção inválida! Tente novamente.")
            linha_bloco()
            continue
        break
    
    if opcao == '1': 
        #Cria um loop para múltiplos cadastros
        while True:
            #Entrada de dados
            print(f"{'Novo cadastro':=^40}")
            nome = input("Nome: ").strip()
            sobrenome = input("Sobrenome: ").strip()
            idade = int(input("Idade: "))
            
            #Valida a entrada de dados e faz cadastro se estiver tudo correto
            if cadastrar(nome, sobrenome, idade) == False:
                continue

            id_pessoal = len(lista_cadastro) #cria um ID baseado nº de pessoas cadastradas

            #Cria loop no cadastro de endereço para não precisar voltar ao começo caso haja erro aqui
            while True:
                print("Dados do Endereço (favor preencher TODOS os campos!")
                rua = input("Rua: ").strip()
                numero = int(input("Núemro: "))
                complemento = input("Complemento: ").strip()
                bairro = input("Bairro: ").strip()
                cidade = input("Cidade: ").strip()
                estado = input("Estado: ").strip()
                
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
                print("Cadastro(s) efetuado(s) com sucesso!")
                break

    elif opcao == '2':
        while True:
            linha_bloco("Listar Cadastro")
            print(f"{'':^10}{'1 - Listar Pessoas':<30}")
            print(f"{'':^10}{'2 - Listar Endereços':<30}")
            print(f"{'':^10}{'3 - Listar Pessoas e Endereços':<30}")
            print(f"{'':^10}{'4 - Procurar pelo ID':<30}")
            print(f"{'':^10}{'5 - Sair':<30}")
            
            while True:
                opcao = input("Escolha uma opção[1-5]:\n")

                if opcao not in "1 2 3 4 5" or opcao == "" or opcao == None:
                    print("Opção inválida! Tente novamente.")
                    continue
                break
                  
            if opcao == '1':
                if len(lista_cadastro) == 0 or len(lista_enderecos) == 0:
                    linha_bloco()
                    print("Não há ninguém cadastrado!\n")
                    linha_bloco()
                    
                else:
                    linha_bloco()
                    print(f"\n{'Pessoas Cadastradas por ordem de ID!':=^40}\n")
                    listar_cadastros(lista_cadastro)
                    linha_bloco()
            
            elif opcao == '2':
                if len(lista_cadastro) == 0 or len(lista_enderecos) == 0:
                    linha_bloco()
                    print("Não há nenhum endereço cadastrado!\n")
                    linha_bloco()
                    
                else:
                    linha_bloco()
                    print(f"{'Endereços Cadastradas por ordem de ID!':=^40}\n")
                    listar_enderecos(lista_enderecos)
                    linha_bloco()

            elif opcao == '3':
                if len(lista_cadastro) == 0 or len(lista_enderecos) == 0:
                    linha_bloco()
                    print("Não há nenhum endereço cadastrado!\n")
                    linha_bloco()
                else:
                    linha_bloco()
                    print(f"{'Cadastro e Endereço por ordem de ID!':=^40}\n")
                    for i in range(len(lista_cadastro)+1):
                        procurar_cadastro(lista_cadastro, i)
                        print()
                        procurar_endereco(lista_enderecos, i)
                        linha_bloco()
            
            elif opcao == '4':
                if len(lista_cadastro) == 0  or len(lista_enderecos) == 0:
                    linha_bloco()
                    print("Não há ninguém cadastrado!\n")
                    linha_bloco()
                else:
                    linha_bloco()
                    id_pessoal = input("Qual ID você gostaria de visualizar?\n")
                    linha_bloco()
                    linha_bloco(f"ID {id_pessoal}")
                    procurar_cadastro(lista_cadastro, int(id_pessoal))
                    print()
                    procurar_endereco(lista_enderecos, int(id_pessoal))
                    linha_bloco()
                            
            elif opcao =='5':
                break
        
            while True:
                resp = input("Deseja retornar ao menu "
                             "'Listar Cadastro[S/N]'?\n").lower().strip()[0]
                
                if resp not in "sn" or resp == "" or resp == None:
                    continue
                break
            if resp == "n":
                break
    
    elif opcao == '3':
        nome_arquivo = input("Deseja salvar o cadastro com qual nome?\n")
        arquivo_cadastro_pessoal = open(nome_arquivo + '.txt','a')
        
        for pessoa in lista_cadastro:
            arquivo_cadastro_pessoal.write(f"{pessoa['Nome']}"
                                           f":{pessoa['Sobrenome']}"
                                           f":{pessoa['Idade']}"
                                           f":{pessoa['ID']}\n")
        arquivo_cadastro_pessoal.close()
        
        arquivo_cadastro_endereco = open(nome_arquivo + '_end.txt','a')
                       
        for endereco in lista_enderecos:
            arquivo_cadastro_endereco.write(f"{endereco['Rua']}"
                                            f":{endereco['Número']}"
                                            f":{endereco['Complemento']}"
                                            f":{endereco['Bairro']}"
                                            f":{endereco['Cidade']}"
                                            f":{endereco['Estado']}"
                                            f":{endereco['ID']}\n")
            
        arquivo_cadastro_endereco.close()
            
    elif opcao == '4':
        nome_arquivo = input("Qual o nome do arquivo"
                             " que você deseja importar?\n")
        
        arquivo_importado = open(nome_arquivo + '.txt','r')
        
        for linha in arquivo_importado:
            linha = linha.strip().split(':')
            print(linha)
            pessoa = {}
            pessoa['Nome'] = linha[0]
            pessoa['Sobrenome'] = linha[1]
            pessoa['Idade'] = linha[2]
            pessoa['ID'] = linha[3]
            lista_cadastro.append(pessoa)        

        arquivo_importado.close()
        
        arquivo_importado_end = open(nome_arquivo + '_end.txt','r')
        
        for linha in arquivo_importado_end:
            linha = linha.strip().split(':')
            print(linha)
            endereco_pessoa = {}
            endereco_pessoa['Rua'] = linha[0]
            endereco_pessoa['Número'] = linha[1]
            endereco_pessoa['Complemento'] = linha[2]
            endereco_pessoa['Bairro'] = linha[3]
            endereco_pessoa['Cidade'] = linha[4]
            endereco_pessoa['Estado'] = linha[5]
            endereco_pessoa['ID'] = linha[6]
            
            lista_enderecos.append(endereco_pessoa)        

        arquivo_importado.close()
        
        arquivo_cadastro_endereco = open(nome_arquivo + '_end.txt','a')
    
    elif opcao == '5':
        print()
        linha_bloco("Cadastrum Pythonicum 2.0")
        print(f"{'Obrigado por usar nossos serviços!':^40}\n")
        linha_bloco("Até Breve!")
        break

################################################################################
# Listas testes
# lista_cadastro = [{'Nome': 'Arthur', 'Sobrenome': "Cordeiro", "Idade": 27}, {'Nome': 'Ana', 'Sobrenome': "Maria", "Idade": 40}]
# lista_enderecos = [{'Rua': "Dos bobos", "Número": 0, "Complemento": "Vazio", "Bairro": "Nobre", "Cidade": "Pobre", "Estado": "Inexistente"}, {'Rua': "Amadeu", "Número": 120, "Complemento": "Cheio", "Bairro": "Nobritude", "Cidade": "Rico", "Estado": "Existe"}]
