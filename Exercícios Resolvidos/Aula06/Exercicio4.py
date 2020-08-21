# """Execicios 04
# Exercicio retirado do site <https://wiki.python.org.br/EstruturaDeDecisao>

# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:

# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;

# Triângulo Equilátero: três lados iguais;

# Triângulo Isósceles: quaisquer dois lados iguais;

# Triângulo Escaleno: três lados diferentes;
# """

l1=int(input("Insira o valor do lado 1 do triangulo: "))
l2=int(input("Insira o valor do lado 2 do triangulo: "))
l3=int(input("Insira o valor do lado 3 do triangulo: "))

if l1<(l2+l3) and l2<(l1+l3) and l3<(l1+l2):

    if l1==l2==l3:

        print("É um triângulo equilátero!")

    elif l1==l2 or l1==l3 or l2==l3:

        print("É um triângulo isóceles!")

    else:

        print("É um triângulo Escaleno!")

else:

     print("Não é um triângulo!")

