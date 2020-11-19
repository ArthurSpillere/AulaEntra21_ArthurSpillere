#marca, nome, modelo, placa, proprietario, cor, km_rodado, qte_passageiros,
#motor, combustivel, meio_locomocao.

# from func_banco import 

class Veiculo():
    def __init__(self, marca, nome, modelo, placa, proprietario, cor, km_rodado,
                 qte_passageiros, motor, combustivel, meio_locomocao, valor):
        
        self.marca = marca
        self.nome = nome
        self.modelo = modelo
        self.placa = placa
        self.proprietario = proprietario
        self.cor = cor
        self.km_rodado = km_rodado
        self.qte_passageiros = qte_passageiros
        self.motor = motor
        self.combustivel = combustivel
        self.meio_locomocao = meio_locomocao
        self.valor = valor
        
        
    def __str__(self):
        pass
    
    
class Pessoa():
    def __init__(self, nome, data_nascimento, cpf, endereco, salario, profissao,
                 telefone, nome_responsavel, sexo, naturalidade,
                 nacionalidade):
        
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
        self.salario = salario
        self.profissao = profissao
        self.telefone = telefone
        self.nome_responsavel = nome_responsavel
        self.sexo = sexo
        self.naturalidade = naturalidade
        self.nacionalidade = nacionalidade  
        
           
    def __str__(self):
        pass    
    
    
def main():
    
    criar_tabela_veiculo()
    
    carro = Veiculo("Volkswagen", "Gol", "Hatch", "ABC-1234", "Arthur",
                    "Branca", 13500, 5, 1.6, "Flex", "Terrestre", 13500)
    
    cadastro = (carro.marca, carro.nome, carro.modelo, carro.placa,
                carro.proprietario, carro.cor, carro.km_rodado,
                carro.qte_passageiros, carro.motor, carro.combustivel,
                carro.meio_locomocao, carro.valor)
    
    # cadastro_no_banco_veiculo(cadastro)
    
    update_veiculo()
    

if __name__ == "__main__":
    main()
    
    