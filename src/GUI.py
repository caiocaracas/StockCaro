import tkinter as tk
from tkinter import messagebox

class GUI:
  def __init__(self, master: tk.Tk) -> None:
    self.master = master
    self.master.resizable(False, False)
    self.master.title("Gerenciador Mercado")
    self.master.geometry("700x400")

    self.frames = []
    self.frame_anterior = None

    """ Frames de Login """
    self.login_frame = tk.Frame(self.master)
    self.login_frame.forget()
    self.frames.append(self.login_frame)

    """ Frames de Cadastro """
    self.cadastro_frame = tk.Frame(self.master)
    self.cadastro_frame.forget()
    self.frames.append(self.cadastro_frame)

    """ Frames de Usuario """
    self.usuario_frame = tk.Frame(self.master)
    self.usuario_frame.forget()
    self.frames.append(self.usuario_frame)

    """ Frame Administrador"""
    self.admin_frame = tk.Frame(self.master)
    self.admin_frame.forget()
    self.frames.append(self.admin_frame)

    """ Adicionar Produto """
    self.adicionar_produto_frame = tk.Frame(self.master)
    self.adicionar_produto_frame.forget()
    self.frames.append(self.adicionar_produto_frame)

    """ Modificar Lista """
    self.modificar_lista_frame = tk.Frame(self.master)
    self.modificar_lista_frame.forget()
    self.frames.append(self.modificar_lista_frame)

    """ Verificar Dividas """
    self.verificar_dividas_frame = tk.Frame(self.master)
    self.verificar_dividas_frame.forget()
    self.frames.append(self.verificar_dividas_frame)

    """ Verificar Dispensa """
    self.verificar_dispensa_frame = tk.Frame(self.master)
    self.verificar_dispensa_frame.forget()
    self.frames.append(self.verificar_dispensa_frame)

    """ Realizar Compra """
    self.realizar_compra_frame = tk.Frame(self.master)
    self.realizar_compra_frame.forget()
    self.frames.append(self.realizar_compra_frame)

    """ Adicionar Morador """
    self.adicionar_morador_frame = tk.Frame(self.master)
    self.adicionar_morador_frame.forget()
    self.frames.append(self.adicionar_morador_frame)

    """ Configurações """
    self.config_frame = tk.Frame(self.master)
    self.config_frame.forget()
    self.frames.append(self.config_frame)

  """ Screens """

  def login_screen(self):
    """ Username """
    tk.Label(self.login_frame, text="Usuário:").pack()
    
    self.entry_username = tk.Entry(self.login_frame)
    self.entry_username.pack()

    """ Password """
    tk.Label(self.login_frame, text="Senha:").pack()
    
    self.entry_password = tk.Entry(self.login_frame, show="*")
    self.entry_password.pack()

    """ Botão Login """
    tk.Button(self.login_frame, text="Login", command=self.efetuar_login).pack(pady=10)

    """ Botão Cadastro """
    tk.Button(self.login_frame, text="Cadastro", command=self.show_cadastro).pack()

  def cadastro_screen(self) -> None:
    """ Nome """
    tk.Label(self.cadastro_frame, text="Nome:").pack()
    
    self.entry_name = tk.Entry(self.cadastro_frame)
    self.entry_name.pack()

    """ Email """
    tk.Label(self.cadastro_frame, text="Email").pack()
    
    self.entry_email = tk.Entry(self.cadastro_frame)
    self.entry_email.pack()

    """" Senha """
    tk.Label(self.cadastro_frame, text="Insira a Senha").pack()

    self.entry_senha = tk.Entry(self.cadastro_frame, show="*")
    self.entry_senha.pack()

    """ Confirmar Senha """
    tk.Label(self.cadastro_frame, text="Confirme a Senha").pack()
    
    self.entry_confirmar_senha = tk.Entry(self.cadastro_frame, show="*")
    self.entry_confirmar_senha.pack()

    """ Botão de confirmação """
    tk.Button(self.cadastro_frame, text="Confirmar Cadastro", command=self.confirmar_cadastro).pack(pady=10)

  def usuario_screen(self, usuario: str) -> None:
    """ Bem Vindo """
    tk.Label(self.usuario_frame, text=f"Bem vindo, {usuario}", font=("Helvetica", 16)).pack(side=tk.TOP, pady=10)

    """ Botões a esquerda """
    tk.Button(self.usuario_frame, text="Verificar Dividas",  width=12, height=4, command=self.show_verificar_dividas  ).pack(anchor=tk.W, padx=5, pady=5)
    tk.Button(self.usuario_frame, text="Realizar Compra",    width=12, height=4, command=self.show_realizar_compra    ).pack(anchor=tk.W, padx=5, pady=5)
    tk.Button(self.usuario_frame, text="Verificar Dispensa", width=12, height=4, command=self.show_verificar_dispensa ).pack(anchor=tk.W, padx=5, pady=5)
    tk.Button(self.usuario_frame, text="Configurações",      width=12, height=4, command=self.show_config             ).pack(anchor=tk.W, padx=5, pady=5)

    """ Lista de Compras """
    tk.Label(self.usuario_frame, text="Lista de Compras").place(relx=0.785, rely=0.1)

    self.lista = tk.Listbox(self.usuario_frame, width=18, height=15, bg="light grey", font=("Times new Roman", 10))
    self.lista.place(relx=0.75, rely=0.15)

    """ Botão de Modfiicar Lista """
    tk.Button(self.usuario_frame, text="Modificar Lista", width=15, height=1, command=self.show_modificar_lista).place(relx=0.75, rely=0.85)

  def admin_screen(self, admin: str) -> None:
    """ Bem Vindo """
    tk.Label(self.admin_frame, text=f"Bem vindo, {admin}", font=("Helvetica", 16)).pack(side=tk.TOP, pady=10)

    """ Botões a esquerda """
    tk.Button(self.admin_frame, text="Verificar Dividas",  width=12, height=3, command=self.show_verificar_dividas  ).pack(anchor=tk.W, padx=5, pady=4)
    tk.Button(self.admin_frame, text="Realizar Compra",    width=12, height=3, command=self.show_realizar_compra    ).pack(anchor=tk.W, padx=5, pady=4)
    tk.Button(self.admin_frame, text="Verificar Dispensa", width=12, height=3, command=self.show_verificar_dispensa ).pack(anchor=tk.W, padx=5, pady=4)
    tk.Button(self.admin_frame, text="Adicionar Morador",  width=12, height=3, command=self.show_adicionar_morador  ).pack(anchor=tk.W, padx=5, pady=4)
    tk.Button(self.admin_frame, text="Configurações",      width=12, height=3, command=self.show_config             ).pack(anchor=tk.W, padx=5, pady=4)

    """ Lista de Compras Geral """
    self.lista_geral = tk.Listbox(self.admin_frame, width=18, height=15, bg="light grey", font=("Times new Roman", 10))
    self.lista_geral.place(relx=0.5, rely=0.15)

    """ Botão de Modfiicar Lista Pessoal """
    tk.Label(self.admin_frame, text="Lista Geral").place(relx=0.56, rely=0.1)
    tk.Button(self.admin_frame, text="Modificar Geral", width=15, height=1).place(relx=0.5, rely=0.85)

    """ Lista de Compras Pessoal """
    self.lista_pessoal = tk.Listbox(self.admin_frame, width=18, height=15, bg="light grey", font=("Times new Roman", 10))
    self.lista_pessoal.place(relx=0.75, rely=0.15)

    """ Botão de Modfiicar Lista Pessoal """
    tk.Label(self.admin_frame, text="Lista Pessoal").place(relx=0.8, rely=0.1)
    tk.Button(self.admin_frame, text="Modificar Pessoal", width=15, height=1).place(relx=0.75, rely=0.85)

  def adicionar_produto_screen(self) -> None:
    tk.Label(self.adicionar_produto_frame, text="Adicionar Produto", font=("", 15)).pack(side=tk.TOP)
    
    """ Produto Existente """
    tk.Label(self.adicionar_produto_frame, text="Produtos Existentes", font=("", 12)).place(x=15, y=50)

    self.produtos_existentes = tk.Listbox(self.adicionar_produto_frame, width=20, height=10)
    self.produtos_existentes.place(x=15, y=80)

    tk.Label(self.adicionar_produto_frame, text="Quantidade").place(x=225, y=245)

    self.quantidade_produto_existente = tk.Entry(self.adicionar_produto_frame, width=5)
    self.quantidade_produto_existente.place(x=310, y=242)

    tk.Button(self.adicionar_produto_frame, text="Adicionar Produto Existente", width=19, height=1, command=self.adicionar_produto_existente).place(x=500, y=242)

    """ Novo Produto """
    tk.Label(self.adicionar_produto_frame, text="Novo Produto", font=("", 15)).place(x=280, y=310)
    
    tk.Label(self.adicionar_produto_frame, text="Nome do Produto").place(x=10, y=370)
    
    self.nome_novo_produto = tk.Entry(self.adicionar_produto_frame, width=15)
    self.nome_novo_produto.place(x=130, y=368)

    tk.Label(self.adicionar_produto_frame, text="Preço").place(x=285, y=370)
    
    self.preco_novo_produto = tk.Entry(self.adicionar_produto_frame, width=10)
    self.preco_novo_produto.place(x=330, y=368)

    tk.Label(self.adicionar_produto_frame, text="Quantidade").place(x=440, y=370)

    self.quantidade_novo_produto = tk.Entry(self.adicionar_produto_frame, width=5)
    self.quantidade_novo_produto.place(x=525, y=368)

    tk.Button(self.adicionar_produto_frame, text="Adicionar novo produto", width=19, height=1, command=self.adicionar_novo_produto).place(x=500, y=410)

    """ Botão Confirmação """
    tk.Button(self.adicionar_produto_frame, text="Confirmar", width=20, height=1, command=self.show_ultimo_frame).place(x=240, y=470)

  def modificar_lista_screen(self) -> None:
    tk.Label(self.modificar_lista_frame, text="Alteração Lista", font=("", 15)).pack(side=tk.TOP)

    """ Lista """
    self.lista_modificar = tk.Listbox(self.modificar_lista_frame, width=40, height=12)
    self.lista_modificar.place(x=120, y=40)

    """ Quantidade a remover """
    tk.Label(self.modificar_lista_frame, text="Quantidade (0: excluir)").place(x=120, y=270)
    
    self.quantidade = tk.Entry(self.modificar_lista_frame, width=5)
    self.quantidade.place(x=300, y=270)

    tk.Button(self.modificar_lista_frame, text="Remover", width=5, height=1).place(x=380, y=265)

    """ Adicionar Produto """
    tk.Button(self.modificar_lista_frame, text="Adicionar Novo Produto", width=20, height=2).place(x=200, y=340)

    """ Confirmar Alterações """
    tk.Button(self.modificar_lista_frame, text="Confirmar Alterações", width=20, height=2).place(x=200, y=400)

  def verificar_dividas_screen(self) -> None:
    pass

  def verificar_dispensa_screen(self) -> None:
    pass

  def realizar_compra_screen(self) -> None:
    pass

  def adicionar_morador_screen(self) -> None:
    pass

  def config_screen(self) -> None:
    pass
  
  
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

  def show_usuario(self, usuario: str) -> None:
    for frame in self.frames:
      frame.forget()
    
    for widget in self.usuario_frame.winfo_children():
      widget.destroy()

    self.master.geometry("700x400")
    self.usuario_screen(usuario)
    self.usuario_frame.pack(fill=tk.BOTH, expand=True)
  
  def show_admin(self, admin: str) -> None:
    for frame in self.frames:
      frame.forget()
    
    for widget in self.admin_frame.winfo_children():
      widget.destroy()

    self.master.geometry("700x420")
    self.admin_screen(admin)
    self.admin_frame.pack(fill=tk.BOTH, expand=True)

  def show_adicionar_produto(self) -> None:
    for frame in self.frames:
      frame.forget()
    
    for widget in self.adicionar_produto_frame.winfo_children():
      widget.destroy()

    self.master.geometry("700x500")
    self.adicionar_produto_screen()
    self.adicionar_produto_frame.pack(fill=tk.BOTH, expand=True)

  def show_modificar_lista(self) -> None:
    for frame in self.frames:
      frame.forget()
    
    for widget in self.modificar_lista_frame.winfo_children():
      widget.destroy()

    self.master.geometry("600x450")
    self.modificar_lista_screen()
    self.modificar_lista_frame.pack(fill=tk.BOTH, expand=True)

  def show_verificar_dividas(self) -> None:
    for frame in self.frames:
      frame.forget()
    
    for widget in self.verificar_dividas_frame.winfo_children():
      widget.destroy()

    self.master.geometry("700x400")
    self.verificar_dividas_screen()
    self.verificar_dividas_frame.pack()

  def show_verificar_dispensa(self) -> None:
    for frame in self.frames:
      frame.forget()
    
    for widget in self.verificar_dispensa_frame.winfo_children():
      widget.destroy()

    self.master.geometry("700x400")
    self.verificar_dispensa_screen()
    self.verificar_dispensa_frame.pack()
  
  def show_realizar_compra(self) -> None:
    for frame in self.frames:
      frame.forget()
    
    for widget in self.realizar_compra_frame.winfo_children():
      widget.destroy()

    self.master.geometry("700x400")
    self.realizar_compra_screen()
    self.realizar_compra_frame.pack()

  def show_adicionar_morador(self) -> None:
    for frame in self.frames:
      frame.forget()
    
    for widget in self.adicionar_morador_frame.winfo_children():
      widget.destroy()

    self.master.geometry("700x400")
    self.adicionar_morador_screen()
    self.adicionar_morador_frame.pack()

  def show_config(self) -> None:
    for frame in self.frames:
      frame.forget()
    
    for widget in self.config_frame.winfo_children():
      widget.destroy()

    self.master.geometry("700x400")
    self.config_screen()
    self.config_frame.pack()

  """ Métodos complementares """

  def efetuar_login(self):
    username = self.entry_username.get()
    password = self.entry_password.get()

    if not username or not password:
      messagebox.showerror("Preenchimento Incompleto", "Preencha todos os campos na tela")
    
    elif username == "Arthur" and password == "1234":
      self.show_usuario(username)
    elif username == "Admin" and password == "admin":
      self.show_admin(username)

  def confirmar_cadastro(self) -> None:
    name = self.entry_name.get()
    email = self.entry_email.get()
    senha = self.entry_senha.get()

    if not name or not email or not senha or not self.entry_confirmar_senha.get():
      messagebox.showerror("Campo não Preenchido", "Preencha todos os campos")
      return None
    
    if senha == self.entry_confirmar_senha.get():
      print(f"{name} - {email} - {senha}")
      self.show_login()
    else:
      messagebox.showerror("Novo Usuário Inválido", "Senha incorreta ou Usuario já existente")
    
  def atualizar_lista(self, lista: tk.Listbox, nova_lista: dict) -> None:
    lista.delete(0, tk.END)
    for item, quantidade in nova_lista:
      lista.insert(tk.END, [item, quantidade])

  def adicionar_produto_existente(self) -> None:
    pass
  
  def adicionar_novo_produto(self) -> None:
    pass

if __name__ == "__main__":
  root = tk.Tk()
  interface = GUI(root)
  interface.show_adicionar_produto()

  root.mainloop()
