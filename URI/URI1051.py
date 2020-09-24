#Valor máximo do salário para cada faixa de imposto
faixa_imposto = [4500, 3000, 2000, 0]
imposto = [28, 18, 8, 0] #em %
imp_pagar = 0

salario = round(float(input()),2)

for i,j in enumerate(faixa_imposto):
    if salario - j > 0:
        imp_pagar+= (salario - j) * (imposto[i]/100)
        salario=j
        
        if imp_pagar == 0:
            print('Isento')

        elif i == len(faixa_imposto) - 1:
            print(f'R$ {imp_pagar:.2f}')
