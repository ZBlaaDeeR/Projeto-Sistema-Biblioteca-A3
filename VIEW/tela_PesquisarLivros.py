 #Importando bibliotecas
from tkinter import ttk   #Importa o módulo ttk, que é o Toolkit Temático do Tkinter.
import tkinter as tk      #Importa o módulo inteiro tkinter com um apelido (tk).
from PIL import Image, ImageTk # usada para abrir, editar, redimensionar e exibir imagens no Python.
from CONTROLLER.controllerLivro import LivroController
from tkinter import messagebox
from VIEW.tela_Atualizarlivros import tela_Atualizarlivros

class tela_PesquisarLivros:
    def __init__(self,root_ref,IDfuncionario=None):
         # Recebe a janela principal
          self.root_ref = root_ref
          
          self.IDfuncionario = IDfuncionario


        # Cria uma nova janela secundária 
          self.janelaPesquisarLivros = tk.Toplevel()
          self.janelaPesquisarLivros.title("Pesquisar Livros")
          largura = 1024
          altura = 768
        
          #Posicionamento do programa(Ao inicia-lo)
          largura_tela = self.janelaPesquisarLivros.winfo_screenwidth()
          altura_tela = self.janelaPesquisarLivros.winfo_screenheight()
          x = (largura_tela - largura) // 2
          y = (altura_tela - altura) // 2
          self.janelaPesquisarLivros.geometry(f"{largura}x{altura}+{x}+{y}")
         

          #Criando o atributo imagem e convertendo ele para tk.
          self.imagem = Image.open(r"C:\Users\allan\OneDrive\Área de Trabalho\atualizeiraid\Projeto Biblioteca\VIEW\imagens\imagembiblioteca.png")
          self.imagem = self.imagem.resize((1024,768)) 
          self.imagem_tk = ImageTk.PhotoImage(self.imagem)

          #Cria a label que será responsavel por exibir e manipular a imagem na janela.
          self.label_imagem = tk.Label(self.janelaPesquisarLivros, image=self.imagem_tk)
          self.label_imagem.image = self.imagem_tk
          self.label_imagem.place(x=0, y=0,relwidth=1, relheight=1)

          
          #criando cor label
          cor1 = "#FFFFFF"
          cor2 = "#B4B4B4"

          #Frame
          self.frame = tk.Frame(self.janelaPesquisarLivros, width=868, height=580,bg=cor2)
          self.frame.place(x=79,y=94)
          self.frame2 = tk.Frame(self.janelaPesquisarLivros, width=868, height=450,bg=cor1)
          self.frame2.place(x=79,y=160)

          #Botões
          self.b_Voltar = tk.Button( self.frame,text='VOLTAR',width=12,height=2,command=self.onClose,relief="raised", overrelief="ridge",bg="light blue",fg="black")
          self.b_Voltar.place(x=25,y=530)
          self.b_Excluir = tk.Button( self.frame,text='EXCLUIR',width=12,height=2,command=self.excluirLivroSelecionado,relief="raised", overrelief="ridge",bg="red",fg="white")
          self.b_Excluir.place(x=745,y=530)
          self.b_Pesquisar = tk.Button( self.frame,text='Pesquisar',command=self.pesquisarLivros,width=8,height=2,relief="raised", overrelief="ridge",bg="light blue",fg="black")
          self.b_Pesquisar.place(x=760,y=15)

          self.b_Atualizar = tk.Button( self.frame,text='Atualizar',width=12,height=2,command=self.abrir_Atualizarlivros,relief="raised", overrelief="ridge",bg="light blue",fg="black")
          self.b_Atualizar.place(x=600,y=530)
          

          # Texto estático
          label_textoTitulo = tk.Label(self.frame, text="Pesquisar livro: ", font=("Arial", 14),bg=cor2)
          label_textoTitulo.place(x=20,y=20)


          #Campos de Pesquisa
          self.campo_Pesquisar = tk.Entry(self.frame,width=40, font=("Arial", 18))
          self.campo_Pesquisar.place(x=220,y=20)
          
          #Carregar os livros
          self.carregarLivros()

          #Codigo para impedir manipulação da tela
          self.janelaPesquisarLivros.resizable(False, False)




    #mostra os livros na tela
    def carregarLivros(self):
      # Cria o Treeview
      colunas = ("ID", "Título", "Autor", "Editora", "Categoria", "Ano","Disponibilidade")
      self.tree = ttk.Treeview(self.frame2, columns=colunas, show='headings')

      # Define os nomes das colunas
      for col in colunas:
          self.tree.heading(col, text=col)
          self.tree.column(col, width=120)

      self.tree.place(relx=0, rely=0, relwidth=1, relheight=1)

      controller = LivroController()
      livros = controller.exibirLivros()
      
      # Inserir dados na tabela
      for livro in livros:
          self.tree.insert("", "end", values=livro)

    def onClose(self): 
          self.janelaPesquisarLivros.destroy()
          self.root_ref.deiconify()

    #Pesquisar os livros de acordo com o digitado
    def pesquisarLivros(self):
      termo = self.campo_Pesquisar.get()
      controller = LivroController()
      resultados = controller.pesquisarLivro(termo)
      # Limpar a tabela antes de exibir os resultados
      for item in self.tree.get_children():
          self.tree.delete(item)

      for livro in resultados:
          self.tree.insert("", "end", values=livro)

    #Função para remover do DB o livro
    def excluirLivroSelecionado(self):
      item_selecionado = self.tree.selection()

      if not item_selecionado:
          messagebox.showwarning("Aviso", "Selecione um livro para excluir.")
          return
      # Obtem os dados da linha selecionada
      valores = self.tree.item(item_selecionado)["values"]
      livro_id = valores[0]
      confirmacao = messagebox.askyesno("Confirmar Exclusão", f"Tem certeza que deseja excluir o livro ID {livro_id}?")
     
      if confirmacao:
          controller = LivroController()
          controller.excluirLivro(livro_id)
          self.tree.delete(item_selecionado)  

    def abrir_Atualizarlivros(self):
          item_selecionado = self.tree.selection()

          if not item_selecionado:
               messagebox.showwarning("Aviso", "Selecione um livro para atualizar.")
               return

          # Pega o ID do membro selecionado (assumindo que está na primeira coluna)
          valores = self.tree.item(item_selecionado)["values"]
          IDlivro = valores[0]            
          self.janelaPesquisarLivros.withdraw()
          tela_Atualizarlivros(self.janelaPesquisarLivros,IDlivro,self.IDfuncionario)
            
          


          
          

          