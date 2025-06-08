#Importando bibliotecas
from tkinter import ttk   #Importa o módulo ttk, que é o Toolkit Temático do Tkinter.
import tkinter as tk      #Importa o módulo inteiro tkinter com um apelido (tk).
from PIL import Image, ImageTk # usada para abrir, editar, redimensionar e exibir imagens no Python.
from tkcalendar import DateEntry # Usada para adicionarmos um campo de calendario
from datetime import datetime #Import para facilitar a conversão de datas
from tkinter import messagebox
from CONTROLLER.controllerEmprestimos import EmprestimoController

class tela_GestãodeDevolução:
    def __init__(self,root_ref,IDfuncionario=None):
         # Recebe a janela principal
          self.root_ref = root_ref
          self.IDfuncionario = IDfuncionario


        # Cria uma nova janela secundária 
          self.janelaGestãodeDevolução = tk.Toplevel()
          self.janelaGestãodeDevolução.title("Gestão de Devoluções")
          largura = 1024
          altura = 768
        
          #Posicionamento do programa(Ao inicia-lo)
          largura_tela = self.janelaGestãodeDevolução.winfo_screenwidth()
          altura_tela = self.janelaGestãodeDevolução.winfo_screenheight()
          x = (largura_tela - largura) // 2
          y = (altura_tela - altura) // 2
          self.janelaGestãodeDevolução.geometry(f"{largura}x{altura}+{x}+{y}")
          

          #Criando o atributo imagem e convertendo ele para tk.
          self.imagem = Image.open(r"C:\Users\allan\OneDrive\Área de Trabalho\atualizeiraid\Projeto Biblioteca\VIEW\imagens\imagembiblioteca.png")
          self.imagem = self.imagem.resize((1024,768)) 
          self.imagem_tk = ImageTk.PhotoImage(self.imagem)

          #Cria a label que será responsavel por exibir e manipular a imagem na janela.
          self.label_imagem = tk.Label(self.janelaGestãodeDevolução, image=self.imagem_tk)
          self.label_imagem.image = self.imagem_tk
          self.label_imagem.place(x=0, y=0,relwidth=1, relheight=1)

          #Frame
          self.frame = tk.Frame(self.janelaGestãodeDevolução, width=678, height=280)
          self.frame.place(x=170,y=220)
          self.frame2 = tk.Frame(self.janelaGestãodeDevolução, width=300, height=50)
          self.frame2.place(x=363,y=110)

          #Campos de texto
          self.campo_IDEmprestimo = tk.Entry(self.frame,width=40, font=("Arial", 14))
          self.campo_IDEmprestimo.place(x=220,y=40)
         

          #Campos de data
          self.campo_DataDevolução= DateEntry(self.frame,width=14, date_pattern='dd/mm/yyyy',font=("Arial", 14))
          self.campo_DataDevolução.place(x=220,y=120)
          
          
          #Texto estatico 
          label_textoID = tk.Label(self.frame, text="ID Emprestimo: ", font=("Arial", 14))
          label_textoID.place(x=20,y=40)
         
          label_textoDataDevolução = tk.Label(self.frame, text="Devolvido Em: ", font=("Arial", 14))
          label_textoDataDevolução.place(x=20,y=120)
          
          label_textoDevolução = tk.Label(self.frame2, text="Devolução de Empréstimo", font=("Arial", 14))
          label_textoDevolução.place(x=30,y=13)

          #Botões
          self.b_Voltar = tk.Button( self.frame,text='VOLTAR',width=12,height=2,command=self.onClose,relief="raised", overrelief="ridge",bg="light blue",fg="black")
          self.b_Voltar.place(x=20,y=200)
          self.b_Salvar = tk.Button( self.frame,text='SALVAR',width=12,height=2,command=self.DevolucaoEmprestimo,relief="raised", overrelief="ridge",bg="light blue",fg="black")
          self.b_Salvar.place(x=570,y=200)

          #Codigo para impedir manipulação da tela
          self.janelaGestãodeDevolução.resizable(False, False)
    
    
    #Função que fará a devolução e alterar livro para disponivel
    def DevolucaoEmprestimo(self):
         IDemprestimo = self.campo_IDEmprestimo.get().strip()
         DataDevolucao = self.campo_DataDevolução.get().strip()
         

         if not IDemprestimo or not DataDevolucao:
               messagebox.showwarning("Campos Obrigatórios", "Preencha todos os campos antes de Salvar o Empréstimo.")
               return

         DataDevolucaoMySQL = datetime.strptime(DataDevolucao, "%d/%m/%Y").date()
         Devolucao = EmprestimoController()
         Devolucao.devolucaoemprestimo(IDemprestimo, DataDevolucaoMySQL)

    def onClose(self):
        self.janelaGestãodeDevolução.destroy()
        self.root_ref.deiconify()