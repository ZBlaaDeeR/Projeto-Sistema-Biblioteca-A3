 #Importando bibliotecas
from tkinter import ttk   #Importa o módulo ttk, que é o Toolkit Temático do Tkinter.
import tkinter as tk      #Importa o módulo inteiro tkinter com um apelido (tk).
from PIL import Image, ImageTk # usada para abrir, editar, redimensionar e exibir imagens no Python.
from tkinter import messagebox
from CONTROLLER.controllerEmprestimos import EmprestimoController
from VIEW.tela_AtualizarEmprestimo import tela_AtualizarEmprestimo

class tela_HistoricoEmprestimos:
    def __init__(self,root_ref,IDfuncionario=None):
         # Recebe a janela principal
          self.root_ref = root_ref
          self.IDfuncionario = IDfuncionario


        # Cria uma nova janela secundária 
          self.janelaHistoricoEmprestimos = tk.Toplevel()
          self.janelaHistoricoEmprestimos.title("Histórico de Empréstimos")
          largura = 1024
          altura = 768
        
          #Posicionamento do programa(Ao inicia-lo)
          largura_tela = self.janelaHistoricoEmprestimos.winfo_screenwidth()
          altura_tela = self.janelaHistoricoEmprestimos.winfo_screenheight()
          x = (largura_tela - largura) // 2
          y = (altura_tela - altura) // 2
          self.janelaHistoricoEmprestimos.geometry(f"{largura}x{altura}+{x}+{y}")
         

          #Criando o atributo imagem e convertendo ele para tk.
          self.imagem = Image.open(r"C:\Users\allan\OneDrive\Área de Trabalho\atualizeiraid\Projeto Biblioteca\VIEW\imagens\imagembiblioteca.png")
          self.imagem = self.imagem.resize((1024,768)) 
          self.imagem_tk = ImageTk.PhotoImage(self.imagem)

          #Cria a label que será responsavel por exibir e manipular a imagem na janela.
          self.label_imagem = tk.Label(self.janelaHistoricoEmprestimos, image=self.imagem_tk)
          self.label_imagem.image = self.imagem_tk
          self.label_imagem.place(x=0, y=0,relwidth=1, relheight=1)

          
          #criando cor label
          cor1 = "#FFFFFF"
          cor2 = "#B4B4B4"

          #Frame
          self.frame = tk.Frame(self.janelaHistoricoEmprestimos, width=868, height=580,bg=cor2)
          self.frame.place(x=79,y=94)
          self.frame2 = tk.Frame(self.janelaHistoricoEmprestimos, width=868, height=450,bg=cor1)
          self.frame2.place(x=79,y=160)

          #Formatação campos de texto
          self._formatando = False  
          self.var_CPF = tk.StringVar()
          self.var_CPF.trace_add("write", self.formatarcpf)

          #Botões
          self.b_Voltar = tk.Button( self.frame,text='VOLTAR',width=12,height=2,command=self.onClose,relief="raised", overrelief="ridge",bg="light blue",fg="black")
          self.b_Voltar.place(x=25,y=530)
          self.b_Excluir = tk.Button( self.frame,text='EXCLUIR',width=12,height=2,command=self.excluirEmprestimoSelecionado,relief="raised", overrelief="ridge",bg="red",fg="white")
          self.b_Excluir.place(x=745,y=530)
          self.b_Pesquisar = tk.Button( self.frame,text='Pesquisar',width=8,height=2,command=self.pesquisarEmprestimos,relief="raised", overrelief="ridge",bg="light blue",fg="black")
          self.b_Pesquisar.place(x=760,y=15)
          self.b_Atualizar = tk.Button( self.frame,text='Atualizar',width=12,height=2,command=self.abrir_AtualizarEmprestimo,relief="raised", overrelief="ridge",bg="light blue",fg="black")
          self.b_Atualizar.place(x=600,y=530)

          # Texto estático
          label_textoTitulo = tk.Label(self.frame, text="Pesquisar Empréstimo: ", font=("Arial", 14),bg=cor2)
          label_textoTitulo.place(x=16,y=20)


          #Campos de Pesquisa
          self.campo_Pesquisar = tk.Entry(self.frame,width=40, font=("Arial", 18),textvariable=self.var_CPF)
          self.campo_Pesquisar.place(x=220,y=20)

          #Codigo para impedir manipulação da tela
          self.janelaHistoricoEmprestimos.resizable(False, False)

          self.carregarEmprestimos()
          


    #Função responsavel pela formatação do campoCPF
    def formatarcpf(self, *args):
          if self._formatando:
               return

          valor = self.var_CPF.get()
          pos_cursor_bruto = self.campo_Pesquisar.index(tk.INSERT)
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
          self.campo_Pesquisar.after_idle(lambda: self._ajustar_cursor(digitos_antes, novo_formatado, self.campo_Pesquisar))


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

     #Pesquisar os empresitmos de acordo com o digitado
    def pesquisarEmprestimos(self):
      termo = self.campo_Pesquisar.get()
      controller = EmprestimoController()
      resultados = controller.pesquisarEmprestimo(termo)
      # Limpar a tabela antes de exibir os resultados
      for item in self.tree.get_children():
          self.tree.delete(item)

      for emprestimo in resultados:
          self.tree.insert("", "end", values=emprestimo)


    def carregarEmprestimos(self):
        # Cria o Treeview
        colunas = ("ID", "IDLivro", "IDMembro", "Data Emprestimo","Prazo Devolução","Data da Devolução","Situação")
        self.tree = ttk.Treeview(self.frame2, columns=colunas, show='headings')

        # Define os nomes das colunas
        for col in colunas:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)

        self.tree.place(relx=0, rely=0, relwidth=1, relheight=1)

        controller = EmprestimoController()
        emprestimos = controller.exibirLivros()
        
        # Inserir dados na tabela
        for emprestimo in emprestimos:
            self.tree.insert("", "end", values=emprestimo)

    # Função para remover do DB o empréstimo
    def excluirEmprestimoSelecionado(self):
        item_selecionado = self.tree.selection()

        if not item_selecionado:
            messagebox.showwarning("Aviso", "Selecione um empréstimo para excluir.")
            return
        # Obtém os dados da linha selecionada
        valores = self.tree.item(item_selecionado)["values"]
        emprestimo_id = valores[0]  # Supondo que o ID do empréstimo está na primeira coluna

        confirmacao = messagebox.askyesno("Confirmar Exclusão", f"Tem certeza que deseja excluir o empréstimo ID {emprestimo_id}?")
        
        if confirmacao:
            controller = EmprestimoController()
            controller.excluirEmprestimo(emprestimo_id)
            self.tree.delete(item_selecionado)

    def abrir_AtualizarEmprestimo(self):
          item_selecionado = self.tree.selection()

          if not item_selecionado:
               messagebox.showwarning("Aviso", "Selecione um empréstimo para atualizar.")
               return

          valores = self.tree.item(item_selecionado)["values"]

          IDemprestimo = valores[0]  # Primeira coluna
          IDLivro = valores[1]       # Segunda coluna
          IDMembro = valores[2]      # Terceira coluna

          self.janelaHistoricoEmprestimos.withdraw()
          tela_AtualizarEmprestimo(self.janelaHistoricoEmprestimos,IDemprestimo,IDLivro,IDMembro,self.IDfuncionario)


    def onClose(self): 
          self.janelaHistoricoEmprestimos.destroy()
          self.root_ref.deiconify()


      
         


        
        

        