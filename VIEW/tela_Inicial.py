   #Importando bibliotecas
from tkinter import ttk   #Importa o módulo ttk, que é o Toolkit Temático do Tkinter.
import tkinter as tk      #Importa o módulo inteiro tkinter com um apelido (tk).
from PIL import Image, ImageTk # usada para abrir, editar, redimensionar e exibir imagens no Python.
from VIEW.tela_CadastrarLivro import tela_CadastrarLivro
from VIEW.tela_CadastrarMembro import tela_CadastrarMembro
from VIEW.tela_PesquisarLivros import tela_PesquisarLivros
from VIEW.tela_PesquisarMembros import tela_PesquisarMembros
from VIEW.tela_RegistroEmprestimos import tela_ResgistroEmprestimos
from VIEW.tela_HistoricoEmprestimos import tela_HistoricoEmprestimos
from VIEW.tela_Gestãodedevolução import tela_GestãodeDevolução
from VIEW.tela_conta import tela_contafuncionario


class TelaInicial:
    #Função inicial que cria a tela.
    def __init__(self,root_ref,IDfuncionario=None):
        # Recebe a janela principal
        self.root_ref = root_ref
        self.IDfuncionario = IDfuncionario



        #Atributos da tela
        self.janela_Principal = tk.Toplevel()
        largura = 1024
        altura = 768
        
        #Posicionamento do programa(Ao inicia-lo)
        largura_tela = self.janela_Principal.winfo_screenwidth()
        altura_tela = self.janela_Principal.winfo_screenheight()
        x = (largura_tela - largura) // 2
        y = (altura_tela - altura) // 2
        self.janela_Principal.geometry(f"{largura}x{altura}+{x}+{y}")
        self.janela_Principal.title("Sistema Biblioteca")

        #Criando o atributo imagem e convertendo ele para tk.
        self.imagem = Image.open(r"C:\Users\allan\OneDrive\Área de Trabalho\atualizeiraid\Projeto Biblioteca\VIEW\imagens\imagembiblioteca.png")
        self.imagem = self.imagem.resize((1024,768)) 
        self.imagem_tk = ImageTk.PhotoImage(self.imagem)

        #Cria a label que será responsavel por exibir e manipular a imagem na janela.
        self.label_imagem = tk.Label(self.janela_Principal, image=self.imagem_tk)
        self.label_imagem.place(x=0, y=0,relwidth=1, relheight=1)

        #Botões
        self.b_PesquisarLivros =  tk.Button(self.label_imagem,command= self.abrir_PesquisarLivros ,width=26, height=4, text="Pesquisar Livros",font= 'arial 13 bold',relief="raised", overrelief="ridge")
        self.b_PesquisarLivros.place(x=200, y=160)

        self.b_PesquisarMembros =  tk.Button(self.label_imagem,command= self.abrir_PesquisarMembros , width=26, height=4, text="Pesquisar Membros",font= 'arial 13 bold',relief="raised", overrelief="ridge")
        self.b_PesquisarMembros.place(x=550, y=160)
        
        self.b_CadastrarLivros = tk.Button(self.label_imagem,command=self.abrir_CadastroLivro, width=26, height=4, text="Cadastrar Livros",font= 'Ivy 13 bold',relief="raised", overrelief="ridge")
        self.b_CadastrarLivros.place(x=200, y=320)
        
        self.b_CadastrarMembros =  tk.Button(self.label_imagem,command=self.abrir_CadastroMembro ,width=26, height=4, text="Cadastrar Membros",font= 'Ivy 13 bold',relief="raised", overrelief="ridge")
        self.b_CadastrarMembros.place(x=550, y=320)

        self.b_RegistrodeEmprestimos =  tk.Button(self.label_imagem,command=self.abrir_RegistroEmprestimos, width=26, height=4, text="Registro de Empréstimos",font= 'Ivy 13 bold',relief="raised", overrelief="ridge")
        self.b_RegistrodeEmprestimos.place(x=550, y=480)

        self.b_HistoricodeEmprestimos =  tk.Button(self.label_imagem, command=self.abrir_HistoricoEmprestimos,width=26, height=4, text="Histórico de Empréstimos",font= 'Ivy 13 bold',relief="raised", overrelief="ridge")
        self.b_HistoricodeEmprestimos.place(x=200, y=480)

        self.b_GestaodeDevolucoes =  tk.Button(self.label_imagem, command=self.abrir_Gestãodedevolução, width=26, height=4, text="Gestão de Devoluções",font= 'Comic_Sans_MS 13 bold',relief="raised", overrelief="ridge")
        self.b_GestaodeDevolucoes.place(x=200, y=640)

        self.b_Relatorios =  tk.Button(self.label_imagem,command=self.abrir_contafuncionario, width=26, height=4, text="Conta",font= 'Helvetica 13 bold',relief="raised", overrelief="ridge")
        self.b_Relatorios.place(x=550, y=640)

        #Codigo para impedir manipulação da tela
        self.janela_Principal.resizable(False, False)


    #Funções abrir telas
    def abrir_CadastroLivro(self):
        self.janela_Principal.withdraw()
        tela_CadastrarLivro(self.janela_Principal,self.IDfuncionario)
    
    def abrir_PesquisarLivros(self):
        self.janela_Principal.withdraw()
        tela_PesquisarLivros(self.janela_Principal,self.IDfuncionario)

    def abrir_PesquisarMembros(self):
        self.janela_Principal.withdraw()
        tela_PesquisarMembros(self.janela_Principal,self.IDfuncionario)

    def abrir_CadastroMembro(self):
        self.janela_Principal.withdraw()
        tela_CadastrarMembro(self.janela_Principal,self.IDfuncionario)

    def abrir_RegistroEmprestimos(self):
        self.janela_Principal.withdraw()
        tela_ResgistroEmprestimos(self.janela_Principal,self.IDfuncionario)
    
    
    def abrir_HistoricoEmprestimos(self):
        self.janela_Principal.withdraw()
        tela_HistoricoEmprestimos(self.janela_Principal,self.IDfuncionario)

    def abrir_Gestãodedevolução(self):
        self.janela_Principal.withdraw()
        tela_GestãodeDevolução(self.janela_Principal,self.IDfuncionario)

    def abrir_contafuncionario(self):
        self.janela_Principal.withdraw()
        tela_contafuncionario(self.janela_Principal,self.IDfuncionario)
  

