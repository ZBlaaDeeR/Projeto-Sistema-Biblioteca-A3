  #Importando bibliotecas
from tkinter import ttk   #Importa o módulo ttk, que é o Toolkit Temático do Tkinter.
import tkinter as tk      #Importa o módulo inteiro tkinter com um apelido (tk).
from PIL import Image, ImageTk # usada para abrir, editar, redimensionar e exibir imagens no Python.
from VIEW.tela_Inicial import TelaInicial
from CONTROLLER.controllerFuncionarios import Funcionarioscontroller

class TelaLogin:
    #Função inicial que cria a tela.
    def __init__(self):
        #Atributos da tela
        self.janela_Login = tk.Tk()
        largura = 1024
        altura = 768
        
        #Posicionamento do programa(Ao inicia-lo)
        largura_tela = self.janela_Login.winfo_screenwidth()
        altura_tela = self.janela_Login.winfo_screenheight()
        x = (largura_tela - largura) // 2
        y = (altura_tela - altura) // 2
        self.janela_Login.geometry(f"{largura}x{altura}+{x}+{y}")
        self.janela_Login.title("Sistema Biblioteca")

        #Criando o atributo imagem e convertendo ele para tk.
        self.imagem = Image.open(r"C:\Users\allan\OneDrive\Área de Trabalho\atualizeiraid\Projeto Biblioteca\VIEW\imagens\imagembiblioteca.png")
        self.imagem = self.imagem.resize((1024,768)) 
        self.imagem_tk = ImageTk.PhotoImage(self.imagem)

        #Cria a label que será responsavel por exibir e manipular a imagem na janela.
        self.label_imagem = tk.Label(self.janela_Login, image=self.imagem_tk)
        self.label_imagem.place(x=0, y=0,relwidth=1, relheight=1)

        #Frame
        self.frame = tk.Frame(self.janela_Login, width=600, height=240)
        self.frame.place(x=230,y=220)
        self.frame2 = tk.Frame(self.janela_Login, width=220, height=50)
        self.frame2.place(x=400,y=110)

        #Campos de texto
        self.campo_Login = tk.Entry(self.frame,width=32, font=("Arial", 14))
        self.campo_Login.place(x=180,y=40)
        self.campo_Senha = tk.Entry(self.frame,width=32, font=("Arial", 14),show="*")
        self.campo_Senha.place(x=180,y=100)

        #Texto estatico 
        label_Login = tk.Label(self.frame, text="Login: ", font=("Arial", 14))
        label_Login.place(x=60,y=40)
        label_Senha = tk.Label(self.frame, text="Senha: ", font=("Arial", 14))
        label_Senha.place(x=60,y=100)

        label_Acessar = tk.Label(self.frame2, text="Acessar", font=("Arial", 14))
        label_Acessar.place(x=70,y=13)

        #Botão 
        self.b_ENTRAR = tk.Button( self.frame,text='ENTRAR',command=self.abrir_Telainicial,width=12,height=2,relief="raised", overrelief="ridge",bg="light blue",fg="black")
        self.b_ENTRAR.place(x=440,y=180)


        #Codigo para impedir manipulação da tela
        self.janela_Login.resizable(False, False)

       
    def abrir_Telainicial(self):
         login = self.campo_Login.get()
         senha = self.campo_Senha.get()
         funcionario = Funcionarioscontroller()
         id_funcionario = funcionario.VerificarCredenciais(login, senha)

         if id_funcionario:
          self.janela_Login.withdraw()
          TelaInicial(self.janela_Login, id_funcionario)

    def iniciar(self):
        self.janela_Login.mainloop()



