# Exercicio 10
# Faça um programa que peça 3 números inteiros e mostre o os tês em ordem decrescente.
# 
#jeito simples que da certo até para números iguais.
valor1=int(input("Insira um primeiro valor: "))
valor2=int(input("Insira um segundo valor: "))
valor3=int(input("Insira um terceiro valor: "))

 
print('Os números escolhidos foram:',valor1,'-',valor2,'-',valor3)

if valor1<valor2:
    troca_pos=valor1
    valor1=valor2
    valor2=troca_pos

if valor2<valor3:
    troca_pos=valor3
    valor3=valor2
    valor2=troca_pos

if valor1<valor2:
    troca_pos=valor1
    valor1=valor2
    valor2=troca_pos

print(f'Os números em ordem decrescente são: {valor1}>{valor2}>{valor3}')