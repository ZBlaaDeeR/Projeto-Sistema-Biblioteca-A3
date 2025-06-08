import mysql.connector
from MODEL.conexaoDB import conectar
from tkinter import messagebox
from datetime import datetime


class Emprestimos:
    def __init__(self,TituloLivro=None,CPFMembro=None,DataEmprestimo=None,PrazoDevolução=None,DataDevolucao=None,ID=None):
        self.IDemprestimo = ID
        self.TituloLivro = TituloLivro
        self.CPFMembro =CPFMembro
        self.DataEmprestimo = DataEmprestimo
        self.PrazoDevolucao = PrazoDevolução
        self.DataDevolucao = DataDevolucao

    #Seleciona todos os emprestimos é exibe eles
    def exibir_emprestimos(self):
        conexao = None
        cursor = None
        try:
            conexao = conectar()
            cursor = conexao.cursor()
            cursor.execute("SELECT  ID, IDlivro, IDmembro, DataEmprestimo, PrazoDevolucao, DataDevolucao, Situacao FROM Emprestimos")
            return cursor.fetchall()
        except Exception as erro:
            messagebox.showerror("Error no Banco de Dados",f"Erro ao tentar buscar emprestimos: {erro}")
            return []
        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()
        

    #Busca o ID da tabela livro
    def buscarIDlivro(self):
        conexao = None
        cursor = None
        try:
            conexao = conectar()
            cursor = conexao.cursor()
            cursor.execute("SELECT ID FROM Livros WHERE Titulo = %s", (self .TituloLivro,))
            resultado = cursor.fetchone()
            if resultado:
                return resultado[0]
            else:
                messagebox.showwarning("Livro não encontrado", "Nenhum livro com esse título foi encontrado! ")
                return None
        except mysql.connector.Error as erro:
             messagebox.showerror("Erro no Banco de Dados", f"Erro ao buscar ID do livro:\n{erro}")
             return None
        finally:
            if cursor:
                 cursor.close()
            if conexao:
                 conexao.close()

    #Busca o Id da tabela membro
    def buscarIDmembro(self):
        conexao = None
        cursor = None
        try:
            conexao = conectar()
            cursor = conexao.cursor()
            cursor.execute("SELECT ID FROM Membros WHERE CPF = %s", (self.CPFMembro,))
            resultado = cursor.fetchone()
            if resultado:
                return resultado[0]
            else:
                messagebox.showwarning("Membro não encontrado", "Nenhum Membro com esse CPF foi encontrado!")
                return None
        except mysql.connector.Error as erro:
            messagebox.showerror("Erro no Banco de Dados", f"Erro ao buscar ID do membro:\n{erro}")
            return None
        except mysql.connector.Error as erro:
                messagebox.showerror("Erro no Banco de Dados",f"Erro ao buscar ID do membro: {erro}")
                return None
        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()
    
    #Função que vai adicionar o Livro ao banco de dados
    def adicionar_Emprestimos(self):

        conexao = None
        cursor = None

        IDlivro = self.buscarIDlivro()
        IDmembro = self.buscarIDmembro()

        if IDlivro is None:
             return
        if IDmembro is None:
            return


        try:
            conexao = conectar()
            cursor = conexao.cursor()

            #Verifica se o livro na tabela está Disponivel
            cursor.execute("SELECT Disponibilidade FROM Livros WHERE ID = %s", (IDlivro,))
            resultado = cursor.fetchone()

            disponibilidade = resultado[0]

            if disponibilidade != "Disponível":
                messagebox.showerror("Livro Indisponível", "Este livro não está disponível para empréstimo.")
                return

            #Codigo MySQL que será enviado ao banco com as informações
            sql = "INSERT INTO Emprestimos (IDlivro,IDmembro,DataEmprestimo,PrazoDevolucao) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (IDlivro,IDmembro,self.DataEmprestimo,self.PrazoDevolucao))

            #Codigo que MySQL que mudara a Disponibilidade do Livro
            sql_update = "UPDATE Livros SET Disponibilidade = 'Emprestado' WHERE ID = %s"
            cursor.execute(sql_update, (IDlivro,))


            conexao.commit()
            messagebox.showinfo("Sucesso", "Empréstimo adicionado com sucesso!")

        except mysql.connector.Error as erro:
            messagebox.showerror("Erro no Empréstimo", f"Erro ao adicionar empréstimo:\n{erro}")
        finally:
            #Fechando as conexões para evitar conflitos
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()

    #Função da devolução do livro
    def registrar_devolucao(self, IDemprestimo, DataDevolucao):
        conexao = None
        cursor = None

        try:
            conexao = conectar()
            cursor = conexao.cursor()

            cursor.execute("""SELECT IDlivro, Situacao FROM Emprestimos WHERE ID = %s""", (IDemprestimo,))
            resultado = cursor.fetchone()

            if not resultado:
                messagebox.showerror("Erro", "Empréstimo não encontrado.")
                return

            IDlivro, situacao = resultado

            if situacao == "Entregue":
                messagebox.showinfo("Aviso", "Este empréstimo já foi finalizado.")
                return

            # Atualiza o empréstimo com a nova data de devolução e define como 'Entregue'
            cursor.execute("""
                UPDATE Emprestimos SET DataDevolucao = %s, Situacao = 'Entregue' WHERE ID = %s""", (DataDevolucao, IDemprestimo))

            # Torna o livro disponível novamente
            cursor.execute("""UPDATE Livros SET Disponibilidade = 'Disponível' WHERE ID = %s""", (IDlivro,))

            conexao.commit()
            messagebox.showinfo("Sucesso", "Devolução registrada com sucesso!")

        except mysql.connector.Error as erro:
            messagebox.showerror("Erro no Banco de Dados", f"Erro ao registrar devolução:\n{erro}")
        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()

    def excluir_emprestimo(self, id_emprestimo):
        conexao = None
        cursor = None
        try:
            conexao = conectar()
            cursor = conexao.cursor()

            # Exclui o empréstimo
            cursor.execute("DELETE FROM Emprestimos WHERE ID = %s", (id_emprestimo,))
            conexao.commit()

            messagebox.showinfo("Sucesso", "Empréstimo excluído com sucesso!")

        except mysql.connector.Error as erro:
            messagebox.showerror("Erro ao excluir empréstimo", f"{erro}")
        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()

    def buscarEmprestimo(self, cpf):
        conexao = None
        cursor = None
        try:
            conexao = conectar()
            cursor = conexao.cursor()

            sql = """ SELECT E.ID, E.IDlivro, E.IDmembro, E.DataEmprestimo, E.PrazoDevolucao, E.DataDevolucao, E.Situacao FROM Emprestimos E JOIN Membros M ON E.IDmembro = M.ID WHERE M.CPF LIKE %s"""
            cursor.execute(sql, (cpf + '%',))  # Busca por CPF começando com o termo
            return cursor.fetchall()

        except mysql.connector.Error as erro:
            messagebox.showerror("Erro no Banco de dados",f"Erro ao buscar empréstimos: {erro}")
            return []
        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()        

    def formatar_data(self,data):
        if data is None:
            return None
        return data.strftime("%d%m%Y")



    def buscarDetalhesEmprestimo(self, IDemprestimo, IDlivro, IDmembro):
        conexao = None
        cursor = None
        try:
            conexao = conectar()
            cursor = conexao.cursor(dictionary=True)

            # Consulta as datas do empréstimo pela IDemprestimo
            sql_datas = """SELECT DataEmprestimo, PrazoDevolucao, DataDevolucao FROM Emprestimos WHERE ID = %s"""
            cursor.execute(sql_datas, (IDemprestimo,))
            datas = cursor.fetchone()

            # Consulta o título do livro pela IDlivro
            sql_titulo = "SELECT Titulo FROM Livros WHERE ID = %s"
            cursor.execute(sql_titulo, (IDlivro,))
            livro = cursor.fetchone()

            # Consulta o CPF do membro pela IDmembro
            sql_cpf = "SELECT CPF FROM Membros WHERE ID = %s"
            cursor.execute(sql_cpf, (IDmembro,))
            membro = cursor.fetchone()

            if not datas or not livro or not membro:
                return None  # Algum dado não foi encontrado

            return {
                "Titulo": livro["Titulo"],
                "CPF": membro["CPF"],
                "DataEmprestimo": self.formatar_data(datas["DataEmprestimo"]),
                "PrazoDevolucao": self.formatar_data(datas["PrazoDevolucao"]),
                "DataDevolucao": self.formatar_data(datas["DataDevolucao"])
            }

        except mysql.connector.Error as erro:
            messagebox.showerror("Erro no Banco de dados", f"Erro ao buscar detalhes do empréstimo: {erro}")
            return None
        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()


    def atualizar_Emprestimo(self):
        try:
            con = conectar()
            cur = con.cursor()

            # 1) Buscar ID do livro pelo título
            cur.execute("SELECT ID FROM Livros WHERE Titulo = %s", (self.TituloLivro,))
            resultado_livro = cur.fetchone()
            if not resultado_livro:
                messagebox.showwarning("Aviso", "Livro não encontrado.")
                return
            idLivro = resultado_livro[0]

            # 2) Buscar ID do membro pelo CPF
            cur.execute("SELECT ID FROM Membros WHERE CPF = %s", (self.CPFMembro,))
            resultado_membro = cur.fetchone()
            if not resultado_membro:
                messagebox.showwarning("Aviso", "Membro não encontrado.")
                return
            idMembro = resultado_membro[0]

            # 3) Executar UPDATE na tabela Emprestimos
            cur.execute(
                "UPDATE Emprestimos SET IDlivro = %s, IDmembro = %s, DataEmprestimo = %s, PrazoDevolucao = %s, DataDevolucao = %s "
                "WHERE ID = %s",
                (idLivro, idMembro, self.DataEmprestimo, self.PrazoDevolucao,self.DataDevolucao ,self.IDemprestimo)
            )
            con.commit()  # Confirma as alterações no banco de dados

            messagebox.showinfo("Sucesso", "Empréstimo atualizado com sucesso.")
        except mysql.connector.Error as e:
            messagebox.showerror("Erro", f"Erro ao atualizar empréstimo: {e}")
        finally:
            con.close()
