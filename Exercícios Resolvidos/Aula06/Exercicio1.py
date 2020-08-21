# # Execicios 01

# # Escreva um programa que calcule a porcentagem de comissão de vendedores com as seguintes condições

# Venda Total
# de R$ 0.00 a R$ 30000.00 - 0%
# de R$ 30000.01 a R$ 50000.00 - 1.5%
# de R$ 50000.01 a R$ 100000.00 - 2.5%
# Acima de R$ 100000.00 - 3.5%
# """

venda=float(input("Insira sua venda total em R$: "))

if 0<=venda<=30000:

    print("Sua comissão é de 0%! Você não receberá nada. Se esforçe mais!")

elif 30000<venda<=50000:
    
    print("Sua comissão é de 1,5%. Você receberá R$",venda*(1+1.5/100))
    print(f"Sua comissão é de 1,5%. Você receberá R${venda*(1+1.5/100):.2f}")

elif 50000<venda<=100000:

    print("Sua comissão é de 2,5%. Você receberá R$",venda*(1+2.5/100))
    print(f"Sua comissão é de 2,5%. Você receberá R${venda*(1+2.5/100):.2f}")

elif venda>=100000:

    print("Sua comissão é de 3.5%. Você receberá R$",venda*(1+3.5/100))
    print(f"Sua comissão é de 3.5%. Você receberá R${venda*(1+3.5/100):.2f}")

else:

    print("Valor inválido")