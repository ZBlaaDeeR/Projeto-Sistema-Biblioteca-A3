from MODEL.emprestimos import Emprestimos
from tkinter import messagebox 

class EmprestimoController:
    def __init__(self):
        pass

    def atualizar_emprestimo(self, IDlivro, IDmembro, dataemprestimo,prazo,devolvido,IDemprestimo):
        emprestimo = Emprestimos(IDlivro, IDmembro,dataemprestimo,prazo,devolvido,IDemprestimo)
        return emprestimo.atualizar_Emprestimo()

    def obter_detalhes_emprestimo(self, IDemprestimo, IDlivro, IDmembro):
        emprestimo = Emprestimos()
        return emprestimo.buscarDetalhesEmprestimo(IDemprestimo, IDlivro, IDmembro)
  
    def pesquisarEmprestimo(self,termo):
        emprestimo = Emprestimos()
        return emprestimo.buscarEmprestimo(termo)

    def excluirEmprestimo(self,emprestimoID):
        emprestimo = Emprestimos()
        emprestimo.excluir_emprestimo(emprestimoID)

    def devolucaoemprestimo(self,IDemprestimo,DataDevolucao):
        emprestimo = Emprestimos()
        emprestimo.registrar_devolucao(IDemprestimo,DataDevolucao)

    def exibirLivros(self):
        emprestimo = Emprestimos()
        return emprestimo.exibir_emprestimos()

    def cadastraremprestimo(self,TituloLivro,CPFMembro,DataEmprestimo,PrazoDevolução):
        emprestimo = Emprestimos(TituloLivro,CPFMembro,DataEmprestimo,PrazoDevolução)
        emprestimo.adicionar_Emprestimos()

    # Métodos que precisam setar atributos antes de chamar o método no model
    def buscarIDlivro(self, titulo_livro):
        emprestimo = Emprestimos()
        emprestimo.TituloLivro = titulo_livro
        return emprestimo.buscarIDlivro()
    
    def buscarIDmembro(self, cpf_membro):
        emprestimo = Emprestimos()
        emprestimo.CPFMembro = cpf_membro
        return emprestimo.buscarIDmembro()
    
    def buscarTituloPorIDlivro(self, id_livro):
        emprestimo = Emprestimos()
        try:
            return emprestimo.buscarTituloPorIDlivro(id_livro)
        except AttributeError:
            messagebox.showerror("Erro", "Método buscarTituloPorIDlivro não implementado no model.")
            return None

    def buscarCPFPorIDmembro(self, id_membro):
        emprestimo = Emprestimos()
        try:
            return emprestimo.buscarCPFPorIDmembro(id_membro)
        except AttributeError:
            messagebox.showerror("Erro", "Método buscarCPFPorIDmembro não implementado no model.")
            return None