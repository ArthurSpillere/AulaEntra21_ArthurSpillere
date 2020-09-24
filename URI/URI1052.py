calendario = ['january', 'february', 'march', 'april', 'may', 'june',
             'july', 'august', 'september', 'october', 'november', 'december']

#Recebe número do mês
mes = int(input())

#Mostra nome correspondente ao número do mês
print(calendario[mes-1].capitalize())
