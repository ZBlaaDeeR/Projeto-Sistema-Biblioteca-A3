from MODEL.funcionarios import Funcionarios

class Funcionarioscontroller:
    def __init__(self):
        pass

    def atualizarDadosFuncionario(self,IDfuncionario,nome, login, senha, cargo):
        funcionarios = Funcionarios()
        return funcionarios.atualizar_dados_funcionario(IDfuncionario,nome, login, senha, cargo)
    
    def adicionarFuncionario(self, nome, login, senha, cargo):
        funcionarios = Funcionarios()
        return funcionarios.adicionar_funcionario( nome, login, senha, cargo)
    
    def excluirFuncionario(self,IDfuncionario):
        funcionarios = Funcionarios()
        return funcionarios.excluir_funcionario(IDfuncionario)

    def exibirDadosFuncionario(self,IDfuncionario):
        funcionarios = Funcionarios()
        return funcionarios.buscarFuncionarioPorID(IDfuncionario)

    def VerificarCredenciais(self,Login,Senha):
        funcionarios = Funcionarios()
        return funcionarios.confirmar_login(Login,Senha)