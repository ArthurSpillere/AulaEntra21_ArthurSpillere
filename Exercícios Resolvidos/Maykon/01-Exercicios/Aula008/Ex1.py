#--- Exercício 1  - Funções
#--- Escreva uma função para cadastro de pessoa:
#---       a função deve receber três parâmetros, nome, sobrenome e idade
#---       a função deve salvar os dados da pessoa em uma lista com escopo global
#---       a função deve permitir o cadastro apenas de pessoas com idade igual ou superior a 18 anos
#---       a função deve retornar uma mensagem caso a idade informada seja menor que 18
#---       caso a pessoa tenha sido cadastrada com sucesso deve ser retornado um id 
#--- A função deve ser salva em um arquivo diferente do arquivo principal onde será chamada

lista_cadastro = []

def cadastrar(nome:str, sobrenome:str, idade:int)->str:
    if (nome == "" or nome == None or sobrenome == "" or sobrenome == None or
        idade == "" or idade == None or not isinstance(idade, int)):
        print("Entrada de dados inválida! Tente novamente!")
        return False

    if idade >= 18:
        pessoa = {}
        pessoa['Nome'] = nome
        pessoa['Sobrenome'] = sobrenome
        pessoa['idade'] = idade
        pessoa['ID'] = len(lista_cadastro) + 1

        lista_cadastro.append(pessoa)

        return print("Pessoa cadastrada com sucesso!")

    else:
        print("Não é possível cadastrar menor de 18 anos.")
        return False

