# Exercicio 17
# A formula de calculo de área de um circulo é:
# 
# area = pi*r²
# 
# Sabemos que:
# 
# pi = 3.14
# r = raio da circunferência em metros (float)
# 
# Crie um programa que peça ao usuário o raio e calcule a área da circunferência
# 
raio=float(input('Insira o raio de um circulo em cm: '))
pi=float(3.14)
area=pi*raio**2

print(f'A aréa do círculo é de {area}cm²')
