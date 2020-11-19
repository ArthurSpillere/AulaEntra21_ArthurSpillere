import sqlite3
from veiculos import Pessoa, Veiculo
import template as template

def cadastrar_no_banco():
    # template.cabecalho("Cadastro")
    # template.texto_menu("[1] Pessoa")
    # template.texto_menu("[2] Veículo")
    # template.rodape()
    
    while True:
        try:
            resp = int(input("Selecione uma opção:\n"))

            if resp not in range(1,3):
                print("Você digitou uma opção inválida. Tente novamente!")
                continue
            
            else:
                break
        
        except:
            print("Você digitou uma opção inválida. Tente novamente!")
            continue
        
    conn = sqlite3.connect("Cadastro_Geral.db")
    cursor = conn.cursor()
    
    if resp == 1:
        
        nome = input("Nome:\n")
        data_nascimento = input("Data de nascimento:\n")
        cpf = input("CPF:\n")
        endereco = input("Endereço:\n")
        salario = float(input("Salário:\n"))
        profissao = input("Profissão:\n")
        telefone = input("Telefone:\n")
        nome_responsavel = input("Nome do Responsável:\n")
        sexo = input("Sexo:\n")
        naturalidade = input("Naturalidade:\n")
        nacionalidade = input("Nacionalidade:\n")
        
        pessoa = Pessoa(nome, data_nascimento, cpf, endereco, salario,
                        profissao, telefone, nome_responsavel, sexo,
                        naturalidade, nacionalidade)
        
        
        cadastro_pessoa = (pessoa.nome, pessoa.data_nascimento, pessoa.cpf, pessoa.endereco,
             pessoa.salario, pessoa.profissao, pessoa.telefone,
             pessoa.nome_responsavel, pessoa.sexo, pessoa.naturalidade,
             pessoa.nacionalidade, 0)
        
        try:
            cursor.execute("""
                INSERT INTO Cadastro_pessoa(nome, data_nascimento, cpf, endereco,
                salario, profissao, telefone, nome_responsavel, sexo,
                naturalidade, nacionalidade, veiculo_id)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?) 
                """, cadastro_pessoa)
            
        except Exception as ex:
            conn.rollback()
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            
        conn.commit()
        
    if resp == 2:
        
        marca = input("Marca:\n")
        nome = input("Nome do carro:\n")
        modelo = input("Modelo:\n")
        placa = input("Placa:\n")
        proprietario = input("Proprietário:\n")
        cor = input("Cor:\n")
        km_rodado = input("Kilometros rodados:\n")
        qte_passageiros = input("Quantidade de lugares:\n")
        motor = input("Motor:\n")
        combustivel = input("Combustível:\n")
        meio_locomocao = input("Meio de locomoção:\n")
        valor = input("Valor:\n")
        
        carro = Veiculo(marca, nome, modelo, placa, proprietario, cor,
                        km_rodado, qte_passageiros, motor, combustivel,
                        meio_locomocao, valor)
        
        cadastro_veiculo = (carro.marca, carro.nome, carro.modelo, carro.placa,
            carro.proprietario, carro.cor, carro.km_rodado,
            carro.qte_passageiros, carro.motor, carro.combustivel,
            carro.meio_locomocao, carro.valor)
        
        try:
            cursor.execute("""
                INSERT INTO Cadastro_veiculo(marca, nome, modelo, placa,
                proprietario, cor, km_rodado, qte_passageiros, motor,
                combustivel, meio_locomocao, valor)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?) 
                """, cadastro_veiculo)

            conn.commit()
            
            print("Cadastro efetuado com sucesso!")

        except Exception as ex:
            conn.rollback()
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
    
        
    # cursor.execute("""
    #     SELECT * FROM Cadastro_pessoa INNER JOIN Cadastro_veiculo ON Cadastro_pessoa.veiculo_id = Cadastro_veiculo.id
    #     """)
    
    # print(cursor.fetchall())
    
    conn.close()


def criar_tabelas(): 
    conn = sqlite3.connect("Cadastro_Geral.db")
    cursor = conn.cursor()

    try:
        cursor.executescript("""
            CREATE TABLE Cadastro_veiculo(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                marca TEXT NOT NULL,
                nome TEXT NOT NULL,
                modelo TEXT NOT NULL,
                placa TEXT NOT NULL,
                proprietario TEXT NOT NULL,
                cor TEXT NOT NULL,
                km_rodado INTEGER,
                qte_passageiros INTEGER,
                motor INTEGER NOT NULL,
                combustivel TEXT NOT NULL,
                meio_locomocao TEXT NOT NULL,
                valor REAL NOT NULL
            );
            
            CREATE TABLE Cadastro_pessoa(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                data_nascimento TEXT NOT NULL,
                cpf VARCHAR(11) NOT NULL,
                endereco TEXT NOT NULL,
                salario REAL,
                profissao TEXT NOT NULL,
                telefone VARCHAR(11),
                nome_responsavel TEXT NOT NULL,
                sexo TEXT NOT NULL,
                naturalidade TEXT NOT NULL,
                nacionalidade TEXT NOT NULL,
                veiculo_id INTEGER,
                
                FOREIGN KEY (veiculo_id) REFERENCES Cadastro_veiculo(id)
            );
            """)

        print("Tabela criada com sucesso!")
        
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
        print("Tabela já criada neste banco de dados! Para alterações, "
            "use o UPDATE!")
    
    conn.close()


def deletar_no_banco(): 
    conn = sqlite3.connect('Cadastro_Geral.db')
    cursor = conn.cursor()

    try:
        id_cliente = int(input("Qual id você gostaria de deletar?"))

        # excluindo um registro da tabela
        cursor.execute("""
        DELETE FROM Cadastro_veiculo
        WHERE id = ?
        """, (id_cliente,))

        conn.commit()

        print('Registro excluido com sucesso.')
    
    except Exception as ex:
        conn.rollback()
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)

    try:

        # excluindo um registro da tabela
        cursor.execute("""
        DELETE FROM Cadastro_pessoa
        WHERE id = ?
        """, (id_cliente,))

        conn.commit()

        print('Registros excluidos com sucesso.')
    
    except Exception as ex:
        conn.rollback()
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)

    conn.close()


def update():
    conn = sqlite3.connect('Cadastro_Geral.db')
    cursor = conn.cursor()

    escolha = int(input("Você gostaria de atualizar?\n\n[1] Pessoa\n\n"
                        "[2] Veículo\n\n"))
    
    if escolha == 1:
        lista = cursor.execute("""PRAGMA table_info(Cadastro_pessoa)""")
        print("Você optou por alterar cadastro em uma pessoa.\n")
        
    elif escolha == 2:
        lista = cursor.execute("""PRAGMA table_info(Cadastro_veiculo)""")
        print("Você optou por alterar cadastro em um veículo.\n")
    
    opcoes = []
    
    for opcao in lista:
        opcoes.append(opcao[1])

    for num, opcao in enumerate(opcoes):
        if num != 0:
            print(f"[{num}] - {opcao}")
    
    opc = int(input("\nInsira uma opção para atualizar:\n"))
    
    campo_atualizar = opcoes[opc]
    
    id_cliente = int(input("\nInsira o id que você deseja alterar:\n"))
    
    atualizacao = input(f"\nInsira a nova informação para atualizar o campo "
                        f"{campo_atualizar}:\n")
    
    # alterando os dados da tabela
    if escolha == 1:
        cursor.execute(f"""
        UPDATE Cadastro_pessoa
        SET {campo_atualizar} = '{atualizacao}'
        WHERE id = {id_cliente}
        """)
    
    elif escolha == 2:
        cursor.execute(f"""
        UPDATE Cadastro_veiculo
        SET {campo_atualizar} = '{atualizacao}'
        WHERE id = {id_cliente}
        """)

    conn.commit()
    
    conn.close()
    

def apresentar_banco():
    conn = sqlite3.connect('Cadastro_Geral.db')
    cursor = conn.cursor()

    if True:
        lista = cursor.execute("""PRAGMA table_info(Cadastro_pessoa)""")
        
        opcoes = []
    
        for opcao in lista:
            opcoes.append(opcao[1])
        opcoes = tuple(opcoes)
            
        cursor.execute("""
        SELECT * FROM Cadastro_pessoa
        """)

        matriz = [opcoes]
        
        for linha in cursor.fetchall():
            matriz.append(linha)

        for linha in matriz:
            print()
            for x in linha:
                print(x, end = " ")
            
            
            print()
        
                        
                # for categoria in linha:
                #     print(categoria, end = " ")

            # matrix_column = [y[index - 1] for y in self.matrix_int]
        
        
    # elif escolha == 2:
    #     lista = cursor.execute("""PRAGMA table_info(Cadastro_veiculo)""")


