   #Importando bibliotecas
from tkinter import ttk   #Importa o módulo ttk, que é o Toolkit Temático do Tkinter.
import tkinter as tk      #Importa o módulo inteiro tkinter com um apelido (tk).
from PIL import Image, ImageTk # usada para abrir, editar, redimensionar e exibir imagens no Python.
from tkcalendar import DateEntry # Usada para adicionarmos um campo de calendario
from datetime import datetime #Import para facilitar a conversão de datas
from tkinter import messagebox
from CONTROLLER.controllerEmprestimos import EmprestimoController

class tela_ResgistroEmprestimos:
    def __init__(self,root_ref,IDfuncionario=None):
         # Recebe a janela principal
          self.root_ref = root_ref
          self.IDfuncionario = IDfuncionario


        # Cria uma nova janela secundária 
          self.janelaRegistroEmprestimos = tk.Toplevel()
          self.janelaRegistroEmprestimos.title("Registrar Empréstimos")
          largura = 1024
          altura = 768
        
          #Posicionamento do programa(Ao inicia-lo)
          largura_tela = self.janelaRegistroEmprestimos.winfo_screenwidth()
          altura_tela = self.janelaRegistroEmprestimos.winfo_screenheight()
          x = (largura_tela - largura) // 2
          y = (altura_tela - altura) // 2
          self.janelaRegistroEmprestimos.geometry(f"{largura}x{altura}+{x}+{y}")
          

          #Criando o atributo imagem e convertendo ele para tk.
          self.imagem = Image.open(r"C:\Users\allan\OneDrive\Área de Trabalho\atualizeiraid\Projeto Biblioteca\VIEW\imagens\imagembiblioteca.png")
          self.imagem = self.imagem.resize((1024,768)) 
          self.imagem_tk = ImageTk.PhotoImage(self.imagem)

          #Cria a label que será responsavel por exibir e manipular a imagem na janela.
          self.label_imagem = tk.Label(self.janelaRegistroEmprestimos, image=self.imagem_tk)
          self.label_imagem.image = self.imagem_tk
          self.label_imagem.place(x=0, y=0,relwidth=1, relheight=1)

          #Frame
          self.frame = tk.Frame(self.janelaRegistroEmprestimos, width=678, height=315)
          self.frame.place(x=170,y=220)
          self.frame2 = tk.Frame(self.janelaRegistroEmprestimos, width=300, height=50)
          self.frame2.place(x=363,y=110)

          #Formatação campos de texto
          self._formatando = False           
          self.var_CPF = tk.StringVar()
          self.var_CPF.trace_add("write", self.formatarcpf)

          #Campos de texto
          self.campo_TituloLivro = tk.Entry(self.frame,width=40, font=("Arial", 14))
          self.campo_TituloLivro.place(x=220,y=40)
          self.campo_CPFMembro = tk.Entry(self.frame,width=40, font=("Arial", 14),textvariable=self.var_CPF)
          self.campo_CPFMembro.place(x=220,y=100)

          #Campos de data
          self.campo_DataEmprestimo= DateEntry(self.frame,width=14, date_pattern='dd/mm/yyyy',font=("Arial", 14))
          self.campo_DataEmprestimo.place(x=220,y=160)
          self.campo_DataDevolucao = DateEntry(self.frame,width=14, date_pattern='dd/mm/yyyy',font=("Arial", 14))
          self.campo_DataDevolucao.place(x=220,y=220)
          
          #Texto estatico 
          label_textoTitulo = tk.Label(self.frame, text="Titulo do Livro: ", font=("Arial", 14))
          label_textoTitulo.place(x=20,y=40)
          label_textoCPFMembro = tk.Label(self.frame, text="CPF Membro: ", font=("Arial", 14))
          label_textoCPFMembro.place(x=20,y=100)
          label_textoDataEmprestimo = tk.Label(self.frame, text="Emprestado Em: ", font=("Arial", 14))
          label_textoDataEmprestimo.place(x=20,y=160)
          label_textoDataDevolucao = tk.Label(self.frame, text="Prazo para Devolução: ", font=("Arial", 14))
          label_textoDataDevolucao.place(x=20,y=220)
          
          label_textoCadastar = tk.Label(self.frame2, text="Registrar Novo Empréstimo", font=("Arial", 14))
          label_textoCadastar.place(x=30,y=13)

          #Botões
          self.b_Voltar = tk.Button( self.frame,text='VOLTAR',width=12,height=2,command=self.onClose,relief="raised", overrelief="ridge",bg="light blue",fg="black")
          self.b_Voltar.place(x=20,y=260)
          self.b_Salvar = tk.Button( self.frame,text='SALVAR',width=12,height=2,command=self.SalvarEmprestimo,relief="raised", overrelief="ridge",bg="light blue",fg="black")
          self.b_Salvar.place(x=570,y=260)

          #Codigo para impedir manipulação da tela
          self.janelaRegistroEmprestimos.resizable(False, False)
    
    #Função responsavel pela formatação do campoCPFMembro
    def formatarcpf(self, *args):
          if self._formatando:
               return

          valor = self.var_CPF.get()
          pos_cursor_bruto = self.campo_CPFMembro.index(tk.INSERT)
          digitos_antes = len([c for c in valor[:pos_cursor_bruto] if c.isdigit()])

          todos_digitos = [c for c in valor if c.isdigit()]
          if len(todos_digitos) > 11:
               todos_digitos = todos_digitos[:11]

          novo_formatado = ""
          for i, num in enumerate(todos_digitos):
               if i == 3 or i == 6:
                    novo_formatado += "."
               if i == 9:
                    novo_formatado += "-"
               novo_formatado += num

          if valor == novo_formatado:
               return

          self._formatando = True
          self.var_CPF.set(novo_formatado)
          self.campo_CPFMembro.after_idle(lambda: self.ajustarcursor(digitos_antes, novo_formatado, self.campo_CPFMembro))

    #Função responsável por ajustar o cursor para o ultimo digito
    def ajustarcursor(self, digitos_antes, novo_formatado, campo):
          n = digitos_antes
          count = 0
          nova_pos = len(novo_formatado)
          for idx, ch in enumerate(novo_formatado):
               if ch.isdigit():
                    count += 1
               if count == n:
                    nova_pos = idx + 1
                    break

          if nova_pos > len(novo_formatado):
               nova_pos = len(novo_formatado)

          campo.icursor(nova_pos)
          self._formatando = False
          

    def SalvarEmprestimo(self):
         TituloLivro = self.campo_TituloLivro.get().strip()
         CPFMembro = self.campo_CPFMembro.get().strip()
         DataEmprestimo = self.campo_DataEmprestimo.get().strip()
         PrazoEmprestimo = self.campo_DataDevolucao.get().strip()

         if not TituloLivro or not CPFMembro or not DataEmprestimo or not PrazoEmprestimo:
               messagebox.showwarning("Campos Obrigatórios", "Preencha todos os campos antes de Salvar o Empréstimo.")
               return

         DataEmprestimoMySQL = datetime.strptime(DataEmprestimo, "%d/%m/%Y").date()
         PrazoEmprestimoMySQL = datetime.strptime(PrazoEmprestimo, "%d/%m/%Y").date()
         Emprestimo = EmprestimoController()
         Emprestimo.cadastraremprestimo(TituloLivro, CPFMembro,DataEmprestimoMySQL ,PrazoEmprestimoMySQL)

    def onClose(self):
        self.janelaRegistroEmprestimos.destroy()
        self.root_ref.deiconify()

          


