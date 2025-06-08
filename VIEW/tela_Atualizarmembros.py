#Importando bibliotecas
from tkinter import ttk   #Importa o módulo ttk, que é o Toolkit Temático do Tkinter.
import tkinter as tk      #Importa o módulo inteiro tkinter com um apelido (tk).
from PIL import Image, ImageTk # usada para abrir, editar, redimensionar e exibir imagens no Python.
from tkinter import messagebox
from CONTROLLER.controllerMembro import MembroController


class tela_Atualizarmembros:
    def __init__(self,root_ref,IDmembro,IDfuncionario=None):
         # Recebe a janela principal
          self.root_ref = root_ref
          self.IDmembro = IDmembro
          self.IDfuncionario = IDfuncionario


        # Cria uma nova janela secundária 
          self.janelaAtualizarMembros = tk.Toplevel()
          self.janelaAtualizarMembros.title("Cadastrar Membros")
          largura = 1024
          altura = 768
        
          #Posicionamento do programa(Ao inicia-lo)
          largura_tela = self.janelaAtualizarMembros.winfo_screenwidth()
          altura_tela = self.janelaAtualizarMembros.winfo_screenheight()
          x = (largura_tela - largura) // 2
          y = (altura_tela - altura) // 2
          self.janelaAtualizarMembros.geometry(f"{largura}x{altura}+{x}+{y}")
          

          #Criando o atributo imagem e convertendo ele para tk.
          self.imagem = Image.open(r"C:\Users\allan\OneDrive\Área de Trabalho\atualizeiraid\Projeto Biblioteca\VIEW\imagens\imagembiblioteca.png")
          self.imagem = self.imagem.resize((1024,768)) 
          self.imagem_tk = ImageTk.PhotoImage(self.imagem)

          #Cria a label que será responsavel por exibir e manipular a imagem na janela.
          self.label_imagem = tk.Label(self.janelaAtualizarMembros, image=self.imagem_tk)
          self.label_imagem.image = self.imagem_tk
          self.label_imagem.place(x=0, y=0,relwidth=1, relheight=1)

          #Frame
          self.frame = tk.Frame(self.janelaAtualizarMembros, width=678, height=315)
          self.frame.place(x=170,y=220)
          self.frame2 = tk.Frame(self.janelaAtualizarMembros, width=300, height=50)
          self.frame2.place(x=363,y=110)

          #Formatação campos de texto
          self._formatando = False  
          self.var_Nome = tk.StringVar()
          self.var_Nome.trace_add("write", self.formatarNome)         
          self.var_CPF = tk.StringVar()
          self.var_CPF.trace_add("write", self.formatarcpf)
          self.var_telefone = tk.StringVar()
          self.var_telefone.trace_add("write", self.formatartelefone)

          #Campos de texto
          self.campo_Gmail = tk.Entry(self.frame,width=40, font=("Arial", 14))
          self.campo_Gmail.place(x=220,y=40)
          self.campo_Nome = tk.Entry(self.frame,width=40, font=("Arial", 14), textvariable=self.var_Nome)
          self.campo_Nome.place(x=220,y=100)
          self.campo_Telefone = tk.Entry(self.frame,width=14, font=("Arial", 14), textvariable=self.var_telefone)
          self.campo_Telefone.place(x=220,y=160)
          self.campo_CPF = tk.Entry(self.frame,width=14, font=("Arial", 14),textvariable=self.var_CPF)
          self.campo_CPF.place(x=507,y=160)
          
          #Texto estatico 
          label_textoGmail = tk.Label(self.frame, text="Digite seu Gmail: ", font=("Arial", 14))
          label_textoGmail.place(x=20,y=40)
          label_textoNome = tk.Label(self.frame, text="Digite seu Nome: ", font=("Arial", 14))
          label_textoNome.place(x=20,y=100)
          label_textoTelefone = tk.Label(self.frame, text="Telefone: ", font=("Arial", 14))
          label_textoTelefone.place(x=20,y=160)
          label_textoCPF = tk.Label(self.frame, text="CPF: ", font=("Arial", 14))
          label_textoCPF.place(x=420,y=160)
          
          label_textoCadastar = tk.Label(self.frame2, text="Cadastrar Novo Membro", font=("Arial", 14))
          label_textoCadastar.place(x=56,y=13)

          #Botões
          self.b_Voltar = tk.Button( self.frame,text='VOLTAR',width=12,height=2,command=self.onClose,relief="raised", overrelief="ridge",bg="light blue",fg="black")
          self.b_Voltar.place(x=20,y=240)
          self.b_Salvar = tk.Button( self.frame,text='SALVAR',width=12,height=2,command=self.atualizarMembro,relief="raised", overrelief="ridge",bg="light blue",fg="black")
          self.b_Salvar.place(x=570,y=240)

          #Codigo para impedir manipulação da tela
          self.janelaAtualizarMembros.resizable(False, False)

          self.carregar_dados_membro()


     
    #Função responsavel pela formatação do campoNome
    def formatarNome(self, *args):
          if self._formatando:
               return

          valor = self.var_Nome.get()

          # Remove tudo que não for letra ou espaço
          valor_filtrado = ''.join([c for c in valor if c.isalpha() or c.isspace()])

          # Remove espaços múltiplos seguidos
          valor_formatado = ' '.join(valor_filtrado.split())

          self._formatando = True
          self.var_Nome.set(valor_formatado)
          self._formatando = False

    #Função responsavel pela formatação do campoCPF
    def formatarcpf(self, *args):
          if self._formatando:
               return

          valor = self.var_CPF.get()
          pos_cursor_bruto = self.campo_CPF.index(tk.INSERT)
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
          self.campo_CPF.after_idle(lambda: self._ajustar_cursor(digitos_antes, novo_formatado, self.campo_CPF))

    #Função responsavel pela formatação do campoTelefone
    def formatartelefone(self, *args):
          if self._formatando:
               return

          valor = self.var_telefone.get()
          pos_cursor_bruto = self.campo_Telefone.index(tk.INSERT)
          digitos_antes = len([c for c in valor[:pos_cursor_bruto] if c.isdigit()])

          todos_digitos = [c for c in valor if c.isdigit()]
          if len(todos_digitos) > 11:
               todos_digitos = todos_digitos[:11]

          novo_formatado = ""
          for i, num in enumerate(todos_digitos):
               if i == 0:
                    novo_formatado += "(" + num
               elif i == 1:
                    novo_formatado += num + ") "
               elif 2 <= i <= 6:
                    novo_formatado += num
               elif i == 7:
                    novo_formatado += "-" + num
               else:
                    novo_formatado += num

          if valor == novo_formatado:
               return

          self._formatando = True
          self.var_telefone.set(novo_formatado)
          self.campo_Telefone.after_idle(lambda: self._ajustar_cursor(digitos_antes, novo_formatado, self.campo_Telefone))

    #Função responsável por ajustar o cursor para o ultimo digito
    def _ajustar_cursor(self, digitos_antes, novo_formatado, campo):
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

    def onClose(self):
          self.janelaAtualizarMembros.destroy()
          self.root_ref.deiconify()
          self.root_ref.recarregarMembros()


    def atualizarMembro(self):
          nome = self.campo_Nome.get().strip()
          gmail = self.campo_Gmail.get().strip()
          telefone = self.campo_Telefone.get().strip()
          cpf = self.campo_CPF.get().strip()

          membro_controller = MembroController()

          # Verificar se todos os campos estão preenchidos
          if not nome or not gmail or not telefone or not cpf:
               messagebox.showwarning("Campos Obrigatórios", "Preencha todos os campos antes de salvar as alterações.")
               return

          # Validar CPF
          if not membro_controller.validadorCpf(cpf):
               messagebox.showerror("CPF Inválido", "O CPF informado não é válido.")
               return

          # Validar Telefone
          if not membro_controller.verificarTelefone(telefone):
               messagebox.showerror("Telefone Inválido", "O número de telefone informado não é válido.")
               return

          # Tentar atualizar os dados
          if membro_controller.atualizarDadosMembro(self.IDmembro, nome, gmail, telefone, cpf):
               messagebox.showinfo("Sucesso", "Dados do membro atualizados com sucesso!")
          else:
               messagebox.showerror("Erro", "Falha ao atualizar os dados do membro.")



    def carregar_dados_membro(self):
          membro = MembroController()
          if self.IDmembro:
               dados = membro.exibirDadosMembro(self.IDmembro)
            
               if dados:
                    nome, gmail, telefone, cpf = dados
                    self.campo_Nome.insert(0, nome)
                    self.campo_Gmail.insert(0, gmail)
                    self.campo_Telefone.insert(0, telefone)
                    self.campo_CPF.insert(0, cpf)

