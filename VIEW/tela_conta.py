#Importando bibliotecas
from tkinter import ttk   #Importa o módulo ttk, que é o Toolkit Temático do Tkinter.
import tkinter as tk      #Importa o módulo inteiro tkinter com um apelido (tk).
from PIL import Image, ImageTk # usada para abrir, editar, redimensionar e exibir imagens no Python.
from tkinter import messagebox
from CONTROLLER.controllerFuncionarios import Funcionarioscontroller
from VIEW.tela_cadastrarfuncionario import tela_Cadastrarfuncionario

class tela_contafuncionario:
     def __init__(self,root_ref,IDfuncionario=None):
          # Recebe a janela principal
          self.root_ref = root_ref
          self.IDfuncionario = IDfuncionario


          # Cria uma nova janela secundária
          self.janelacontafuncionario = tk.Toplevel()
          self.janelacontafuncionario.title("Cadastrar Livros")
          largura = 1024
          altura = 768
        
          #Posicionamento do programa(Ao inicia-lo)
          largura_tela = self.janelacontafuncionario.winfo_screenwidth()
          altura_tela = self.janelacontafuncionario.winfo_screenheight()
          x = (largura_tela - largura) // 2
          y = (altura_tela - altura) // 2
          self.janelacontafuncionario.geometry(f"{largura}x{altura}+{x}+{y}")
          
         
          #Criando o atributo imagem e convertendo ele para tk.
          self.imagem = Image.open(r"C:\Users\allan\OneDrive\Área de Trabalho\atualizeiraid\Projeto Biblioteca\VIEW\imagens\imagembiblioteca.png")
          self.imagem = self.imagem.resize((1024,768)) 
          self.imagem_tk = ImageTk.PhotoImage(self.imagem)

          #Cria a label que será responsavel por exibir e manipular a imagem na janela.
          self.label_imagem = tk.Label(self.janelacontafuncionario, image=self.imagem_tk)
          self.label_imagem.place(x=0, y=0,relwidth=1, relheight=1)

          #Frame
          self.frame = tk.Frame(self.janelacontafuncionario, width=720, height=420)
          self.frame.place(x=152,y=180)
          self.frame2 = tk.Frame(self.janelacontafuncionario, width=300, height=50)
          self.frame2.place(x=363,y=65)
          self.frame2 = tk.Frame(self.janelacontafuncionario, width=300, height=50)
          self.frame2.place(x=363,y=65)
          
          #Formatação campos de texto
          self._formatando_nome = False
          self._formatando_cargo = False

          self.var_Nome = tk.StringVar()
          self.var_Nome.trace_add("write", self.formatarNome)

          self.var_Cargo = tk.StringVar()
          self.var_Cargo.trace_add("write", self.formatarCargo)

         #Botões
          self.b_Voltar = tk.Button( self.frame,text='VOLTAR',width=12,height=2,command=self.onClose,relief="raised", overrelief="ridge",bg="light blue", fg="black")
          self.b_Voltar.place(x=20,y=360)
          self.b_Salvar = tk.Button( self.frame,text='SALVAR',width=12,height=2,command=self.atualizarFuncionario,relief="raised", overrelief="ridge",bg="light blue", fg="black")
          self.b_Salvar.place(x=570,y=360)

          self.b_CadastrarFuncionario = tk.Button( self.frame,text='CADASTRAR FUNCIONARIO',width=24,height=2,command=self.abrir_cadastrofuncionario,relief="raised", overrelief="ridge",bg="light green",fg="black")
          self.b_CadastrarFuncionario.place(x=260,y=360)
          

          self.b_Excluir = tk.Button(self.label_imagem, text='Excluir Conta', width=12, height=2,command=self.excluirContaFuncionario, relief="raised", overrelief="ridge", bg="red", fg="white")
          self.b_Excluir.place(x=900, y=700)


          # Texto estático
          label_textoNome = tk.Label(self.frame, text="Editar Nome: ", font=("Arial", 14))
          label_textoNome.place(x=20,y=60)
          label_textoLogin = tk.Label(self.frame, text="Editar Login: ", font=("Arial", 14))
          label_textoLogin.place(x=20,y=120)
          label_textoSenha = tk.Label(self.frame, text="Editar Senha: ", font=("Arial", 14))
          label_textoSenha.place(x=20,y=180)
          label_textoCargo = tk.Label(self.frame, text="Editar Cargo: ", font=("Arial", 14))
          label_textoCargo.place(x=20,y=240)
          

          label_textoCadastar = tk.Label(self.frame2, text="Atualizar Informações", font=("Arial", 14))
          label_textoCadastar.place(x=56,y=13)



         #Campos de texto
          self.campo_Nome = tk.Entry(self.frame,width=40, font=("Arial", 14),textvariable=self.var_Nome)
          self.campo_Nome.place(x=220,y=60)
          self.campo_Login = tk.Entry(self.frame,width=40, font=("Arial", 14))
          self.campo_Login.place(x=220,y=120)
          self.campo_Senha = tk.Entry(self.frame,width=40, font=("Arial", 14))
          self.campo_Senha.place(x=220,y=180)
          self.campo_Cargo = tk.Entry(self.frame,width=40, font=("Arial", 14),textvariable=self.var_Cargo)
          self.campo_Cargo.place(x=220,y=240)
          

          #Codigo para impedir manipulação da tela
          self.janelacontafuncionario.resizable(False, False)

          #Carregando dados na tela
          self.carregar_dados_funcionario()

      #Função responsavel pela formatação do campoNome
     def formatarNome(self, *args):
               if self._formatando_nome:
                    return

               valor = self.var_Nome.get()

               # Remove tudo que não for letra ou espaço
               valor_filtrado = ''.join([c for c in valor if c.isalpha() or c.isspace()])

               # Remove espaços múltiplos seguidos
               valor_formatado = ' '.join(valor_filtrado.split())

               self._formatando_nome = True
               self.var_Nome.set(valor_formatado)
               self._formatando_nome = False

      #Função responsavel pela formatação do campoCargo
     def formatarCargo(self, *args):
               if self._formatando_cargo:
                    return

               valor = self.var_Cargo.get()

               # Remove tudo que não for letra ou espaço
               valor_filtrado = ''.join([c for c in valor if c.isalpha() or c.isspace()])

               # Remove espaços múltiplos seguidos
               valor_formatado = ' '.join(valor_filtrado.split())

               self._formatando_cargo = True
               self.var_Cargo.set(valor_formatado)
               self._formatando_cargo = False
          
     def onClose(self):
        self.janelacontafuncionario.destroy()
        self.root_ref.deiconify()

     def atualizarFuncionario(self):
          nome = self.campo_Nome.get().strip()
          login = self.campo_Login.get().strip()
          senha = self.campo_Senha.get().strip()
          cargo = self.campo_Cargo.get().strip()
          funcionario = Funcionarioscontroller()

          if not nome or not login or not senha or not cargo:
               messagebox.showwarning("Campos Obrigatórios", "Preencha todos os campos antes de salvar as alterações.")
               return

          if funcionario.atualizarDadosFuncionario(self.IDfuncionario, nome, login, senha, cargo):
               messagebox.showinfo("Sucesso", "Dados do funcionário atualizados com sucesso!")
          else:
               messagebox.showerror("Erro", "Falha ao atualizar os dados do funcionário.")

     def excluirContaFuncionario(self):
          funcionarios = Funcionarioscontroller()
          return funcionarios.excluirFuncionario(self.IDfuncionario)


     def carregar_dados_funcionario(self):
          funcionario = Funcionarioscontroller()
          if self.IDfuncionario:
               dados = funcionario.exibirDadosFuncionario(self.IDfuncionario)
               if dados:
                    nome, login, senha, cargo = dados
                    self.campo_Nome.insert(0, nome)
                    self.campo_Login.insert(0, login)
                    self.campo_Senha.insert(0, senha)
                    self.campo_Cargo.insert(0, cargo)

     def abrir_cadastrofuncionario(self):
        self.janelacontafuncionario.withdraw()
        tela_Cadastrarfuncionario(self.janelacontafuncionario,self.IDfuncionario)