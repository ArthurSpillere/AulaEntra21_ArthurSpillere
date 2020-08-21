# """Execicios 02

# Escreva um programa que receba 4 notas e calcule a média.
# Mostre a seguinte mensagem conforme a media final.

# Media Final
# de 0 a 5 - Reprovado
# de 5 a 6.5 - Recuperação
# de 6.5 a 9 - Aprovado
# Acima de 9 - Aprovado com louvor
# """

nota1=float(input("Insira a primeira nota: "))
nota2=float(input("Insira a segunda nota: "))
nota3=float(input("Insira a terceira nota: "))
nota4=float(input("Insira a quarta nota: "))

media=(nota1+nota2+nota3+nota4)/4

if nota1>10 or nota2>10 or nota3>10 or nota4>10 or nota1<0 or nota2<0 or nota3<0 or nota4<0:

    print("Você digitou alguma nota errada. Corrija.")

else:

    if 0<=media<5:

        print(f"Sua média é {media:.2f}. Status: Reprovado!")

    elif 5<=media<6.5:

        print(f"Sua média é {media:.2f}. Status: Recuperação!")

    elif 6.5<=media<9:

        print(f"Sua média é {media:.2f}. Status: Aprovado!")

    else:

        print(f"Sua média é {media:.2f}. Satatus: Aprovado com Louvor!")
