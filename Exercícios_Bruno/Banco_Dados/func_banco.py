import sqlite3
from veiculos import Pessoa, Veiculo

def cadastro_nos_bancos(cadastro):
    conn = sqlite3.connect("Cadastro_Geral.db")
    cursor = conn.cursor()
    
    
    try:
        cursor.execute("""
            INSERT INTO Cadastro_veiculo(marca, nome, modelo, placa,
            proprietario, cor, km_rodado, qte_passageiros, motor,
            combustivel, meio_locomocao, valor)
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?) 
            """, cadastro[0])

        conn.commit()
        
        print("Cadastro efetuado com sucesso!")

    except Exception as ex:
        conn.rollback()
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
    
    try:
        cursor.execute("""
            INSERT INTO Cadastro_pessoa(nome, data_nascimento, cpf, endereco,
            salario, profissao, telefone, nome_responsavel, sexo,
            naturalidade, nacionalidade, veiculo_id)
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?) 
            """, cadastro[1])
        
    except Exception as ex:
        conn.rollback()
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
        
    conn.commit()
    
        
    cursor.execute("""
        SELECT * FROM Cadastro_pessoa INNER JOIN Cadastro_veiculo ON Cadastro_pessoa.veiculo_id = Cadastro_veiculo.id
        """)
    
    print(cursor.fetchall())
    
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


def deletar_nos_bancos(): 
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


def update_veiculo():
    conn = sqlite3.connect('Cadastro_Geral.db')
    cursor = conn.cursor()

    escolha = int(input("Você gostaria de atualizar\n\n [1] Pessoa\n\n"
                        "[2] Veículo?\n\n"))
    
    if escolha == 1:
        lista = cursor.execute("""PRAGMA table_info(Cadastro_pessoa)""")
        print("Você optou por alterar cadastro em um veículo.")
        
    elif escolha == 2:
        lista = cursor.execute("""PRAGMA table_info(Cadastro_veiculo)""")
        print("Você optou por alterar cadastro em um veículo.")
    
    opcoes = []
    
    for opcao in lista:
        opcoes.append(opcao[1])

    for num, opcao in enumerate(opcoes):
        if num != 0:
            print(f"[{num}] - {opcao}")
    
    opc = int(input("\nInsira uma opção para atualizar:\n"))
    
    campo_atualizar = opcoes[opc]
    
    id_cliente = int(input("\nInsira o id que você deseja alterar:\n"))
    
    atualizacao = input(f"Insira a nova informação para atualizar o "
                        f"campo {campo_atualizar}")
    
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


def atualiza_informacoes(id_veiculos, nome, modelo, ano, placa, proprietario, num_portas, qtd_passageiros, motor, meio_locomocao):

    cursor.execute("""

    UPDATE veiculos

    SET nome = ?, modelo = ?, ano = ?, placa = ?,proprietario = ?, num_portas = ?, qtd_passageiros = ?, motor = ?, 

    meio_locomocao = ?

    # WHERE id = ?

    """, (nome, modelo, ano, placa, proprietario, num_portas, qtd_passageiros, motor, meio_locomocao,id_veiculos))

    conn.commit()


# atualiza_informacoes(1,"Siena", "Sedan", "2017", "ABC-1234", "Amanda","4", "2", "1.0", "Carro")

# conn.close()


    
carro = Veiculo("Volkswagen", "Gol", "Hatch", "ABC-1234", "Arthur",
                "Branca", 13500, 5, 1.6, "Flex", "Terrestre", 13500)

cadastro1 = (carro.marca, carro.nome, carro.modelo, carro.placa,
            carro.proprietario, carro.cor, carro.km_rodado,
            carro.qte_passageiros, carro.motor, carro.combustivel,
            carro.meio_locomocao, carro.valor)

pessoa = Pessoa("Arthur", "25/12/1900", 33322211156, "Rua dos bobos 0",
                50000, "Desempregado", 47999871523, "Mamãe", "Masculino",
                "Blumenauense", "Brasileiro")

cadastro2 = (pessoa.nome, pessoa.data_nascimento, pessoa.cpf, pessoa.endereco,
             pessoa.salario, pessoa.profissao, pessoa.telefone,
             pessoa.nome_responsavel, pessoa.sexo, pessoa.naturalidade,
             pessoa.nacionalidade, 1)

cadastro = [cadastro1, cadastro2]

cadastro_nos_bancos(cadastro)

pessoa = Pessoa("Maria", "25/12/1900", 33322211156, "Rua dos bobos 0",
                50000, "Desempregado", 47999871523, "Mamãe", "Masculino",
                "Blumenauense", "Brasileiro")

carro = Veiculo("Ford", "Fiesta", "Hatch", "ABC-1234", "Arthur",
                "Branca", 13500, 5, 1.6, "Flex", "Terrestre", 13500)

cadastro1 = (carro.marca, carro.nome, carro.modelo, carro.placa,
            carro.proprietario, carro.cor, carro.km_rodado,
            carro.qte_passageiros, carro.motor, carro.combustivel,
            carro.meio_locomocao, carro.valor)


cadastro2 = (pessoa.nome, pessoa.data_nascimento, pessoa.cpf, pessoa.endereco,
             pessoa.salario, pessoa.profissao, pessoa.telefone,
             pessoa.nome_responsavel, pessoa.sexo, pessoa.naturalidade,
             pessoa.nacionalidade, 2)

cadastro = [cadastro1, cadastro2]

cadastro_nos_bancos(cadastro)

deletar_nos_bancos()