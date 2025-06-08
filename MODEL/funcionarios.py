import mysql.connector
from MODEL.conexaoDB import conectar
from tkinter import messagebox
class Funcionarios:
    def __init__(self):
        pass 
    

    #Checa se o login e senha são valídos
    def confirmar_login(self, login, senha):
        conexao = None
        cursor = None
        try:
            conexao = conectar()
            cursor = conexao.cursor()
            sql = "SELECT ID FROM Funcionarios WHERE Login = %s AND Senha = %s"
            cursor.execute(sql, (login, senha))
            resultado = cursor.fetchone()
            if resultado:
                return resultado[0]  
            else:
                messagebox.showerror("Erro de Login", "Usuário ou senha inválidos.")
                return None
        except mysql.connector.Error as erro:
            messagebox.showerror("Erro no Banco de Dados", f"Erro ao verificar login:\n{erro}")
            return None
        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()


    def atualizar_dados_funcionario(self, id_funcionario, nome, login, senha, cargo):
        conexao = None
        cursor = None
        try:
            conexao = conectar()
            cursor = conexao.cursor()
            sql = """ UPDATE Funcionarios SET Nome = %s, Login = %s, Senha = %s, Cargo = %s WHERE ID = %s """
            cursor.execute(sql, (nome, login, senha, cargo, id_funcionario))
            conexao.commit()

            if cursor.rowcount == 0:
                messagebox.showwarning("Não encontrado", "Funcionário com o ID informado não foi encontrado.")
                return False
            return True

        except mysql.connector.Error as erro:
            messagebox.showerror("Erro ao atualizar", f"Erro ao atualizar dados do funcionário:\n{erro}")
            return False
        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()


    def buscarFuncionarioPorID(self,id_funcionario):
        conexao = conectar()
        if not conexao:
            messagebox.showerror("Erro", "Não foi possível conectar ao banco de dados.")
            return None

        cursor = None
        try:
            cursor = conexao.cursor()
            sql = "SELECT Nome, Login, Senha, Cargo FROM Funcionarios WHERE ID = %s"
            cursor.execute(sql, (id_funcionario,))
            resultado = cursor.fetchone()
            return resultado if resultado else None
        except mysql.connector.Error as erro:
            messagebox.showerror("Erro no Banco de Dados", f"Erro ao buscar funcionário:\n{erro}")
            return None
        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()


    def excluir_funcionario(self, funcionario_id):
        conexao = None
        cursor = None
        try:
            conexao = conectar()
            cursor = conexao.cursor()

            confirmar = messagebox.askyesno("Confirmar Exclusão", "Tem certeza que deseja excluir esta conta?")
            if not confirmar:
                return

            cursor.execute("DELETE FROM Funcionarios WHERE ID = %s", (funcionario_id,))
            conexao.commit()

            if cursor.rowcount == 0:
                messagebox.showwarning("Não encontrado", "Funcionário com o ID informado não foi encontrado.")
            else:
                messagebox.showinfo("Sucesso", "Funcionário excluído com sucesso!")

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao excluir funcionário: {str(e)}")
        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()

        
    def adicionar_funcionario(self, nome, login, senha, cargo):
        conexao = None
        cursor = None

        try:
            conexao = conectar()
            cursor = conexao.cursor()
            sql = "INSERT INTO Funcionarios (Nome, Login, Senha, Cargo) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (nome, login, senha, cargo))
            conexao.commit()
            messagebox.showinfo("Sucesso", "Funcionário adicionado com sucesso!")

        except mysql.connector.Error as erro:
            if erro.errno == 1062:
                messagebox.showerror("Login já cadastrado", "Este login já está registrado no sistema.")
            else:
                messagebox.showerror("Erro no Banco de Dados", f"Erro ao adicionar funcionário: {erro}")

        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()



