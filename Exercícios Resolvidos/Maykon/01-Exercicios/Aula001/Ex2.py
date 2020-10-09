#--- Exercício 2  - Variáveis
#--- Crie um menu para um sistema de cadastro de funcionários
#--- O menu deve ser impresso com a função format()
#--- As opções devem ser variáveis do tipo inteiro
#--- As descrições das opções serão:
#---    Cadastrar funcionário
#---    Listar funcionários
#---    Editar funcionário
#---    Deletar funcionário
#---    Sair
#--- Além das opções o menu deve conter um cabeçalho e um rodapé
#--- Entre o cabeçalho e o menu e entre o menu e o rodapé deverá ter espaçamento de 3 linhas
#--- Deve ser utilizado os caracteres especiais de quebra de linha e de tabulação

lista_opcoes = {'cadastro_funcinario': 1, 'listar_funcionario': 2,
                'editar_funcionario': 3, 'deletar_funcionario': 4, 'sair': 5}
a, b, c, d, e = lista_opcoes.values()
print('='*40)
print("{:^40}".format('Bem vindo ao Cadastrum Python 2.0'))
print('='*40,'\n','\n','\n')

print("""{}) Cadastrar funcionário
{}) Listar funcionários
{}) Editar funcionário
{}) Deletar funcionário
{}) Sair""".format(a, b, c, d ,e))

print('\n','\n')
print('='*40)

opcao = int(input("Digite a opção desejada (1-5):\n"))
for chave, valor in lista_opcoes.items():
    if opcao == valor:
        print("Você escolheu a opção número {}".format(valor),
            "referenta à {}".format(chave))
        break
    
if str(opcao) not in "1 2 3 4 5":
    print("Opção inválida. Tente novamente.")