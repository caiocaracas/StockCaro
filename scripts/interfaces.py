from abc import ABC, abstractmethod
from typing import Dict, List, Type

"""
 Implementação Interface Produto
"""
class Produto(ABC):
  @abstractmethod
  def __init__(self, nome_prodto: str, id_produto: int, preco: float, usuarios: List[int]) -> None:
    pass

  @abstractmethod
  def nome_produto(self) -> str:
    pass

  @abstractmethod
  def nome_produto(self, novo_nome: str) -> None:
    pass

  @abstractmethod
  def id(self) -> int:
    pass
  
  @abstractmethod
  def preco(self) -> float:
    pass

  @abstractmethod
  def preco(self, novo_preco: float) -> None:
    pass

  @abstractmethod
  def pertence(self) -> List[int]:
    pass

  @abstractmethod
  def adicionar_usuario(self, novo_usuario: int) -> None:
    pass

  @abstractmethod
  def remover_usuario(self, usuario: int) -> None:
    pass


"""
  Implementação Interface Lista
"""

class Lista(ABC):
  @abstractmethod
  def __init__(self) -> None:
    pass
  
  @abstractmethod
  def __str__(self) -> str:
    pass

  @abstractmethod
  def adicionar_produto(self, novo_produto_id: int, quantidade: int) -> None:
    pass

  @abstractmethod
  def remover_produto(self, produto_id: int, quantidade: int) -> None:
    pass
  
  @abstractmethod
  def obter_lista(self, dispensa_id: int) -> Dict[int, int]:
    pass

  @abstractmethod
  def valor_compra(self) -> float:
    pass

"""
  Implementação Interface Usuario
"""

class Usuario(ABC):
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
  def email(self, novo_email: str) -> None:
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

class Dispensa(ABC):
  @abstractmethod
  def __init__(self, residencia_id: int) -> None:
    pass

  @abstractmethod
  def estoque(self) -> Dict[int, int]:
    pass

  @abstractmethod
  def adicionar_produto(self, produto_id: int, quantidade: int) -> None:
    pass

  @abstractmethod
  def remover_produto(self, produto_id: int, quantidade: int) -> None:
    pass


"""
  Implementação Interface Residência
"""

class Residencia(ABC):
  @abstractmethod
  def __init__(self) -> None:
    pass

  @abstractmethod
  def administrador(self) -> int:
    pass

  @abstractmethod
  def moradores(self) -> List[int]:
    pass

  @abstractmethod
  def lista_geral(self) -> int:
    pass

  @abstractmethod  
  def dispensa(self) -> int:
    pass

  @abstractmethod
  def adicionar_morador(self, novo_morador_id: int) -> None:
    pass

  @abstractmethod
  def remover_morador(self, morador_id: int) -> None:
    pass
  
  @abstractmethod
  def adicionar_produto_dispensa(self, produto_id: int, quantidade: int) -> None:
    pass

  @abstractmethod
  def remover_produto_dispensa(self, produto_id: int, quantidade: int) -> None:
    pass

  @abstractmethod
  def adicionar_produto_lista_geral(self, produto_id: int, quantidade: int) -> None:
    pass

  @abstractmethod
  def remover_produto_lista_geral(self, produto_id: int, quantidade: int) -> None:
    pass