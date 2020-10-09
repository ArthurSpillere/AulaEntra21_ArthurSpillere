
#--- Exercício 3  - Variáveis
#--- Imprima dois parágrafos do último livro que você leu
#--- A impressão deve conter informações do livro, que deverão estar em variáveis
#--- As informações do Livro serão: 
#---    Título
#---    Edição
#---    Autor
#---    Data de publicação
#--- Os parágrafos devem estar formatados conforme a formatação do livro

texto = ("    Tenha um grande objetivo, saiba por que você faz o que faz,\n"
             "tenha seu principal sonho bem delineado e, no trabalho, "
             "coti-\ndiano, concentre-se apenas no próximo degrau, na próxima\n"
             "meta, no próximo estágio, na próxima grande conquista de\ncurto "
             "prazo.\n    Faça seu melhor dia após dia, sempre se concentrando"
             "na\ntarefa daquele dia. E o seu sucesso maior estará garantido.")

info_livro = {"Título": "Seja FODA!", "Edição": "Não Consta",
              "Autor": "Caio Carneiro", "Data de publicação": "2017"}

for chave, valor in info_livro.items():
    print("{}: {}".format(chave, valor))

print("\n", texto,"\n")
