#--- Exercício 1  - Variáveis
#--- Crie 5 variáveis para armazenar os dados de um funcionário
#--- Funcionario: Nome, Sobrenome, Cpf, Rg, Salário
#--- Deve ser usado apenas uma vez a função print()
#--- Cada dado deve ser impresso em uma linha diferente
#--- O salário deve ser de tipo flutuante

cadastro_usuario = {'Nome': 'Arthur', 'Sobrenome': 'Cordeiro',
                    'CPF': '999.999.999-99', 'RG': '99999-9','Salário': 3000.25
                    }

for chave, valor in cadastro_usuario.items():
    print("O {}: {}".format(chave, valor))
