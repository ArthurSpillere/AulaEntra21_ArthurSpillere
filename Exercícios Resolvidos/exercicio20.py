#  Exercicio 20
# Usando a seguinte fórmula:
# 
# valor_receber = dinheiro_emprestado*(1+(taxa_juros/100))**tempo_emprestimo
# 
# Crie um programa que solicite ao usuário o valor do dinheiro emprestado, 
# a taxa de juros em porcentagem e o tempo do empréstimo.
# 
# Mostre na telas o valor do dinheiro emprestado, a taxa de juros em porcentagem, 
# tempo do empréstimo e o valor que deve ser devolvido no final do empréstimo.

dinheiro_emprestado=float(input('Insira o valor do empréstimo: '))
taxa_juros=float(input('Insira a taxa de juros(%): '))
tempo_emprestimo=int(input('Insira o tempo do pagamento do empréstimo: '))

valor_receber=dinheiro_emprestado*(1+(taxa_juros/100))**tempo_emprestimo

print(f"""
O valor emprestado foi de: R${dinheiro_emprestado} com uma taxa de juros de {taxa_juros}%
O tempo de retorno do empréstimo é de {tempo_emprestimo}meses
O valor total a receber no final do empréstimo é de R${valor_receber:.2f}.""")
