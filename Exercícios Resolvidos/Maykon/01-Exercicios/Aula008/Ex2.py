#--- Exercício 2  - Funções
#--- Escreva uma função para cadastro de endereço:
#---       a função deve receber sete parâmetros, id da pessoa, rua, numero, complemento, bairro, cidade e estado
#---       a função deve salvar os dados de endereço em uma lista com escopo global
#---       a função deve permitir o cadastro apenas de endereços com todos os dados preenchidos
#---       a função deve retornar uma mensagem ao final de acordo com a situação
#--- A função deve ser salva em um arquivo diferente do arquivo principal onde será chamada

lista_enderecos = []

def endereco(id_pessoal:int, rua:str, numero:int, complemento:str, bairro:str,
             cidade:str, estado:str)->str:

    if (rua == "" or rua ==  None or numero < 0 or numero == None or
        complemento == "" or complemento == None or cidade == "" or
        cidade == None or estado == "" or estado == None):

        print("Algum dado foi digitado errado. Favor tentar novamente!")
        return False
    else:
        endereco_pessoa = {}
        endereco_pessoa["Rua"] = rua
        endereco_pessoa["Número"] = numero
        endereco_pessoa["Complemento"] = complemento
        endereco_pessoa["Bairro"] = bairro
        endereco_pessoa["Cidade"] = cidade
        endereco_pessoa["Estado"] = estado
        endereco_pessoa["ID"] = id_pessoal
        lista_enderecos.append(endereco_pessoa)

        return print("Cadastro efetuado com sucesso!")
        
