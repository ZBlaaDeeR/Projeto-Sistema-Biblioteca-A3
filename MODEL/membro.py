import mysql.connector
from tkinter import messagebox
from MODEL.conexaoDB import conectar

class Membro:
    def __init__(self,Nome=None,Gmail=None,Telefone=None,CPF=None):
        self.nome = Nome
        self.gmail = Gmail
        self.telefone = Telefone
        self.CPF =CPF

    #Seleciona todos os membros é exibe eles
    def exibir_membros(self):
        conexao = None
        cursor = None
        try:
            conexao = conectar()
            cursor = conexao.cursor()
            cursor.execute("SELECT ID, Nome, Gmail, Telefone, CPF FROM Membros")
            return cursor.fetchall()
        except Exception as erro:
            messagebox.showerror("Error no Banco de Dados",f"Erro ao tentar buscar membros: {erro}")
            return []
        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()

    #Função que vai adicionar o membro ao banco de dados
    def adicionar_membro(self):

        conexao = None
        cursor = None

        try:
            conexao = conectar()
            cursor = conexao.cursor()
            #Codigo MySQL que será enviado ao banco com as informações
            sql = "INSERT INTO Membros (Nome,Gmail,Telefone,CPF) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (self.nome,self.gmail,self.telefone,self.CPF))
            conexao.commit()
            messagebox.showinfo("Sucesso","Membro adicionado com Sucesso")

        except mysql.connector.Error as erro:
            if erro.errno == 1062:
                messagebox.showerror("CPF já cadastrado", "Este CPF já está registrado no sistema.")
            else:
                messagebox.showerror("Erro no Banco de Dados", f"Erro ao adicionar membro: {erro}")
                
        finally:
            #Fechando as conexões para evitar conflitos
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()

    def atualizar_dados_membro(self, id_membro, nome, login, senha, cargo):
        conexao = None
        cursor = None
        try:
            conexao = conectar()
            cursor = conexao.cursor()
            sql = """ UPDATE Membros SET Nome = %s, Gmail = %s, Telefone = %s, CPF = %s WHERE ID = %s """
            cursor.execute(sql, (nome, login, senha, cargo, id_membro))
            conexao.commit()

            if cursor.rowcount == 0:
                messagebox.showwarning("Não encontrado", "Membro com o ID informado não foi encontrado.")
                return False
            return True

        except mysql.connector.Error as erro:
            messagebox.showerror("Erro ao atualizar", f"Erro ao atualizar dados do membro:\n{erro}")
            return False
        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()

    def excluir_membro(self, membro_id):
            conexao = None
            cursor = None
            try:
                conexao = conectar()
                cursor = conexao.cursor()
                # Verifica se o membro tem empréstimos 
                cursor.execute("SELECT COUNT(*) FROM Emprestimos WHERE IDmembro = %s", (membro_id,))
                resultado = cursor.fetchone()

                if resultado[0] > 0:
                    # Se houver empréstimos, pergunta ao usuário se deseja excluir mesmo assim
                    confirmar = messagebox.askyesno("Membro com empréstimos","Este membro possui empréstimos registrados.\nDeseja excluir mesmo assim? (Os empréstimos também serão removidos)")
                    if not confirmar:
                        return  

                    # Codigo sql para excluir os empréstimos vinculados
                    cursor.execute("DELETE FROM Emprestimos WHERE IDmembro = %s", (membro_id,))
                    conexao.commit()

                # Codigo sql para excluir o membro
                cursor.execute("DELETE FROM Membros WHERE ID = %s", (membro_id,))
                conexao.commit()
                messagebox.showinfo("Sucesso", "Membro excluído com sucesso!")

            except mysql.connector.Error as erro:
                messagebox.showerror("Erro ao excluir membro", f"{erro}")
            finally:
                if cursor:
                    cursor.close()
                if conexao:
                    conexao.close()


    def buscarMembro(self, termo):
        conexao = None
        cursor = None
        try:
            conexao = conectar()
            cursor = conexao.cursor()
            sql = "SELECT ID, Nome, Gmail, Telefone, CPF FROM Membros WHERE CPF LIKE %s"
            cursor.execute(sql, (termo + '%',)) 
            return cursor.fetchall()
        except mysql.connector.Error as erro:
            messagebox.showerror("Erro no Banco de dados",f"Erro ao buscar membros: {erro}")
            return []
        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()

    def buscarMembroPorID(self,id_membro):
        conexao = conectar()
        if not conexao:
            messagebox.showerror("Erro", "Não foi possível conectar ao banco de dados.")
            return None

        cursor = None
        try:
            cursor = conexao.cursor()
            sql = "SELECT Nome, Gmail, Telefone, CPF FROM Membros WHERE ID = %s"
            cursor.execute(sql, (id_membro,))
            resultado = cursor.fetchone()
            return resultado if resultado else None
        except mysql.connector.Error as erro:
            messagebox.showerror("Erro no Banco de Dados", f"Erro ao buscar membro:\n{erro}")
            return None
        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()

    def atualizar_dados_membro(self, id_membro, nome, gmail, telefone, cpf):
        conexao = None
        cursor = None
        try:
            conexao = conectar()
            cursor = conexao.cursor()
            sql = """
                UPDATE Membros
                SET Nome = %s, Gmail = %s, Telefone = %s, CPF = %s
                WHERE ID = %s
            """
            cursor.execute(sql, (nome, gmail, telefone, cpf, id_membro))
            conexao.commit()

            if cursor.rowcount == 0:
                messagebox.showwarning("Não encontrado", "Membro com o ID informado não foi encontrado.")
                return False
            return True

        except mysql.connector.Error as erro:
            messagebox.showerror("Erro ao atualizar", f"Erro ao atualizar dados do membro:\n{erro}")
            return False
        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()



