#Importando bibliotecas
from tkinter import ttk   #Importa o módulo ttk, que é o Toolkit Temático do Tkinter.
import tkinter as tk      #Importa o módulo inteiro tkinter com um apelido (tk).
from PIL import Image, ImageTk # usada para abrir, editar, redimensionar e exibir imagens no Python.
from datetime import datetime #Import para facilitar a conversão de datas
from tkinter import messagebox
from CONTROLLER.controllerEmprestimos import EmprestimoController

class tela_AtualizarEmprestimo:
    def __init__(self,root_ref,IDemprestimo,IDLivro,IDMembro,IDfuncionario=None):
         # Recebe a janela principal
          self.root_ref = root_ref
          self.IDLivro = IDLivro
          self.IDMembro = IDMembro
          self.IDemprestimo = IDemprestimo
          self.IDfuncionario = IDfuncionario


        # Cria uma nova janela secundária 
          self.janelaAtualizarEmprestimo = tk.Toplevel()
          self.janelaAtualizarEmprestimo.title("Registrar Empréstimos")
          largura = 1024
          altura = 768
        
          #Posicionamento do programa(Ao inicia-lo)
          largura_tela = self.janelaAtualizarEmprestimo.winfo_screenwidth()
          altura_tela = self.janelaAtualizarEmprestimo.winfo_screenheight()
          x = (largura_tela - largura) // 2
          y = (altura_tela - altura) // 2
          self.janelaAtualizarEmprestimo.geometry(f"{largura}x{altura}+{x}+{y}")
          

          #Criando o atributo imagem e convertendo ele para tk.
          self.imagem = Image.open(r"C:\Users\allan\OneDrive\Área de Trabalho\atualizeiraid\Projeto Biblioteca\VIEW\imagens\imagembiblioteca.png")
          self.imagem = self.imagem.resize((1024,768)) 
          self.imagem_tk = ImageTk.PhotoImage(self.imagem)

          #Cria a label que será responsavel por exibir e manipular a imagem na janela.
          self.label_imagem = tk.Label(self.janelaAtualizarEmprestimo, image=self.imagem_tk)
          self.label_imagem.image = self.imagem_tk
          self.label_imagem.place(x=0, y=0,relwidth=1, relheight=1)

          #Frame
          self.frame = tk.Frame(self.janelaAtualizarEmprestimo, width=678, height=380)
          self.frame.place(x=170,y=220)
          self.frame2 = tk.Frame(self.janelaAtualizarEmprestimo, width=300, height=50)
          self.frame2.place(x=363,y=110)

          # Formatação para o campo de data
          self._formatando = False  
          self.var_data_emprestimo = tk.StringVar()
          self.var_data_emprestimo.trace_add("write", lambda *args: self.formatardata(self.var_data_emprestimo, self.campo_DataEmprestimo))

          self.var_data_devolucao = tk.StringVar()
          self.var_data_devolucao.trace_add("write", lambda *args: self.formatardata(self.var_data_devolucao, self.campo_DataDevolucao))

          self.var_data_real_devolucao = tk.StringVar()
          self.var_data_real_devolucao.trace_add("write", lambda *args: self.formatardata(self.var_data_real_devolucao, self.campo_Devolução))

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
          self.campo_DataEmprestimo= tk.Entry(self.frame,width=14,font=("Arial", 14), textvariable=self.var_data_emprestimo)
          self.campo_DataEmprestimo.place(x=220,y=160)
          self.campo_DataDevolucao = tk.Entry(self.frame,width=14,font=("Arial", 14),textvariable=self.var_data_devolucao)
          self.campo_DataDevolucao.place(x=220,y=220)
          self.campo_Devolução= tk.Entry(self.frame,width=14,font=("Arial", 14), textvariable=self.var_data_real_devolucao)
          self.campo_Devolução.place(x=220,y=280)
          
          #Texto estatico 
          label_textoTitulo = tk.Label(self.frame, text="Titulo do Livro: ", font=("Arial", 14))
          label_textoTitulo.place(x=20,y=40)
          label_textoCPFMembro = tk.Label(self.frame, text="CPF Membro: ", font=("Arial", 14))
          label_textoCPFMembro.place(x=20,y=100)
          label_textoDataEmprestimo = tk.Label(self.frame, text="Emprestado Em: ", font=("Arial", 14))
          label_textoDataEmprestimo.place(x=20,y=160)
          label_textoDataDevolucao = tk.Label(self.frame, text="Prazo para Devolução: ", font=("Arial", 14))
          label_textoDataDevolucao.place(x=20,y=220)
          label_textoDevolucao = tk.Label(self.frame, text="Devolvido em: ", font=("Arial", 14))
          label_textoDevolucao.place(x=20,y=280)
          
          label_textoCadastar = tk.Label(self.frame2, text="Registrar Novo Empréstimo", font=("Arial", 14))
          label_textoCadastar.place(x=30,y=13)

          #Botões
          self.b_Voltar = tk.Button( self.frame,text='VOLTAR',width=12,height=2,command=self.onClose,relief="raised", overrelief="ridge",bg="light blue",fg="black")
          self.b_Voltar.place(x=20,y=320)
          self.b_Salvar = tk.Button( self.frame,text='SALVAR',width=12,height=2,command=self.atualizarEmprestimo,relief="raised", overrelief="ridge",bg="light blue",fg="black")
          self.b_Salvar.place(x=570,y=320)

          #Codigo para impedir manipulação da tela
          self.janelaAtualizarEmprestimo.resizable(False, False)

          self.carregar_detalhes()

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

    def onClose(self):
          self.janelaAtualizarEmprestimo.destroy()
          self.root_ref.deiconify()

     # Função responsável pela formatação do campo de Data (DD/MM/AAAA)
    def formatardata(self, var_data, campo_data):
          if self._formatando:
               return

          valor = var_data.get()

          # Limita o total de caracteres a 10 (DD/MM/AAAA)
          if len(valor) > 10:
               var_data.set(valor[:10])
               return

          pos_cursor_bruto = campo_data.index(tk.INSERT)
          digitos_antes = len([c for c in valor[:pos_cursor_bruto] if c.isdigit()])

          todos_digitos = [c for c in valor if c.isdigit()]
          # Limita os dígitos a 8 (DDMMAAAA)
          if len(todos_digitos) > 8:
               todos_digitos = todos_digitos[:8]

          novo_formatado = ""
          for i, num in enumerate(todos_digitos):
               if i == 2 or i == 4:
                    novo_formatado += "/"
               novo_formatado += num

          # Garante que o resultado também não ultrapasse 10 caracteres
          if len(novo_formatado) > 10:
               novo_formatado = novo_formatado[:10]

          if valor == novo_formatado:
               return

          self._formatando = True
          var_data.set(novo_formatado)
          campo_data.after_idle(lambda: self.ajustarcursor(digitos_antes, novo_formatado, campo_data))
          self._formatando = False

          # Validação da data completa (apenas se tiver 10 caracteres já formatados)
          if len(novo_formatado) == 10:
               try:
                    datetime.strptime(novo_formatado, "%d/%m/%Y")
               except ValueError:
                    messagebox.showerror("Data inválida", f"A data '{novo_formatado}' não é válida.")
                    var_data.set("")


    def carregar_detalhes(self):
        emprestimo = EmprestimoController()

        detalhes = emprestimo.obter_detalhes_emprestimo( self.IDemprestimo,self.IDLivro,self.IDMembro )

        if not detalhes:
            messagebox.showwarning("Aviso", "Não foi possível carregar os detalhes do empréstimo.")
            return

        self.campo_TituloLivro.delete(0, tk.END)
        self.campo_TituloLivro.insert(0, detalhes["Titulo"])

        # 4) preenche o CPF (trace formata)
        self.var_CPF.set(detalhes["CPF"])

        # 5) preenche as datas (DDMMYYYY → trace converte para DD/MM/AAAA)
        self.var_data_emprestimo.set(self.inserir_barras(detalhes["DataEmprestimo"]))
        self.var_data_devolucao.set(self.inserir_barras(detalhes["PrazoDevolucao"]))
        self.var_data_real_devolucao.set(self.inserir_barras(detalhes["DataDevolucao"]))


    def inserir_barras(self, s):
          if not s or len(s) != 8:
               return ""
          return f"{s[:2]}/{s[2:4]}/{s[4:]}"
    
    
    def atualizarEmprestimo(self):
               titulo = self.campo_TituloLivro.get().strip()
               cpf = self.campo_CPFMembro.get().strip()
               data_emprestimo_str = self.campo_DataEmprestimo.get().strip()
               data_prazo_str = self.campo_DataDevolucao.get().strip()
               data_devolucao_str = self.campo_Devolução.get().strip()

               if not titulo or not cpf:
                    messagebox.showwarning("Campos Obrigatórios", "Preencha todos os campos antes de atualizar o empréstimo.")
                    return

               # Função para converter e validar datas
               def converter_data(data_str, nome_campo):
                    if not data_str:
                         return None
                    try:
                         # Converte de DD/MM/YYYY para objeto datetime
                         data_obj = datetime.strptime(data_str, "%d/%m/%Y")
                         # Formata para YYYY-MM-DD (formato MySQL)
                         return data_obj.strftime("%Y-%m-%d")
                    except ValueError:
                         messagebox.showerror("Formato Inválido", f"Formato de data inválido no campo {nome_campo}. Use DD/MM/AAAA.")
                         raise ValueError(f"Formato de data inválido: {nome_campo}")

               try:
                    # Converter todas as datas
                    data_emprestimo = converter_data(data_emprestimo_str, "Data de Empréstimo") if data_emprestimo_str else None
                    data_prazo = converter_data(data_prazo_str, "Prazo de Devolução") if data_prazo_str else None
                    data_devolucao = converter_data(data_devolucao_str, "Data de Devolução") if data_devolucao_str else None

                    controller = EmprestimoController()
                    sucesso = controller.atualizar_emprestimo(
                         titulo, 
                         cpf,
                         data_emprestimo,
                         data_prazo,
                         data_devolucao,
                         self.IDemprestimo
                    )

                    if sucesso:
                         messagebox.showinfo("Sucesso", "Empréstimo atualizado com sucesso!")
                         self.onClose()
                  

               except ValueError:
                    return  # Já foi exibida mensagem de erro na função converter_data
               except Exception as e:
                    messagebox.showerror("Erro Inesperado", f"Ocorreu um erro ao atualizar o empréstimo:\n{str(e)}")
