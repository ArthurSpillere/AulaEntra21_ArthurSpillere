#--- Exercício 4  - Funções
#--- Crie uma função que imprima um cabeçalho de acordo com uma variável de nome da empresa (passada por parametro)
#--- A impressão deve ocorrer via multiplicação de strings
#--- A multiplicação deve ser feita com base em uma variável que contenha o caracter a ser multiplicado
#--- Crie uma segunda função que imprima um rodapé utilizando a mesma técnica
#--- Crie uma chamada para as duas função, para exibir o resultado no console


def cabecalho(empresa, caracter = "="):
    total_carcter = int((50 - len(empresa)) / 2)

    return f"{caracter*total_carcter}{empresa}{caracter*total_carcter}\n\n"

def rodape(empresa, caracter = "-"):
    total_carcter = int((50 - len(empresa)) / 2)
    return f"\n\n{caracter*total_carcter}{empresa}{caracter*total_carcter}"

emp = input("Insira o nome da empresa para inserir ao cabeçalho:\n")

print(cabecalho(emp))

print("Lorem ipsum dolor sit amet,\n"
      "consectetur adipiscing elit, sed do eiusmod\n"
      "tempor incididunt ut labore et dolore magna\n"
      "aliqua. Ut enim ad minim\n"
      "veniam, quis nostrud exercitation ullamco\n"
      "laboris nisi ut aliquip ex\n"
      "ea commodo consequat. Duis aute irure dolor")

print(rodape(emp, "*"))

