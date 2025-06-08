import mysql.connector
from tkinter import messagebox
from MODEL.conexaoDB import conectar

class Livro:
    def __init__(self, titulo=None, autor=None, editora=None, categoria=None, anoPublicado=None):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.categoria =categoria
        self.anoPublicado = anoPublicado

    #Seleciona todos os livros é exibe eles
    def exibir_livros(self):
        conexao = None
        cursor = None
        try:
            conexao = conectar()
            cursor = conexao.cursor()
            cursor.execute("SELECT ID, Titulo, Autor, Editora, Categoria, AnoPublicado,Disponibilidade FROM Livros")
            return cursor.fetchall()
        except Exception as erro:
            messagebox.showerror("Error no Banco de Dados",f"Erro ao tentar buscar livros: {erro}")
            return []
        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()
        


    #Função que vai adicionar o Livro ao banco de dados
    def adicionar_livro(self):

        conexao = None
        cursor = None
        try:
            conexao = conectar()
            cursor = conexao.cursor()
            #Codigo MySQL que será enviado ao banco com as informações
            sql = "INSERT INTO Livros (Titulo,Autor,Editora,Categoria,AnoPublicado) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (self.titulo,self.autor,self.editora,self.categoria,self.anoPublicado))
            conexao.commit()

            messagebox.showinfo("Sucesso","Livro Adicionado com Sucesso")
        except mysql.connector.Error as erro:
            messagebox.showerror("Error no Banco de Dados ",f"Erro ao adicionar livro: {erro}")
        finally:
            #Fechando as conexões para evitar conflitos
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()

    def excluir_livro(self, livro_id):
        conexao = None
        cursor = None
        try:
            conexao = conectar()
            cursor = conexao.cursor()
            # Verifica se o livro tem empréstimos 
            cursor.execute("SELECT COUNT(*) FROM Emprestimos WHERE IDlivro = %s", (livro_id,))
            resultado = cursor.fetchone()

            if resultado[0] > 0:
                # Se houver empréstimos, pergunta ao usuário se deseja excluir mesmo assim
                confirmar = messagebox.askyesno("Livro com empréstimos","Este livro possui empréstimos registrados.\nDeseja excluir mesmo assim? (Os empréstimos também serão removidos)")
                if not confirmar:
                    return  

                # Codigo sql para excluir os empréstimos vinculados
                cursor.execute("DELETE FROM Emprestimos WHERE IDlivro = %s", (livro_id,))
                conexao.commit()

            # Codigo sql para excluir o livro
            cursor.execute("DELETE FROM Livros WHERE ID = %s", (livro_id,))
            conexao.commit()
            messagebox.showinfo("Sucesso", "Livro excluído com sucesso!")

        except mysql.connector.Error as erro:
            messagebox.showerror("Erro ao excluir livro", f"{erro}")
        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()



    def buscarLivro(self, termo):
        conexao = None
        cursor = None
        try:
            conexao = conectar()
            cursor = conexao.cursor()
            sql = "SELECT ID, Titulo, Autor, Editora, Categoria, AnoPublicado, Disponibilidade FROM Livros WHERE Titulo LIKE %s"
            cursor.execute(sql, (termo + '%',)) 
            return cursor.fetchall()
        except mysql.connector.Error as erro:
            messagebox.showerror("Erro no Banco de dados",f"Erro ao buscar livros: {erro}")
            return []
        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()



    def buscarLivroPorID(self, id_livro):
        conexao = conectar()
        if not conexao:
            messagebox.showerror("Erro", "Não foi possível conectar ao banco de dados.")
            return None

        cursor = None
        try:
            cursor = conexao.cursor()
            sql = "SELECT Titulo, Autor, Editora, Categoria, AnoPublicado FROM Livros WHERE ID = %s"
            cursor.execute(sql, (id_livro,))
            resultado = cursor.fetchone()
            return resultado if resultado else None
        except mysql.connector.Error as erro:
            messagebox.showerror("Erro no Banco de Dados", f"Erro ao buscar livro:\n{erro}")
            return None
        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()

    def atualizarLivro(self, id_livro, titulo, autor, editora, categoria, ano_publicado):
        conexao = None
        cursor = None
        try:
            conexao = conectar()
            cursor = conexao.cursor()
            sql = """
                UPDATE Livros
                SET Titulo = %s, Autor = %s, Editora = %s, Categoria = %s, AnoPublicado = %s
                WHERE ID = %s
            """
            cursor.execute(sql, (titulo, autor, editora, categoria, ano_publicado, id_livro))
            conexao.commit()

            if cursor.rowcount == 0:
                messagebox.showwarning("Não encontrado", "Livro com o ID informado não foi encontrado.")
                return False
            return True

        except mysql.connector.Error as erro:
            messagebox.showerror("Erro ao atualizar", f"Erro ao atualizar dados do livro:\n{erro}")
            return False
        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()


