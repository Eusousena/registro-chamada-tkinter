from tkinter import *

class ChamadaTelefonica:
    def __init__(self):
        self.log = []

    def logchamada(self, nome, numero):
        self.log.append((nome, numero))

    def registrar_chamada(self):
        nome = entrada_nome.get()
        numero = entrada_numero.get()


        # Verifique se os campos não estão vazios
        if nome == "" or numero == "":
            texto_erro["text"] = "Erro: Preencha todos os campos antes de registrar a chamada."
            return

        # Registre a chamada e limpe os campos de entrada
        self.logchamada(nome, numero)
        self.limpar_campos()
        self.atualizar_lista_chamadas()

    def limpar_campos(self):
        # Limpa os campos de entrada e a área de exibição de erros
        entrada_nome.delete(0, 'end')
        entrada_numero.delete(0, 'end')
        texto_erro["text"] = ""

    def atualizar_lista_chamadas(self):
        # Limpa a lista de chamadas e adiciona todas as chamadas registradas
        lista_chamadas.delete(0, 'end')
        for nome, numero in self.log:
            lista_chamadas.insert('end', f"Nome: {nome}, Número: {numero}")

chamada = ChamadaTelefonica()

janela = Tk()    
janela.title('Chamada Telefonica')
janela.geometry("900x800")

texto_orientacao = Label(janela, text='Insira seu nome e número de telefone')
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

# Widgets de Entrada para Nome e Número de Telefone
entrada_nome = Entry(janela)
entrada_nome.grid(column=0, row=1, padx=10, pady=10)
entrada_nome.focus()  # Define o foco inicial no campo de entrada do nome

entrada_numero = Entry(janela)
entrada_numero.grid(column=0, row=2, padx=10, pady=10)

# Botão para Registrar a Chamada
botao_registrar = Button(janela, text="Registrar Chamada", command=chamada.registrar_chamada)
botao_registrar.grid(column=0, row=3, padx=10, pady=10)

# Botão para Limpar os Campos
botao_limpar = Button(janela, text="Limpar Campos", command=chamada.limpar_campos)
botao_limpar.grid(column=1, row=3, padx=10, pady=10)

# Widget de Lista para Exibir Chamadas Registradas
lista_chamadas = Listbox(janela, width=50)
lista_chamadas.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

# Texto de Erro (para exibir mensagens de erro)
texto_erro = Label(janela, text='', fg='red')
texto_erro.grid(column=0, row=5, columnspan=2)

janela.mainloop()
