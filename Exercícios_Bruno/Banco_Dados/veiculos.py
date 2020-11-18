#marca, nome, modelo, placa, proprietario, cor, km_rodado, qte_passageiros,
#motor, combustivel, meio_locomocao.

from func_banco import criar_tabela_pessoa, cadastro_no_banco_veiculo, criar_tabela_veiculo, deletar_no_banco

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
                 telefone, nome_de_responsavel, sexo, naturalidade,
                 nacionalidade):
        
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
        self.salario = salario
        self.profissao = profissao
        self.telefone = telefone
        self.nome_de_responsavel = nome_de_responsavel
        self.sexo = sexo
        self.naturalidade = naturalidade
        self.nacionalidade = nacionalidade  
        
           
    def __str__(self):
        pass    
    
    
def main():
    
    criar_tabela_veiculo()
    
    cadastro_no_banco()
    
    deletar_no_banco()
    
if __name__ == "__main__":
    main()