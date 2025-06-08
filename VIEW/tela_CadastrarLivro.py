   #Importando bibliotecas
from tkinter import ttk   #Importa o módulo ttk, que é o Toolkit Temático do Tkinter.
import tkinter as tk      #Importa o módulo inteiro tkinter com um apelido (tk).
from PIL import Image, ImageTk # usada para abrir, editar, redimensionar e exibir imagens no Python.
from tkinter import messagebox
from CONTROLLER.controllerLivro import LivroController

class tela_CadastrarLivro:
     def __init__(self,root_ref,IDfuncionario=None):
          # Recebe a janela principal
          self.root_ref = root_ref
          self.IDfuncionario = IDfuncionario

          

          # Cria uma nova janela secundária
          self.janelaCadastroLivro = tk.Toplevel()
          self.janelaCadastroLivro.title("Cadastrar Livros")
          largura = 1024
          altura = 768
        
          #Posicionamento do programa(Ao inicia-lo)
          largura_tela = self.janelaCadastroLivro.winfo_screenwidth()
          altura_tela = self.janelaCadastroLivro.winfo_screenheight()
          x = (largura_tela - largura) // 2
          y = (altura_tela - altura) // 2
          self.janelaCadastroLivro.geometry(f"{largura}x{altura}+{x}+{y}")
          
         
          #Criando o atributo imagem e convertendo ele para tk.
          self.imagem = Image.open(r"C:\Users\allan\OneDrive\Área de Trabalho\atualizeiraid\Projeto Biblioteca\VIEW\imagens\imagembiblioteca.png")
          self.imagem = self.imagem.resize((1024,768)) 
          self.imagem_tk = ImageTk.PhotoImage(self.imagem)

          #Cria a label que será responsavel por exibir e manipular a imagem na janela.
          self.label_imagem = tk.Label(self.janelaCadastroLivro, image=self.imagem_tk)
          self.label_imagem.place(x=0, y=0,relwidth=1, relheight=1)

          #Frame
          self.frame = tk.Frame(self.janelaCadastroLivro, width=720, height=420)
          self.frame.place(x=152,y=180)
          self.frame2 = tk.Frame(self.janelaCadastroLivro, width=300, height=50)
          self.frame2.place(x=363,y=65)
          
         #Formatação campos de texto
          self._formatando = False  
          self.var_Categoria = tk.StringVar()
          self.var_Categoria.trace_add("write", self.formatarCategoria)
          self.var_Ano = tk.StringVar()
          self.var_Ano.trace_add("write", self.formatarAno)

         #Botões
          self.b_Voltar = tk.Button( self.frame,text='VOLTAR',width=12,height=2,command=self.onClose,relief="raised", overrelief="ridge",bg="light blue",fg="black")
          self.b_Voltar.place(x=20,y=360)
          self.b_Salvar = tk.Button( self.frame,text='SALVAR',width=12,height=2,command=self.SalvarLivro,relief="raised", overrelief="ridge",bg="light blue",fg="black")
          self.b_Salvar.place(x=570,y=360)


          # Texto estático
          label_textoTitulo = tk.Label(self.frame, text="Digite o Titulo do livro: ", font=("Arial", 14))
          label_textoTitulo.place(x=20,y=60)
          label_textoAutor = tk.Label(self.frame, text="Autor do livro: ", font=("Arial", 14))
          label_textoAutor.place(x=20,y=120)
          label_textoEditora = tk.Label(self.frame, text="Editora do livro: ", font=("Arial", 14))
          label_textoEditora.place(x=20,y=180)
          label_textoCategoria = tk.Label(self.frame, text="Categoria do livro: ", font=("Arial", 14))
          label_textoCategoria.place(x=20,y=240)
          label_textoAno = tk.Label(self.frame, text="Ano publicado: ", font=("Arial", 14))
          label_textoAno.place(x=20,y=300)

          label_textoCadastar = tk.Label(self.frame2, text="Cadastrar Novo Livro", font=("Arial", 14))
          label_textoCadastar.place(x=56,y=13)



         #Campos de texto
          self.campo_Titulo = tk.Entry(self.frame,width=40, font=("Arial", 14))
          self.campo_Titulo.place(x=220,y=60)
          self.campo_Autor = tk.Entry(self.frame,width=40, font=("Arial", 14))
          self.campo_Autor.place(x=220,y=120)
          self.campo_Editora = tk.Entry(self.frame,width=40, font=("Arial", 14))
          self.campo_Editora.place(x=220,y=180)
          self.campo_Categoria = tk.Entry(self.frame,width=40, font=("Arial", 14),textvariable=self.var_Categoria)
          self.campo_Categoria.place(x=220,y=240)
          self.campo_AnoPublicado = tk.Entry(self.frame,width=40, font=("Arial", 14),textvariable=self.var_Ano)
          self.campo_AnoPublicado.place(x=220,y=300)

          #Codigo para impedir manipulação da tela
          self.janelaCadastroLivro.resizable(False, False)
     

      #Função responsavel pela formatação do campoYear
     def formatarAno(self, *args):
         valor = self.var_Ano.get()

         # Filtra apenas os números
         somente_numeros = ''.join(filter(str.isdigit, valor))

         # Limita a 4 dígitos
         if len(somente_numeros) > 4:
            somente_numeros = somente_numeros[:4]

         # Atualiza o campo se necessário
         if valor != somente_numeros:
            self.var_Ano.set(somente_numeros)

      #Função responsavel pela formatação do campoNome
     def formatarCategoria(self, *args):
          if self._formatando:
               return

          valor = self.var_Categoria.get()

          # Remove tudo que nao for letra ou espaço
          valor_filtrado = ''.join([c for c in valor if c.isalpha() or c.isspace()])

          # Remove espaços multplos seguidos
          valor_formatado = ' '.join(valor_filtrado.split())

          self._formatando = True
          self.var_Categoria.set(valor_formatado)
          self._formatando = False


     def SalvarLivro(self):
         titulo = self.campo_Titulo.get().strip()
         autor = self.campo_Autor.get().strip()
         editora = self.campo_Editora.get().strip()
         categoria = self.campo_Categoria.get().strip()
         anopublicado = self.campo_AnoPublicado.get().strip()
         livro = LivroController()


         if not titulo or not autor or not categoria or not anopublicado:
               messagebox.showwarning("Campos Obrigatórios", "Preencha todos os campos antes de Adicionar o Livro.")
               return
         
         if not livro.verificarAnoPublicado(anopublicado):
            messagebox.showwarning("Ano Inválido", "Informe um ano válido, que não seja maior que o ano atual.")
            return

         livro.cadastrarLivro(titulo,autor,editora,categoria,anopublicado)

     def onClose(self):
        self.janelaCadastroLivro.destroy()
        self.root_ref.deiconify()


