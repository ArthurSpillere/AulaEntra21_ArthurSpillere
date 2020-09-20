# 3) Estas 3 listas:
# 
# vendas_armando = [100.00, 500.00, 258.50, 710.00, 50.50,750.00 ]
# vendas_eduardo = [10.00, 1050.00, 859.75, 199.05, 500.50,750.00, 568.60, 950.00 ]
# vendas_paulo = [950.00, 89.90, 2500.00, 1750.00,500.00]
# 
# Estas listas são referente as vendas dos vendedores Armando, Paulo e Eduardo.
# 
# 3.1) Com base nelas e usando funções da lista mostradas em aula, mostre:
# A média de vendas de cada um;
# A venda total de cada vendedor;
# A quantidade de vendas de cada vendedor.
# 
# 3.2) Calcule o valor de comissão que o dono da loja deve pagar para seus funcionários seguindo a regra:
# 
# Para total de vendas de 0.00 a 1000.00 Reais - 1%
# Para total de vendas de 1000.01 a 2500.00 Reais - 1.5%
# Para total de vendas de 2500.01 a 5000.00 Reais - 2%
# Para total de vendas a cima de 5000.01 Reais - 3%
# 


vendas_armando = [100.00, 500.00, 258.50, 710.00, 50.50,750.00 ]
vendas_eduardo = [10.00, 1050.00, 859.75, 199.05, 500.50,750.00, 568.60, 950.00 ]
vendas_paulo =   [950.00, 89.90, 2500.00, 1750.00,500.00]

media_armando=sum(vendas_armando)/len(vendas_armando)
media_eduardo=sum(vendas_eduardo)/len(vendas_eduardo)
media_paulo=sum(vendas_paulo)/len(vendas_paulo)
if 0<sum(vendas_armando)<=1000:
    comissao_armando=1
elif 1000<sum(vendas_armando)<=2500:
    comissao_armando=1.5 
elif 2500<sum(vendas_armando)<=5000:
    comissao_armando=2
elif sum(vendas_armando)>5000:
    comissao_armando=3
else:
    comissao_armando=0

total_armando=sum(vendas_armando)
total_eduardo=sum(vendas_eduardo)
total_paulo=sum(vendas_paulo)

if 0<sum(vendas_eduardo)<=1000:
    comissao_eduardo=1
elif 1000<sum(vendas_eduardo)<=2500:
    comissao_eduardo=1.5 
elif 2500<sum(vendas_eduardo)<=5000:
    comissao_eduardo=2
elif sum(vendas_eduardo)>5000:
    comissao_eduardo=3
else:
    comissao_eduardo=0

qtde_vendas_armando=len(vendas_armando)
qtde_vendas_eduardo=len(vendas_eduardo)
qtde_vendas_paulo=len(vendas_paulo)

if 0<sum(vendas_paulo)<=1000:
    comissao_paulo=1
elif 1000<sum(vendas_paulo)<=2500:
    comissao_paulo=1.5 
elif 2500<sum(vendas_paulo)<=5000:
    comissao_paulo=2
elif sum(vendas_paulo)>5000:
    comissao_paulo=3
else:
    comissao_paulo=0

print(f"""
Resumo Armando:
Total das vendas R${total_armando:.2f}
Média das vendas R${media_armando:.2f}
Total de {qtde_vendas_armando} itens vendidos.
Sua comissão total será de {comissao_armando}%, recebendo R${total_armando*comissao_armando/100:.2f}
 
Resumo Eduardo:
Total das vendas R${total_eduardo:.2f}
Média das vendas R${media_eduardo:.2f}
Total de {qtde_vendas_eduardo} itens vendidos.
Sua comissão total será de {comissao_eduardo}%, recebendo R${total_eduardo*comissao_eduardo/100:.2f}

Resumo Paulo:
Total das vendas R${total_paulo:.2f}
Média das vendas R${media_paulo:.2f}
Total de {qtde_vendas_paulo} itens vendidos.
Sua comissão total será de {comissao_paulo}%, recebendo R${total_paulo*comissao_paulo/100:.2f}""")



