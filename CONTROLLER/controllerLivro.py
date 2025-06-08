from MODEL.livro import Livro
from datetime import datetime


class LivroController:
    def __init__(self):
        pass

    def atualizarDadosLivro(self, id_livro, titulo, autor, editora, categoria, ano_publicado):
        livro = Livro()
        return livro.atualizarLivro(id_livro, titulo, autor, editora, categoria, ano_publicado)


    def exibirDadosLivro(self, id_livro):
        livro = Livro()
        return livro.buscarLivroPorID(id_livro)


    def pesquisarLivro(self,termo):
        livro = Livro()
        return livro.buscarLivro(termo)

    def excluirLivro(self,livroID):
        livro = Livro()
        livro.excluir_livro(livroID)

    def exibirLivros(self):
        livro = Livro()
        return livro.exibir_livros()

    def cadastrarLivro(self, titulo, autor, editora, categoria, anoPublicado):
        livro = Livro(titulo, autor, editora, categoria, anoPublicado)
        livro.adicionar_livro()

    
    def verificarAnoPublicado(self,ano_str: str) -> bool:
        ano_str = ano_str

        if len(ano_str) != 4 or not ano_str.isdigit():
            return False

        ano = int(ano_str)
        ano_atual = datetime.now().year

        return ano <= ano_atual
    
    