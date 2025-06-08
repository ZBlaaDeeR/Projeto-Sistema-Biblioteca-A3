#Importando bibliotecas
from tkinter import ttk   #Importa o módulo ttk, que é o Toolkit Temático do Tkinter.
import tkinter as tk      #Importa o módulo inteiro tkinter com um apelido (tk).
from PIL import Image, ImageTk # usada para abrir, editar, redimensionar e exibir imagens no Python.
from tkinter import messagebox
from CONTROLLER.controllerFuncionarios import Funcionarioscontroller

class tela_Cadastrarfuncionario:
     def __init__(self,root_ref,IDfuncionario=None):
          # Recebe a janela principal
          self.root_ref = root_ref
          self.IDfuncionario =IDfuncionario

          # Cria uma nova janela secundária
          self.janelaCadastrarFuncionario = tk.Toplevel()
          self.janelaCadastrarFuncionario.title("Cadastrar Funcionarios")
          largura = 1024
          altura = 768
        
          #Posicionamento do programa(Ao inicia-lo)
          largura_tela = self.janelaCadastrarFuncionario.winfo_screenwidth()
          altura_tela = self.janelaCadastrarFuncionario.winfo_screenheight()
          x = (largura_tela - largura) // 2
          y = (altura_tela - altura) // 2
          self.janelaCadastrarFuncionario.geometry(f"{largura}x{altura}+{x}+{y}")
          
         
          #Criando o atributo imagem e convertendo ele para tk.
          self.imagem = Image.open(r"C:\Users\allan\OneDrive\Área de Trabalho\atualizeiraid\Projeto Biblioteca\VIEW\imagens\imagembiblioteca.png")
          self.imagem = self.imagem.resize((1024,768)) 
          self.imagem_tk = ImageTk.PhotoImage(self.imagem)

          #Cria a label que será responsavel por exibir e manipular a imagem na janela.
          self.label_imagem = tk.Label(self.janelaCadastrarFuncionario, image=self.imagem_tk)
          self.label_imagem.place(x=0, y=0,relwidth=1, relheight=1)

          #Frame
          self.frame = tk.Frame(self.janelaCadastrarFuncionario, width=720, height=420)
          self.frame.place(x=152,y=180)
          self.frame2 = tk.Frame(self.janelaCadastrarFuncionario, width=300, height=50)
          self.frame2.place(x=363,y=65)
          
         
         #Botões
          self.b_Voltar = tk.Button( self.frame,text='VOLTAR',width=12,height=2,command=self.onClose,relief="raised", overrelief="ridge",bg="light blue",fg="black")
          self.b_Voltar.place(x=20,y=360)
          self.b_Salvar = tk.Button( self.frame,text='SALVAR',width=12,height=2,command=self.SalvarFuncionario,relief="raised", overrelief="ridge",bg="light blue",fg="black")
          self.b_Salvar.place(x=570,y=360)


          # Texto estático
          label_textoNome = tk.Label(self.frame, text="Digite seu Nome: ", font=("Arial", 14))
          label_textoNome.place(x=20,y=60)
          label_textoLogin = tk.Label(self.frame, text="Digite seu Login: ", font=("Arial", 14))
          label_textoLogin.place(x=20,y=120)
          label_textoSenha = tk.Label(self.frame, text="Digite sua senha: ", font=("Arial", 14))
          label_textoSenha.place(x=20,y=180)
          label_textoCargo = tk.Label(self.frame, text="Digite seu Cargo: ", font=("Arial", 14))
          label_textoCargo.place(x=20,y=240)
          

          label_textoCadastar = tk.Label(self.frame2, text="Cadastrar novo Funcionário", font=("Arial", 14))
          label_textoCadastar.place(x=35,y=13)



         #Campos de texto
          self.campo_Nome = tk.Entry(self.frame,width=40, font=("Arial", 14))
          self.campo_Nome.place(x=220,y=60)
          self.campo_Login = tk.Entry(self.frame,width=40, font=("Arial", 14))
          self.campo_Login.place(x=220,y=120)
          self.campo_Senha = tk.Entry(self.frame,width=40, font=("Arial", 14))
          self.campo_Senha.place(x=220,y=180)
          self.campo_Cargo = tk.Entry(self.frame,width=40, font=("Arial", 14))
          self.campo_Cargo.place(x=220,y=240)
          

          #Codigo para impedir manipulação da tela
          self.janelaCadastrarFuncionario.resizable(False, False)

     def onClose(self):
          self.janelaCadastrarFuncionario.destroy()
          self.root_ref.deiconify()

     def SalvarFuncionario(self):
        nome = self.campo_Nome.get().strip()
        login = self.campo_Login.get().strip()
        senha = self.campo_Senha.get().strip()
        cargo = self.campo_Cargo.get().strip()

        funcionario = Funcionarioscontroller()

        if not nome or not login or not senha or not cargo:
            messagebox.showwarning("Campos Obrigatórios", "Preencha todos os campos antes de cadastrar o funcionário.")
            return

        funcionario.adicionarFuncionario(nome, login, senha, cargo)
