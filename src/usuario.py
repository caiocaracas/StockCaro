from src.interfaces import Dict, Type
from src.interfaces import Usuario, Produto, Residencia
from src.lista import ListaPessoal

class UsuarioComum(Usuario):

  def __init__(self, nome: str, email: str, senha: str) -> None:
    self._nome = nome

    self._email = None
    self._senha = None
    self.email = email
    self.senha = senha

    self._id = Usuario.id_counter
    Usuario.id_counter += 1

    self._lista = ListaPessoal(self)
  
  def __str__(self) -> str:
    return f"User: {self.nome}, Email: {self.email}"

  def __eq__(self, usuario: object) -> bool:
    return self.nome == usuario.nome and self.email == usuario.email
  
  @property
  def id(self) -> int:
    return self._id
  
  @property
  def nome(self) -> str:
    return self._nome

  @property
  def lista(self) -> Type["ListaPessoal"]:
    return self._lista
  
  @property
  def email(self) -> str:
    return self._email

  @email.setter
  def email(self, novo_email: str) -> None:
    splited = novo_email.split("@")
    if len(splited) == 2:
      if len(splited[1].split(".")) in (2, 3):
        self._email = novo_email
      else:
        raise ValueError("Novo email inválido")
    else:
      raise ValueError("Novo email inválido")

  @property
  def senha(self) -> str:
    return self._senha

  @senha.setter
  def senha(self, nova_senha: str) -> None:
    self._senha = nova_senha
  
  def autenticar(self, email: str, senha: str) -> bool:
    return email == self.email and self.senha == senha
  
  def alterar_senha(self, antiga_senha: str, nova_senha: str) -> None:
    if antiga_senha == self.senha:
      self.senha = nova_senha
    else:
      raise ValueError("Senha antiga incorreta")

  def adicionar_produto_lista(self, novo_produto: Type["Produto"], quantidade: int) -> None:
    self._lista.adicionar_produto(novo_produto, quantidade)

  def remover_produto_lista(self, produto: Type["Produto"], quantidade: int) -> None:
    self._lista.remover_produto(produto, quantidade)
  
  @property
  def dividas(self) -> Dict[str, float]:
    pass

  def obter_listas(self) -> Dict[Dict[str, int], float]:
    pass

  def finalizar_compra(self) -> None:
    pass

  def adicionar_produto_dispensa(self, produto: Type["Produto"], quantidade: int) -> None:
    pass

  def remover_produto_dispensa(self, produto: Type["Produto"], quantidade: int) -> None:
    pass


"""
  Implementação de Administrador
"""

class Administrador(UsuarioComum):
  def __init__(self, nome: str, email: str, senha: str, residencia: Type["Residencia"]) -> None:
    super().__init__(nome, email, senha)
    self._residencia = residencia
  
  @property
  def residencia(self) -> Residencia:
    return self._residencia
  
  def adicionar_produto_geral(self, produto: Produto, quantidade: int) -> None:
    self._residencia.adicionar_produto_lista_geral(produto=produto, quantidade=quantidade)

  def remover_produto_geral(self, produto: Produto, quantidade: int) -> None:
    self._residencia.remover_produto_lista_geral(produto=produto, quantidade=quantidade)

  def adicionar_morador(self, morador: UsuarioComum) -> None:
    self._residencia.adicionar_morador(novo_morador=morador)

  def remover_morador(self, morador: UsuarioComum) -> None:
    self._residencia.remover_morador(morador=morador)