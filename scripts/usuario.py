from scripts.interfaces import Dict
from scripts.interfaces import UsuarioInterface

class Usuario(UsuarioInterface):
  def __init__(self, nome: str, email: str, senha: str) -> None:
    self.__nome = nome
    self.__senha = senha
    self.__email = email

  @property
  def id(self) -> int:
    return self.__id
  
  @property
  def nome(self) -> str:
    return self.__nome

  @property
  def lista(self) -> int:
    return self.__lista
  
  @property
  def email(self) -> str:
    return self.__email

  @property
  def __senha(self) -> str:
    return self.__senha

  @__senha.setter
  def senha(self, nova_senha: str) -> None:
    self.__senha = nova_senha
  
  @property
  def dispensa(self) -> int:
    pass

  @property
  def residencia(self) -> int:
    pass
  
  @residencia.setter
  def residencia(self, residencia_id: int) -> None:
    pass
  
  @classmethod
  def carregar_usuario(cls, atributos: Dict) -> 'Usuario':
    pass

  def salvar_usuario(self) -> None:
    pass

  def autenticar(self, email: str, senha: str) -> bool:
    pass
  
  def alterar_senha(self, antiga_senha: str, nova_senha: str) -> None:
    pass

  def adicionar_produto_lista(self, novo_produto_id: int, quantidade: int) -> None:
    pass

  def remover_produto_lista(self, produto_id: int, quantidade: int) -> None:
    pass
  
  def adicionar_produto_dispensa(self, produto_id: int, quantidade: int) -> None:
    pass

  def remover_produto_dispensa(self, produto_id: int, quantidade: int) -> None:
    pass

  def dividas(self) -> Dict[str, float]:
    pass

  def obter_listas(self) -> Dict[Dict[str, int], float]:
    pass

  def finalizar_compra(self) -> None:
    pass


"""
  Implementação de Administrador
"""

class Administrador(Usuario):
  def __init__(self, nome: str, email: str, senha: str, residencia_id: int) -> None:
    super().__init__(nome, email, senha)
    self.__residencia = residencia_id

  def adicionar_produto_geral(self, produto_id: int, quantidade: int) -> None:
    pass

  def remover_produto_geral(self, produto_id: int, quantidade: int) -> None:
    pass

  def adicionar_morador(self, morador_id: int) -> None:
    pass

  def remover_morador(self, morador_id: int) -> None:
    pass