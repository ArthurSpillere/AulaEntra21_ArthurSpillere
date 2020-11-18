import sqlite3

def cadastro_no_banco_veiculo(cadastro):
    conn = sqlite3.connect("Cadastro_veiculo.db")
    cursor = conn.cursor()

    try:
        cursor.executemany("""
            INSERT INTO Cadastro_veiculo(marca, nome, modelo, placa,
            proprietario, cor, km_rodado, qte_passageiros, motor,
            combustivel, meio_locomocao)
            VALUES(?,?,?,?,?,?,?,?,?,?,?) 
            """, cadastro)

        conn.commit()
        
        print("Cadastro efetuado com sucesso!")

    except Exception as ex:
        conn.rollback()
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
    # except:
    #     conn.rollback()
    #     raise RuntimeError("Algo deu errado!")

    conn.close()


def cadastro_no_banco_pessoa(cadastro):
    conn = sqlite3.connect("Cadastro_pessoa.db")
    cursor = conn.cursor()

    try:
        cursor.executemany("""
            INSERT INTO Cadastro_pessoa(marca, nome, modelo, placa,
            proprietario, cor, km_rodado, qte_passageiros, motor,
            combustivel, meio_locomocao)
            VALUES(?,?,?,?,?,?,?,?,?,?,?) 
            """, cadastro)

        conn.commit()
        
        print("Cadastro efetuado com sucesso!")

    except Exception as ex:
        conn.rollback()
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
    # except:
    #     conn.rollback()
    #     raise RuntimeError("Algo deu errado!")

    conn.close()
    

def criar_tabela_veiculo(): 
    conn = sqlite3.connect("Cadastro_veiculo.db")
    cursor = conn.cursor()

    try:
        cursor.execute("""
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
            """)

        print("Tabela criada com sucesso!")
        
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
        print("Tabela já criada neste banco de dados! Para alterações, "
            "use o UPDATE!")
    
    conn.close()
    
    
def criar_tabela_pessoa(): 
    conn = sqlite3.connect("Cadastro_pessoa.db")
    cursor = conn.cursor()

    try:
        cursor.execute("""
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
                nacionalidade TEXT NOT NULL
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
    conn = sqlite3.connect('Cadastro_veiculo.db')
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

    conn.close()
    
    conn = sqlite3.connect('Cadastro_pessoa.db')
    cursor = conn.cursor()

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
    conn = sqlite3.connect('Cadastro_veiculo.db')
    cursor = conn.cursor()

    lista = cursor.execute("""PRAGMA table_info(Cadastro_veiculo)""")
    
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
    cursor.execute("""
    UPDATE clientes
    SET ? = ?,
    WHERE id = ?
    """, (campo_atualizar, atualizacao, id_cliente))

    
def update_pessoa():
    pass


    
# def deletar_no_banco_pessoa(): 
#     conn = sqlite3.connect('Cadastro_pessoa.db')
#     cursor = conn.cursor()

#     try:
#         id_cliente = int(input("Qual id você gostaria de deletar?"))

#         # excluindo um registro da tabela
#         cursor.execute("""
#         DELETE FROM Cadastro_pessoa
#         WHERE id = ?
#         """, (id_cliente,))

#         conn.commit()

#         print('Registro excluido com sucesso.')
    
#     except Exception as ex:
#         conn.rollback()
#         template = "An exception of type {0} occurred. Arguments:\n{1!r}"
#         message = template.format(type(ex).__name__, ex.args)
#         print(message)

#     conn.close()





update_veiculo()