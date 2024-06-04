from abc import ABC, abstractmethod
from typing import Dict, List, Type
from scripts.Repository import BaseRepository

"""
 Implementação Interface Produto
"""
class ProdutoInterface(ABC):
  @abstractmethod
  def get_nome_produto(cls, db: Type["BaseRepository"], id: int) -> str:
    pass

  @abstractmethod
  def set_nome_produto(cls, db: Type["BaseRepository"], id: int, novo_nome: str) -> None:
    pass
  
  @abstractmethod
  def get_preco(cls, db: Type["BaseRepository"], id: int) -> float:
    pass

  @abstractmethod
  def set_preco(cls, db: Type["BaseRepository"], id: int, novo_preco: float) -> None:
    pass

  @abstractmethod
  def pertence(cls, db: Type["BaseRepository"], id: int) -> List[int]:
    pass

  @abstractmethod
  def adicionar_usuario(cls, db: Type["BaseRepository"], id: int, novo_usuario: int) -> None:
    pass

  @abstractmethod
  def remover_usuario(cls, db: Type["BaseRepository"], id: int, usuario: int) -> None:
    pass


"""
  Implementação Interface Lista
"""

class ListaInterface(ABC):
  @abstractmethod
  def adicionar_produto(cls, db: Type["BaseRepository"], id: int, novo_produto_id: int, quantidade: int) -> None:
    pass

  @abstractmethod
  def remover_produto(cls, db: Type["BaseRepository"], id: int, produto_id: int, quantidade: int) -> None:
    pass
  
  @abstractmethod
  def obter_lista(cls, db: Type["BaseRepository"], id: int, dispensa_id: int) -> Dict[int, int]:
    pass

  @abstractmethod
  def valor_compra(cls, db: Type["BaseRepository"], id: int) -> float:
    pass

"""
  Implementação Interface Usuario
"""

class UsuarioInterface(ABC):
  @abstractmethod
  def __init__(self, nome: str, email: str, senha: str) -> None:
    pass
  
  @abstractmethod
  def id(self) -> int:
    pass

  @abstractmethod
  def nome(self) -> str:
    pass

  @abstractmethod
  def lista(self) -> int:
    pass

  @abstractmethod
  def email(self) -> str:
    pass

  @abstractmethod
  def senha(self) -> str:
    pass

  @abstractmethod
  def senha(self, nova_senha: str) -> None:
    pass
  
  @abstractmethod
  def dispensa(self) -> int:
    pass

  @abstractmethod
  def residencia(self) -> int:
    pass
  
  @abstractmethod
  def residencia(self, residencia_id: int) -> None:
    pass
  
  @abstractmethod
  def autenticar(self, email: str, senha: str) -> bool:
    pass

  @abstractmethod
  def alterar_senha(self, nova_senha: str) -> None:
    pass

  @abstractmethod
  def adicionar_produto_lista(self, novo_produto_id: int, quantidade: int) -> None:
    pass

  @abstractmethod
  def remover_produto_lista(self, produto_id: int, quantidade: int) -> None:
    pass
  
  @abstractmethod
  def dividas(self) -> Dict[str, float]:
    pass

  @abstractmethod
  def obter_listas(self) -> Dict[Dict[str, int], float]:
    pass

  @abstractmethod
  def finalizar_compra(self) -> None:
    pass

  @abstractmethod
  def adicionar_produto_dispensa(self, produto_id: int, quantidade: int) -> None:
    pass

  @abstractmethod
  def remover_produto_dispensa(self, produto_id: int, quantidade: int) -> None:
    pass


"""
  Implementação Interface Dispensa
"""

class DispensaInterface(ABC):
  @abstractmethod
  def estoque(cls) -> Dict[int, int]:
    pass

  @abstractmethod
  def adicionar_produto(cls, db: Type["BaseRepository"], id: int, produto_id: int, quantidade: int) -> None:
    pass

  @abstractmethod
  def remover_produto(cls, db: Type["BaseRepository"], id: int, produto_id: int, quantidade: int) -> None:
    pass


"""
  Implementação Interface Residência
"""

class ResidenciaInterface(ABC):
  @abstractmethod
  def administrador(cls, db: Type["BaseRepository"], id: int) -> int:
    pass

  @abstractmethod
  def moradores(cls, db: Type["BaseRepository"], id: int) -> List[int]:
    pass

  @abstractmethod
  def lista_geral(cls, db: Type["BaseRepository"], id: int) -> int:
    pass

  @abstractmethod  
  def dispensa(cls, db: Type["BaseRepository"], id: int) -> int:
    pass

  @abstractmethod
  def adicionar_morador(cls, db: Type["BaseRepository"], id: int, novo_morador_id: int) -> None:
    pass

  @abstractmethod
  def remover_morador(cls, db: Type["BaseRepository"], id: int, morador_id: int) -> None:
    pass
  
  @abstractmethod
  def adicionar_produto_dispensa(cls, db: Type["BaseRepository"], id: int, produto_id: int, quantidade: int) -> None:
    pass

  @abstractmethod
  def remover_produto_dispensa(cls, db: Type["BaseRepository"], id: int, produto_id: int, quantidade: int) -> None:
    pass

  @abstractmethod
  def adicionar_produto_lista_geral(cls, db: Type["BaseRepository"], id: int, produto_id: int, quantidade: int) -> None:
    pass

  @abstractmethod
  def remover_produto_lista_geral(cls, db: Type["BaseRepository"], id: int, produto_id: int, quantidade: int) -> None:
    pass