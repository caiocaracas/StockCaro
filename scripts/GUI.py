import tkinter as tk
from tkinter import messagebox
from typing import Union
from scripts.usuario import Usuario, Administrador
from scripts.Repository import UserRepository
from scripts.lista import Lista
from scripts.produto import Produto
from scripts.residencia import Residencia
from scripts.dispensa import Dispensa

class GUI:
  def __init__(self, db: UserRepository) -> None:
    self.master = tk.Tk()
    self.master.title("Gerenciador Mercado")
    self.master.geometry("700x400")
    self.master.resizable(False, False)

    self.__db = db
    self.user : Union[Usuario, Administrador] = None

    self.frames = []
    self.frame_anterior = None

    """ Cores """
    self.cor_botao = "#328032"
    self.cor_botao_texto = "#FFFFFF"
    self.cor_bg = "#C0C0C0"
    self.cor_fg = "#000000"
    self.cor_lista_bg = "#D3D3D3"
    self.cor_lista_texto = "#000000"
    self.cor_entrys = "#DCDCDC"
    self.cor_entrys_texto = "#000000"



    """ Frames de Login """
    self.login_frame = tk.Frame(self.master, bg=self.cor_bg)
    self.frames.append(self.login_frame)

    """ Frames de Cadastro """
    self.cadastro_frame = tk.Frame(self.master, bg=self.cor_bg)
    self.frames.append(self.cadastro_frame)

    """ Frames de Usuario """
    self.usuario_frame = tk.Frame(self.master, bg=self.cor_bg)
    self.frames.append(self.usuario_frame)

    """ Frame Administrador"""
    self.admin_frame = tk.Frame(self.master, bg=self.cor_bg)
    self.frames.append(self.admin_frame)

    """ Adicionar Produto """
    self.adicionar_produto_frame = tk.Frame(self.master, bg=self.cor_bg)
    self.frames.append(self.adicionar_produto_frame)

    """ Modificar Lista """
    self.modificar_lista_frame = tk.Frame(self.master, bg=self.cor_bg)
    self.frames.append(self.modificar_lista_frame)

    """ Verificar Dividas """
    self.verificar_dividas_frame = tk.Frame(self.master, bg=self.cor_bg)
    self.frames.append(self.verificar_dividas_frame)

    """ Verificar Dispensa """
    self.verificar_dispensa_frame = tk.Frame(self.master, bg=self.cor_bg)
    self.frames.append(self.verificar_dispensa_frame)

    """ Realizar Compra """
    self.realizar_compra_frame = tk.Frame(self.master, bg=self.cor_bg)
    self.frames.append(self.realizar_compra_frame)
    self.compras = {}

    """ Adicionar Morador """
    self.adicionar_morador_frame = tk.Frame(self.master, bg=self.cor_bg)
    self.frames.append(self.adicionar_morador_frame)

    """ Configurações """
    self.config_frame = tk.Frame(self.master, bg=self.cor_bg)
    self.frames.append(self.config_frame)

    self.show_login()

  """ Screens """

  def login_screen(self) -> None:
    """ Username """
    tk.Label(self.login_frame, text="Email:", bg=self.cor_bg, fg=self.cor_fg).pack()
    
    self.entry_username = tk.Entry(self.login_frame, bg=self.cor_entrys, fg=self.cor_entrys_texto)
    self.entry_username.pack()

    """ Password """
    tk.Label(self.login_frame, text="Senha:", bg=self.cor_bg, fg=self.cor_fg).pack()
    
    self.entry_password = tk.Entry(self.login_frame, show="*", bg=self.cor_entrys, fg=self.cor_entrys_texto)
    self.entry_password.pack()

    """ Botão Login """
    tk.Button(self.login_frame, text="Login", bg=self.cor_botao, fg=self.cor_botao_texto, command=self.efetuar_login).pack(pady=10)

    """ Botão Cadastro """
    tk.Button(self.login_frame, text="Cadastro", bg=self.cor_botao, fg=self.cor_botao_texto, command=self.show_cadastro).pack()


  def cadastro_screen(self) -> None:
    """ Nome """
    tk.Label(self.cadastro_frame, text="Nome:", bg=self.cor_bg, fg=self.cor_fg).pack()
    
    self.entry_name = tk.Entry(self.cadastro_frame, bg=self.cor_entrys, fg=self.cor_entrys_texto)
    self.entry_name.pack()

    """ Email """
    tk.Label(self.cadastro_frame, text="Email", bg=self.cor_bg, fg=self.cor_fg).pack()
    
    self.entry_email = tk.Entry(self.cadastro_frame, bg=self.cor_entrys, fg=self.cor_entrys_texto)
    self.entry_email.pack()

    """" Senha """
    tk.Label(self.cadastro_frame, text="Insira a Senha", bg=self.cor_bg, fg=self.cor_fg).pack()

    self.entry_senha = tk.Entry(self.cadastro_frame, show="*", bg=self.cor_entrys, fg=self.cor_entrys_texto)
    self.entry_senha.pack()

    """ Confirmar Senha """
    tk.Label(self.cadastro_frame, text="Confirme a Senha", bg=self.cor_bg, fg=self.cor_fg).pack()
    
    self.entry_confirmar_senha = tk.Entry(self.cadastro_frame, show="*", bg=self.cor_entrys, fg=self.cor_entrys_texto)
    self.entry_confirmar_senha.pack()

    """ Botão de confirmação """
    tk.Button(self.cadastro_frame, text="Confirmar Cadastro", bg=self.cor_botao, fg=self.cor_botao_texto, command=self.confirmar_cadastro).pack(pady=10)


  def usuario_screen(self) -> None:
    self.frame_anterior = self.show_usuario
    
    """ Bem Vindo """
    tk.Label(self.usuario_frame, text=f"Bem vindo, {self.user.nome}", font=("Helvetica", 16), bg=self.cor_bg, fg=self.cor_fg).pack(side=tk.TOP, pady=10)

    """ Botões a esquerda """
    tk.Button(self.usuario_frame, text="Verificar Dividas",  width=12, height=4, bg=self.cor_botao, fg=self.cor_botao_texto, command=self.show_verificar_dividas  ).pack(anchor=tk.W, padx=5, pady=5)
    tk.Button(self.usuario_frame, text="Realizar Compra",    width=12, height=4, bg=self.cor_botao, fg=self.cor_botao_texto, command=self.show_realizar_compra    ).pack(anchor=tk.W, padx=5, pady=5)
    tk.Button(self.usuario_frame, text="Verificar Dispensa", width=12, height=4, bg=self.cor_botao, fg=self.cor_botao_texto, command=self.show_verificar_dispensa ).pack(anchor=tk.W, padx=5, pady=5)
    tk.Button(self.usuario_frame, text="Configurações",      width=12, height=4, bg=self.cor_botao, fg=self.cor_botao_texto, command=self.show_config             ).pack(anchor=tk.W, padx=5, pady=5)

    """ Lista de Compras """
    tk.Label(self.usuario_frame, text="Lista de Compras", bg=self.cor_bg, fg=self.cor_fg).place(x=525, y=55)

    self.lista_pessoal = tk.Listbox(self.usuario_frame, width=22, height=16, font=("Times new Roman", 10), bg=self.cor_lista_bg, fg=self.cor_lista_texto)
    self.lista_pessoal.place(x=505, y=80)

    """ Botão de Modfiicar Lista """
    tk.Button(self.usuario_frame, text="Modificar Lista", width=15, height=1, bg=self.cor_botao, fg=self.cor_botao_texto, command=self.show_modificar_lista).place(x=500, y=350)

    """ Sair """
    tk.Button(self.usuario_frame, text="Sair", width=5, height=1, bg=self.cor_botao, fg=self.cor_botao_texto, command=self.show_login).place(x=10, y=5)


  def admin_screen(self) -> None:
    self.frame_anterior = self.show_admin
    
    """ Bem Vindo """
    tk.Label(self.admin_frame, text=f"Bem vindo, {self.user.nome}", font=("Helvetica", 16), bg=self.cor_bg, fg=self.cor_fg).pack(side=tk.TOP, pady=10)

    """ Botões a esquerda """
    tk.Button(self.admin_frame, text="Verificar Dividas",  width=12, height=3, bg=self.cor_botao, fg=self.cor_botao_texto, command=self.show_verificar_dividas  ).pack(anchor=tk.W, padx=5, pady=4)
    tk.Button(self.admin_frame, text="Realizar Compra",    width=12, height=3, bg=self.cor_botao, fg=self.cor_botao_texto, command=self.show_realizar_compra    ).pack(anchor=tk.W, padx=5, pady=4)
    tk.Button(self.admin_frame, text="Verificar Dispensa", width=12, height=3, bg=self.cor_botao, fg=self.cor_botao_texto, command=self.show_verificar_dispensa ).pack(anchor=tk.W, padx=5, pady=4)
    tk.Button(self.admin_frame, text="Adicionar Morador",  width=12, height=3, bg=self.cor_botao, fg=self.cor_botao_texto, command=self.show_adicionar_morador  ).pack(anchor=tk.W, padx=5, pady=4)
    tk.Button(self.admin_frame, text="Configurações",      width=12, height=3, bg=self.cor_botao, fg=self.cor_botao_texto, command=self.show_config             ).pack(anchor=tk.W, padx=5, pady=4)

    """ Lista de Compras Pessoal """
    self.lista_pessoal = tk.Listbox(self.admin_frame, width=22, height=17, font=("Times new Roman", 10), bg=self.cor_lista_bg, fg=self.cor_lista_texto)
    self.lista_pessoal.place(x=530, y=80)

    """ Botão de Modfiicar Lista Pessoal """
    tk.Label(self.admin_frame, text="Lista Pessoal", bg=self.cor_bg, fg=self.cor_fg).place(x=565, y=55)
    tk.Button(self.admin_frame, text="Modificar Pessoal", width=15, height=1, bg=self.cor_botao, fg=self.cor_botao_texto, command=self.show_modificar_lista).place(x=525, y=370)

    """ Sair """
    tk.Button(self.admin_frame, text="Sair", width=5, height=1, bg=self.cor_botao, fg=self.cor_botao_texto, command=self.show_login).place(x=10, y=5)


  def adicionar_produto_screen(self) -> None:
    tk.Label(self.adicionar_produto_frame, text="Adicionar Produto", font=("", 15), bg=self.cor_bg, fg=self.cor_fg).pack(side=tk.TOP)
    
    """ Produto Existente """
    tk.Label(self.adicionar_produto_frame, text="Produtos Existentes", font=("", 12), bg=self.cor_bg, fg=self.cor_fg).place(x=15, y=50)

    self.lista_produtos_existentes = tk.Listbox(self.adicionar_produto_frame, width=20, height=10, bg=self.cor_lista_bg, fg=self.cor_lista_texto)
    self.lista_produtos_existentes.place(x=15, y=80)

    tk.Label(self.adicionar_produto_frame, text="Quantidade", bg=self.cor_bg, fg=self.cor_fg).place(x=225, y=245)

    self.quantidade_produto_existente = tk.Entry(self.adicionar_produto_frame, width=5, bg=self.cor_entrys, fg=self.cor_entrys_texto)
    self.quantidade_produto_existente.place(x=310, y=242)

    tk.Button(self.adicionar_produto_frame, text="Adicionar Produto Existente", width=19, height=1, bg=self.cor_botao, fg=self.cor_botao_texto, command=self.adicionar_produto_existente).place(x=500, y=242)

    """ Novo Produto """
    tk.Label(self.adicionar_produto_frame, text="Novo Produto", font=("", 15), bg=self.cor_bg, fg=self.cor_fg).place(x=280, y=310)
    
    tk.Label(self.adicionar_produto_frame, text="Nome do Produto", bg=self.cor_bg, fg=self.cor_fg).place(x=10, y=370)
    
    self.nome_novo_produto = tk.Entry(self.adicionar_produto_frame, width=15, bg=self.cor_entrys, fg=self.cor_entrys_texto)
    self.nome_novo_produto.place(x=130, y=368)

    tk.Label(self.adicionar_produto_frame, text="Tipo", bg=self.cor_bg, fg=self.cor_fg).place(x=285, y=370)
    
    self.tipo_novo_produto = tk.Entry(self.adicionar_produto_frame, width=10, bg=self.cor_entrys, fg=self.cor_entrys_texto)
    self.tipo_novo_produto.place(x=330, y=368)

    tk.Label(self.adicionar_produto_frame, text="Quantidade", bg=self.cor_bg, fg=self.cor_fg).place(x=440, y=370)

    self.quantidade_novo_produto = tk.Entry(self.adicionar_produto_frame, width=5, bg=self.cor_entrys, fg=self.cor_entrys_texto)
    self.quantidade_novo_produto.place(x=525, y=368)

    tk.Button(self.adicionar_produto_frame, text="Adicionar novo produto", width=19, height=1, bg=self.cor_botao, fg=self.cor_botao_texto, command=self.adicionar_novo_produto).place(x=500, y=410)

    """ Botão Confirmação """
    tk.Button(self.adicionar_produto_frame, text="Confirmar", width=20, height=1, bg=self.cor_botao, fg=self.cor_botao_texto, command=self.frame_anterior).place(x=240, y=470)


  def modificar_lista_screen(self) -> None:
    tk.Label(self.modificar_lista_frame, text="Alteração Lista", font=("", 15), bg=self.cor_bg, fg=self.cor_fg).pack(side=tk.TOP)

    """ Lista """
    self.lista_modificar = tk.Listbox(self.modificar_lista_frame, width=40, height=12, bg=self.cor_lista_bg, fg=self.cor_lista_texto)
    self.lista_modificar.place(x=120, y=40)

    """ Quantidade a remover """
    tk.Label(self.modificar_lista_frame, text="Quantidade (0: excluir)", bg=self.cor_bg, fg=self.cor_fg).place(x=120, y=270)
    
    self.quantidade_remover = tk.Entry(self.modificar_lista_frame, width=5, bg=self.cor_entrys, fg=self.cor_entrys_texto)
    self.quantidade_remover.place(x=300, y=270)

    tk.Button(self.modificar_lista_frame, text="Remover", width=5, height=1, bg=self.cor_botao, fg=self.cor_botao_texto, command=self.remover_item_lista).place(x=380, y=265)

    """ Adicionar Produto """
    tk.Button(self.modificar_lista_frame, text="Adicionar Produto", width=20, height=2, bg=self.cor_botao, fg=self.cor_botao_texto, command=self.show_adicionar_produto).place(x=200, y=340)

    """ Confirmar Alterações """
    tk.Button(self.modificar_lista_frame, text="Confirmar Alterações", width=20, height=2, bg=self.cor_botao, fg=self.cor_botao_texto, command=self.frame_anterior).place(x=200, y=400)


  def verificar_dividas_screen(self) -> None:
    tk.Label(self.verificar_dividas_frame, text="Divídas", font=("Haveltica", 16), bg=self.cor_bg, fg=self.cor_fg).place(x=300, y=10)

    self.lista_dividas = tk.Listbox(self.verificar_dividas_frame, width=28, height=15, bg=self.cor_lista_bg, fg=self.cor_lista_texto)
    self.lista_dividas.place(x=50, y=50)

    tk.Button(self.verificar_dividas_frame, text="Quitar Divída", width=12, height=1, bg=self.cor_botao, fg=self.cor_botao_texto, command=self.quitar_divida).place(x=330, y=295)

    self.lista_pendentes = tk.Listbox(self.verificar_dividas_frame, width=25, height=4, bg=self.cor_lista_bg, fg=self.cor_lista_texto)
    self.lista_pendentes.place(x=420, y=50)

    tk.Button(self.verificar_dividas_frame, text="Confirmar Quitação", width=15, height=1, bg=self.cor_botao, fg=self.cor_botao_texto, command=self.confirmar_quitacao).place(x=450, y=135)
    
    tk.Button(self.verificar_dividas_frame, text="Confirmar", width=15, height=1, bg=self.cor_botao, fg=self.cor_botao_texto, command=self.frame_anterior).place(x=270, y=350)


  def verificar_dispensa_screen(self) -> None:
    tk.Label(self.verificar_dispensa_frame, text="Dispensa", font=("Haveltica", 16), bg=self.cor_bg, fg=self.cor_fg).place(x=300, y=10)

    self.lista_dispensa = tk.Listbox(self.verificar_dispensa_frame, width=28, height=15, bg=self.cor_lista_bg, fg=self.cor_lista_texto)
    self.lista_dispensa.place(x=225, y=50)

    tk.Button(self.verificar_dispensa_frame, text="+", font=("", 16), width=1, height=1, bg=self.cor_botao, fg=self.cor_botao_texto, command=self.aumentar_item_dipensa ).place(x=520, y=290)
    tk.Button(self.verificar_dispensa_frame, text="-", font=("", 16), width=1, height=1, bg=self.cor_botao, fg=self.cor_botao_texto, command=self.diminuir_item_dispensa).place(x=570, y=290)

    tk.Button(self.verificar_dispensa_frame, text="Retornar", width=15, height=1, bg=self.cor_botao, fg=self.cor_botao_texto, command=self.frame_anterior).place(x=270, y=350)


  def realizar_compra_screen(self) -> None:
    tk.Label(self.realizar_compra_frame, text="Realizar Compra", font=("Haveltica", 16), bg=self.cor_bg, fg=self.cor_fg).pack(side=tk.TOP)
    
    self.lista_compras = tk.Listbox(self.realizar_compra_frame, width=18, height=18, bg=self.cor_lista_bg, fg=self.cor_lista_texto)
    self.lista_compras.place(x=15, y=25)

    tk.Label(self.realizar_compra_frame, text="Quantidade Comprada", font=("Haveltica", 11), bg=self.cor_bg, fg=self.cor_fg).place(x=220, y=70)
    self.quantidade_comprada = tk.Entry(self.realizar_compra_frame, width=8, bg=self.cor_entrys, fg=self.cor_entrys_texto)
    self.quantidade_comprada.place(x=400, y=68)

    tk.Label(self.realizar_compra_frame, text="Valor Total do Produto", font=("Haveltica", 11), bg=self.cor_bg, fg=self.cor_fg).place(x=220, y=110)
    self.valor_compra_produto = tk.Entry(self.realizar_compra_frame, width=8, bg=self.cor_entrys, fg=self.cor_entrys_texto)
    self.valor_compra_produto.place(x=400, y=108)

    self.lista_compras_inseridas = tk.Listbox(self.realizar_compra_frame, width=18, height=6, bg=self.cor_lista_bg, fg=self.cor_lista_texto)
    self.lista_compras_inseridas.place(x=500, y=200)

    tk.Button(self.realizar_compra_frame, text="Adicionar Produto a Compra", width=20, height=1, bg=self.cor_botao, fg=self.cor_botao_texto, command=self.adicionar_produto_compra).place(x=260, y=150)
    
    tk.Button(self.realizar_compra_frame, text="Confirmar", width=15, height=1, bg=self.cor_botao, fg=self.cor_botao_texto, command=self.confirmar_compra).place(x=270, y=350)


  def adicionar_morador_screen(self) -> None:
    """ Remover Morador """
    tk.Label(self.adicionar_morador_frame, text="Remover Morador", font=("Haveltica", 15), bg=self.cor_bg, fg=self.cor_fg).pack(side=tk.TOP)

    self.lista_moradores = tk.Listbox(self.adicionar_morador_frame, width=25, height=10, bg=self.cor_lista_bg, fg=self.cor_lista_texto)
    self.lista_moradores.place(x=40, y=40)

    tk.Button(self.adicionar_morador_frame, text="Remover Morador", width=20, height=1, bg=self.cor_botao, fg=self.cor_botao_texto, command=self.remover_morador).place(x=300, y=190)

    """ Adicionar Morador """
    tk.Label(self.adicionar_morador_frame, text="Adicionar Morador", font=("Haveltica", 15), bg=self.cor_bg, fg=self.cor_fg).place(x=255, y=240)

    tk.Label(self.adicionar_morador_frame, text="ID do Usuário", bg=self.cor_bg, fg=self.cor_fg).place(x=40, y=290)

    self.id_morador = tk.Entry(self.adicionar_morador_frame, width=10, bg=self.cor_entrys, fg=self.cor_entrys_texto)
    self.id_morador.place(x=140, y=287)

    tk.Button(self.adicionar_morador_frame, text="Adicionar Morador", width=15, height=1, bg=self.cor_botao, fg=self.cor_botao_texto, command=self.adicionar_morador).place(x=300, y=280)

    tk.Button(self.adicionar_morador_frame, text="Confirmar", width=20, height=2, bg=self.cor_botao, fg=self.cor_botao_texto, command=self.frame_anterior).place(x=250, y=350)


  def config_screen(self) -> None:
    tk.Label(self.config_frame, text="Informaçoes de Usuário", font=("Haveltica", 15), bg=self.cor_bg, fg=self.cor_fg).pack(side=tk.TOP)

    tk.Label(self.config_frame, text=f"ID: {self.user.id}", font=("Haveltica", 12), bg=self.cor_bg, fg=self.cor_fg).place(x=15, y=25)

    tk.Label(self.config_frame, text=f"Email: {self.user.email}", font=("Haveltica", 12), bg=self.cor_bg, fg=self.cor_fg).place(x=15, y=55)

    tk.Label(self.config_frame, text=f"ID_Residência: {self.user.residencia}", font=("Haveltica", 12), bg=self.cor_bg, fg=self.cor_fg).place(x=15, y=85)

    if isinstance(self.user, Administrador):
      tk.Button(self.config_frame, text="Excluir Residencia", width=14, height=1, bg=self.cor_botao, fg=self.cor_botao_texto, command=self.excluir_residencia).place(x=530, y=35)
    elif isinstance(self.user, Usuario):
      tk.Button(self.config_frame, text="Criar Residencia", width=14, height=1, bg=self.cor_botao, fg=self.cor_botao_texto, command=self.criar_residencia).place(x=530, y=35)
      if self.user.residencia:
        tk.Button(self.config_frame, text="Sair da Residencia", width=14, height=1, bg=self.cor_botao, fg=self.cor_botao_texto, command=self.sair_da_residencia).place(x=530, y=75)

    tk.Label(self.config_frame, text="Alterar Senha", font=("Haveltica", 14), bg=self.cor_bg, fg=self.cor_fg).place(x=280, y=130)

    tk.Label(self.config_frame, text="Senha Atual").place(x=15, y=180)
    tk.Label(self.config_frame, text="Nova Senha").place(x=15, y=230)

    self.config_senha_atual = tk.Entry(self.config_frame, width=20, show="*", bg=self.cor_entrys, fg=self.cor_entrys_texto)
    self.config_senha_atual.place(x=120, y=177)
    self.config_nova_senha = tk.Entry(self.config_frame, width=20, show="*", bg=self.cor_entrys, fg=self.cor_entrys_texto)
    self.config_nova_senha.place(x=120, y=227)

    tk.Button(self.config_frame, text="Alterar Senha", width=12, bg=self.cor_botao, fg=self.cor_botao_texto, command=self.alterar_senha).place(x=280, y=270)

    tk.Button(self.config_frame, text="Confirmar", bg=self.cor_botao, fg=self.cor_botao_texto, command=self.frame_anterior, width=15, height=2).place(x=265, y=340)
    

  """ Carregar Frames """

  def show_login(self) -> None:
    for frame in self.frames:
      frame.forget()
    
    for widget in self.login_frame.winfo_children():
      widget.destroy()

    self.master.geometry("400x200")
    self.login_screen()
    self.login_frame.pack(fill=tk.BOTH, expand=True)


  def show_cadastro(self) -> None:
    for frame in self.frames:
      frame.forget()
    
    for widget in self.cadastro_frame.winfo_children():
      widget.destroy()

    self.master.geometry("500x300")
    self.cadastro_screen()
    self.cadastro_frame.pack(fill=tk.BOTH, expand=True)


  def show_usuario(self) -> None:
    for frame in self.frames:
      frame.forget()

    for widget in self.usuario_frame.winfo_children():
      widget.destroy()

    self.master.geometry("700x400")
    self.usuario_screen()
    
    try:
      lista = self.user.lista
    except:
      lista = []
    self.atualizar_lista(self.lista_pessoal, lista)
    self.usuario_frame.pack(fill=tk.BOTH, expand=True)


  def show_admin(self) -> None:
    for frame in self.frames:
      frame.forget()

    for widget in self.admin_frame.winfo_children():
      widget.destroy()

    self.master.geometry("700x420")
    self.admin_screen()
    
    try:
      lista = self.user.lista
    except:
      lista = []
    self.atualizar_lista(self.lista_pessoal, lista)
    self.admin_frame.pack(fill=tk.BOTH, expand=True)


  def show_adicionar_produto(self) -> None:
    for frame in self.frames:
      frame.forget()
    
    for widget in self.adicionar_produto_frame.winfo_children():
      widget.destroy()

    self.master.geometry("700x500")
    self.adicionar_produto_screen()

    try:
      lista = list(self.user.database.mostrar_produtos_cadastrados_da_residencia(self.user.residencia).values())
      lista_existentes = [f"{produto['categoria']} -> {produto['nome']}" for produto in lista]
    except:
      lista_existentes = []

    self.atualizar_lista(self.lista_produtos_existentes, lista_existentes)
    self.adicionar_produto_frame.pack(fill=tk.BOTH, expand=True)


  def show_modificar_lista(self) -> None:
    for frame in self.frames:
      frame.forget()
    
    for widget in self.modificar_lista_frame.winfo_children():
      widget.destroy()

    self.master.geometry("600x450")
    self.modificar_lista_screen()
    
    try:
      lista = self.user.lista
    except:
      lista = []
    self.atualizar_lista(self.lista_modificar, lista)

    self.modificar_lista_frame.pack(fill=tk.BOTH, expand=True)


  def show_verificar_dividas(self) -> None:
    for frame in self.frames:
      frame.forget()
    
    for widget in self.verificar_dividas_frame.winfo_children():
      widget.destroy()

    self.master.geometry("700x400")
    self.verificar_dividas_screen()

    try:
      lista = self.user.dividas()
      lista_dividas = []
      for key, value in lista.items():
        nome = self.user.database.buscar_usuario_por_id(key)['nome']
        lista_dividas.append(f"{nome} ---> {value:.2f}")
    except:
      lista_dividas = []
    self.atualizar_lista(self.lista_dividas, lista_dividas)

    if self.user.residencia:
      moradores = Residencia.info_residencia(self.user.database, self.user.residencia)['moradores']
    else:
      moradores = []

    lista = []
    for morador in moradores:
      if self.user.database.buscar_transferencia_pendente(self.user.id, morador):
        nome = self.user.database.buscar_usuario_por_id(morador)['nome']
        lista.append(f"{nome} quitou a divída?")
    self.atualizar_lista(self.lista_pendentes, lista)
    
    self.verificar_dividas_frame.pack(fill=tk.BOTH, expand=True)


  def show_verificar_dispensa(self) -> None:
    for frame in self.frames:
      frame.forget()
    
    for widget in self.verificar_dispensa_frame.winfo_children():
      widget.destroy()

    self.master.geometry("700x400")
    self.verificar_dispensa_screen()

    try:
      estoque = Dispensa.estoque(self.user.database, self.user.residencia)
      itens_dispensa = {}
      for key, value in estoque.items():
        itens_dispensa[value] = Produto.get_info(self.user.database, key)['nome']

      del estoque
    except:
      itens_dispensa = {}

    self.atualizar_lista(self.lista_dispensa, itens_dispensa)
    self.verificar_dispensa_frame.pack(fill=tk.BOTH, expand=True)


  def show_realizar_compra(self) -> None:
    for frame in self.frames:
      frame.forget()

    for widget in self.realizar_compra_frame.winfo_children():
      widget.destroy()

    self.master.geometry("700x400")
    self.realizar_compra_screen()

    try:
      lista = self.user.obter_listas_compra()
      lista_produtos = {}
      for key, value in lista.items():
        if value > 0:
          produto = Produto.get_info(self.user.database, key)
          lista_produtos[produto['nome']] = value
      del lista
    except:
      lista_produtos = {}

    self.atualizar_lista(self.lista_compras, lista_produtos)
    self.realizar_compra_frame.pack(fill=tk.BOTH, expand=True)


  def show_adicionar_morador(self) -> None:
    for frame in self.frames:
      frame.forget()
    
    for widget in self.adicionar_morador_frame.winfo_children():
      widget.destroy()

    self.master.geometry("700x400")
    self.adicionar_morador_screen()

    try:
      lista_moradores_ids = Residencia.info_residencia(self.user.database, self.user.residencia)['moradores']
      usuarios = {}
      for morador in lista_moradores_ids:
        if morador != self.user.id:
          usuarios[morador] = self.user.database.buscar_usuario_por_id(morador)['nome']
    except:
      usuarios = {}

    self.atualizar_lista(self.lista_moradores, usuarios)
    self.adicionar_morador_frame.pack(fill=tk.BOTH, expand=True)


  def show_config(self) -> None:
    for frame in self.frames:
      frame.forget()
    
    for widget in self.config_frame.winfo_children():
      widget.destroy()

    self.master.geometry("700x400")
    self.config_screen()
    self.config_frame.pack(fill=tk.BOTH, expand=True)

 
  """ Métodos complementares """


  def efetuar_login(self) -> None:
    username = self.entry_username.get()
    password = self.entry_password.get()

    if not username or not password:
      messagebox.showerror("Preenchimento Incompleto", "Preencha todos os campos na tela")
      return None
    
    # carregar informações de usuario
    try:
      info = self.__db.login(username)
      
      if self.__db.buscar_residencia_por_admin(info['id_usuario']):
        self.user = Administrador.carregar_admin(info, self.__db)
        tela = self.show_admin
      else:
        self.user = Usuario.carregar_usuario(info, self.__db)
        tela = self.show_usuario
    except RuntimeError as erro:
      messagebox.showerror("Erro", erro)
      return None
    except KeyError:
      messagebox.showerror("ERRO", "Usuário não encontrado")  
      return None

    if self.user.autenticar(username, password):
      tela() 
    else:
      messagebox.showerror("Usuário não cadastrado", "Senha ou Usuário Incorreto(s)")


  def confirmar_cadastro(self) -> None:
    name = self.entry_name.get()
    email = self.entry_email.get()
    senha = self.entry_senha.get()

    if not name or not email or not senha or not self.entry_confirmar_senha.get():
      messagebox.showerror("Campo não Preenchido", "Preencha todos os campos")
      return None
    
    if senha == self.entry_confirmar_senha.get():
      
      try:
        Usuario.salvar_usuario(self.__db, name, email, senha)
      
      except RuntimeError as erro:
        messagebox.showerror("Erro", erro)
        return None

      self.show_login()
    else:
      messagebox.showerror("Novo Usuário Inválido", "Senha incorreta ou Usuario já existente")


  def atualizar_lista(self, lista: tk.Listbox, nova_lista: Union[list, dict]) -> None:
    lista.delete(0, tk.END)
    
    if isinstance(nova_lista, dict):
      for item, quantidade in nova_lista.items():
        lista.insert(tk.END, f"{quantidade} -> {item}")
    elif isinstance(nova_lista, list):
      for item in nova_lista:
        lista.insert(tk.END, item)


  def adicionar_produto_existente(self) -> None:
    indice = self.lista_produtos_existentes.curselection()

    if not indice or not self.quantidade_produto_existente.get():
      messagebox.showerror("Incompleto", "Preencha quantidade e selecione um produto")
      return None
    
    indice = indice[0]
    try:
      quant = int(self.quantidade_produto_existente.get())
      lista_produtos = list(self.user.database.mostrar_produtos_cadastrados_da_residencia(self.user.residencia).keys())
      produto_id = int(lista_produtos[indice])

      del lista_produtos
    except ValueError:
      messagebox.showerror("Qauntidade inválida", "Quantidade deve ser um valor inteiro positivo")
      return None
    
    if quant <= 0:
      messagebox.showerror("Qauntidade inválida", "Quantidade deve ser um valor inteiro positivo")
      return None
    
    try:
      self.user.adicionar_produto_lista(produto_id, quant)
      messagebox.showinfo("Produto Cadastrado", "Produto Cadastrado com sucesso")
    except RuntimeError as erro:
      messagebox.showerror("Erro", erro)


  def adicionar_novo_produto(self) -> None:
    if not self.nome_novo_produto.get() or not self.tipo_novo_produto.get() or not self.quantidade_novo_produto.get():
      messagebox.showerror("Preencha os campos", "Preencha os campos de Novo Produto")
      return None
    
    try:
      nome_produto = self.nome_novo_produto.get()
      tipo = self.tipo_novo_produto.get()
      quant = int(self.quantidade_novo_produto.get())
    except ValueError:
      messagebox.showerror("Valores Inválidos", "Insira valores do tipo string para Nome, Real para preço e inteiro para quantidade")
      return None

    if quant < 0:
      messagebox.showerror("Qauntidade inválida", "Quantidade deve ser um valor inteiro positivo")
      return None
    
    try:
      Produto.criar_produto(self.user.database, self.user.residencia, nome_produto, None, None, tipo)
      produtos = list(self.user.database.mostrar_produtos_cadastrados_da_residencia(self.user.residencia).keys())
      produto_id = produtos[-1]
      
      del produtos

      self.user.adicionar_produto_lista(produto_id, quant)
      messagebox.showinfo("Produto Adicionado", "Novo Produto criado e adicionado com sucesso")
    except RuntimeError as erro:
      messagebox.showerror("Erro", erro)

    self.show_adicionar_produto()


  def remover_item_lista(self) -> None:
    indice = self.lista_modificar.curselection()
    quant = self.quantidade_remover.get()

    if not indice or not quant:
      messagebox.showerror("Operação Incompleta", "Selecione um item e preencha a quantidade")
      return None
    
    try:
      quant = int(quant)
      produto_id = list(Lista.obter_lista(self.user.database, self.user.id).keys())[indice[0]]
      produto_id = int(produto_id)

    except ValueError:
      messagebox.showerror("Valor Inválido", "Quantidade deve ser um valor inteiro")
      return None
    
    if quant < 0:
      messagebox.showerror("Valor Inválido", "Quantidade deve ser maior que 0")
      return None
    
    if quant == 0:
      quant = int(self.lista_modificar.get(indice).split('->')[0][0:-1])
      print(quant)
    
    self.user.remover_produto_lista(produto_id, quant)
    self.show_modificar_lista()


  def remover_morador(self) -> None:
    indice = self.lista_moradores.curselection()

    if not indice:
      messagebox.showerror("Selecione um Morador", "Selecione um morador para remover")
      return None
    
    indice = indice[0]
    moradores = Residencia.info_residencia(self.user.database, self.user.residencia)['moradores']
    moradores.remove(self.user.id)
    morador_id = moradores[indice]
    del moradores
    
    if messagebox.askquestion("Remover Morador", f"Deseja remover o morador de id {morador_id}") == "yes":
      try:
        self.user.remover_morador(morador_id)
        messagebox.showinfo("Operação Realizada com Sucesso", "Usuario removido da residencia")
      except RuntimeError as erro:
        messagebox.showerror("Erro", erro)
    self.show_adicionar_morador()

  
  def aumentar_item_dipensa(self) -> None:
    estoque = Dispensa.estoque(self.user.database, self.user.residencia)
    index = self.lista_dispensa.curselection()

    if not index:
      messagebox.showerror("Selecione um item", "Nenhum item foi selecionado")
      return None

    index = index[0]
    produto_id = list(estoque.keys())[index]

    try:
      self.user.adicionar_produto_dispensa(produto_id, 1)
    except RuntimeError as erro:
      messagebox.showerror("Erro", erro)
    self.show_verificar_dispensa()


  def diminuir_item_dispensa(self) -> None:
    estoque = Dispensa.estoque(self.user.database, self.user.residencia)
    index = self.lista_dispensa.curselection()

    if not index:
      messagebox.showerror("Selecione um item", "Nenhum item foi selecionado")
      return None

    index = index[0]
    produto_id = list(estoque.keys())[index]

    try:
      self.user.remover_produto_dispensa(produto_id, 1)
    except RuntimeError as erro:
      messagebox.showerror("Erro", erro)
    self.show_verificar_dispensa()


  def adicionar_morador(self) -> None:
    novo_morador_id = self.id_morador.get()

    if not novo_morador_id:
      messagebox.showerror("Preencha o campo ID", "Preencha o campo ID")
      return None
    
    try:
      novo_morador_id = int(novo_morador_id)
    except ValueError:
      messagebox.showerror("Valor inválido", "ID é um numero inteiro")

    try:
      if messagebox.askquestion("Adicionar morador", f"Deseka adicionar o morador de id {novo_morador_id} a residencia") == "yes":
        info_morador = self.user.database.buscar_usuario_por_id(novo_morador_id)
        if not info_morador['residencia_id']:
          self.user.adicionar_morador(novo_morador_id)
          messagebox.showinfo("Sucesso", "Morador adicionado com sucesso")
    except RuntimeError as erro:
      messagebox.showerror("Erro", erro)
    self.show_adicionar_morador()


  def quitar_divida(self) -> None:
    indice = self.lista_dividas.curselection()

    if not indice:
      messagebox.showerror("ERRO de SELEÇÃO", "Nenhum item selecionado")
      return None
    
    selecao = self.lista_dividas.get(indice)
    valor = float(selecao.split('--->')[1])
    if valor >= 0:
      del selecao
      del valor
      messagebox.showerror("ERRO", "Você não deve dinheiro para abrir uma quitação de divida")
      return None

    indice = indice[0]
    try:
      id_divida = list(self.user.dividas().keys())[indice]
      if messagebox.askquestion("Confirmar", f"Deseja emitir um pedido de quitação de divida com usuario de id {id_divida}") == "yes":
        self.user.emitir_pedido_quitar_divida(id_divida)
        
    except RuntimeError as erro:
      messagebox.showerror("ERRO", erro)
      return None
    self.show_verificar_dividas()

  
  def confirmar_quitacao(self) -> None:
    indice = self.lista_pendentes.curselection()
    if not indice:
      messagebox.showerror("ERRO de SELEÇÃO", "Nenhum item selecionado")
      return None

    indice = indice[0]
    moradores = Residencia.info_residencia(self.user.database, self.user.residencia)['moradores']
    moradores.remove(self.user.id)

    try:
      if messagebox.askquestion("Confirmação", "Essa divida foi quitada") == "yes":
        self.user.quitar_dividas(moradores[indice])
    except RuntimeError as erro:
      messagebox.showerror("Erro", erro)
      return None
    self.show_verificar_dividas()


  def adicionar_produto_compra(self) -> None:
    indice = self.lista_compras.curselection()
    quantidade = self.quantidade_comprada.get()
    valor = self.valor_compra_produto.get()

    if not indice or not quantidade or not valor:
      messagebox.showerror("Informações Incompletas", "Selecione um item e preencha os campos")
      return None
    
    try:
      indice = indice[0]
      quantidade = int(quantidade)
      valor = float(valor)

      if quantidade <= 0 or valor < 0:
        raise ValueError
    except ValueError:
      messagebox.showerror("Valores Inválidos", "Valores preenchidos inválidos")
      return None
    
    lista_produtos = list(self.user.obter_listas_compra().keys())
    nova_compra = {'quantidade': quantidade, 'valor': valor}
    
    self.compras[lista_produtos[indice]] = nova_compra
    
    lista = []
    for key in list(self.compras.keys()):
      produto = Produto.get_info(self.user.database, key)['nome']
      lista.append(f"{quantidade} x {produto} ---> {valor}")
    
    self.atualizar_lista(self.lista_compras_inseridas, lista)
    del lista


  def confirmar_compra(self) -> None:
    self.user.finalizar_compra(self.compras)
    self.compras = {}

    self.frame_anterior()


  def alterar_senha(self) -> None:
    senha_atual = self.config_senha_atual.get()
    nova_senha = self.config_nova_senha.get()

    if not senha_atual or not nova_senha:
      messagebox.showerror("Preencha os campos de senha", "Preencha ambos campos de senha")
      return None

    if self.user.alterar_senha(senha_atual, nova_senha):
      messagebox.showinfo("Senha Atualizada", f"Senha atualizada para {nova_senha}")
    else:
      messagebox.showerror("Senha não alterada", "Senha atual incorreta")


  def criar_residencia(self) -> None:
    if messagebox.askquestion("Criar Residência", "Deseja criar uma nova residência") == "yes":
      Residencia.criar_residencia(self.user.database, self.user.id)
      messagebox.showinfo("Residencia criada com sucesso", "A Residência foi criada com sucesso, retornando a tela de login")
      self.show_login()

  
  def excluir_residencia(self) -> None:
    if messagebox.askquestion("Excluir Residência", "Deseja exluir essa residência") == "yes":
      Residencia.excluir_residencia(self.user.database, self.user.residencia)
      messagebox.showinfo("Residencia excluída com sucesso", "A Residência foi excluída com sucesso, retornando a tela de login")
      self.show_login()
  

  def sair_da_residencia(self) -> None:
    try:
      if messagebox.askquestion("Confirmação", "Deseja sair dessa residência") == "yes":
        Residencia.remover_morador(self.user.database, self.user.id)
        messagebox.showinfo("Sucesso", "Você foi removido da residência")
        self.show_login()
    except RuntimeError:
      messagebox.showerror("ERRO", "Não foi possível sair dessa residência")


if __name__ == "__main__":
  interface = GUI()
  
  interface.master.mainloop()
