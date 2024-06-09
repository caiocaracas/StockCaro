from abc import ABC, abstractmethod
from typing import Dict, List, Type
from scripts.Repository import BaseRepository

"""
 Implementação Interface Produto
"""
class ProdutoInterface(ABC):
  @abstractmethod
  def criar_produto(cls, db: Type["BaseRepository"], id_residencia: int, nome: str, 
                    quantidade: int, unid_medida: str = None, categoria: str = None) -> None:
    pass

  @abstractmethod
  def deletar_produto(cls, db: Type["BaseRepository"], id_produto: int) -> None:
    pass
  
  @abstractmethod
  def get_info(cls, db: Type["BaseRepository"], id_produto: int) -> dict:
    pass


"""
  Implementação Interface Lista
"""

class ListaInterface(ABC):
  @abstractmethod
  def adicionar_produto(cls, db: Type["BaseRepository"], id_user: int, novo_produto_id: int, quantidade: int) -> None:
    pass

  @abstractmethod
  def remover_produto(cls, db: Type["BaseRepository"], id_user: int, produto_id: int, quantidade: int) -> None:
    pass
  
  @abstractmethod
  def obter_lista(cls, db: Type["BaseRepository"], id_user: int, dispensa_id: int) -> Dict[int, int]:
    pass

  @abstractmethod
  def obter_lista_compras(cls, db: Type["BaseRepository"], id_user: int, dispensa_id: int) -> dict:
    pass

"""
  Implementação Interface Usuario
"""

class UsuarioInterface(ABC):
  @abstractmethod
  def carregar_usuario(cls, atributos: dict, db: Type["BaseRepository"]) -> Type["UsuarioInterface"]:
    pass

  @abstractmethod
  def salvar_usuario(cls, db: Type["BaseRepository"], nome: str, email: str, senha: str) -> None:
    pass
  
  @abstractmethod
  def excluir_usuario(cls, db: Type["BaseRepository"], id_usuario: int) -> None:
    pass

  @abstractmethod
  def autenticar(self, email: str, senha: str) -> bool:
    pass
  
  @abstractmethod
  def alterar_senha(self, antiga_senha: str, nova_senha: str) -> None:
    pass

  @abstractmethod
  def adicionar_produto_lista(self, novo_produto_id: int, quantidade: int) -> None:
    pass

  @abstractmethod
  def remover_produto_lista(self, produto_id: int, quantidade: int) -> None:
    pass

  @abstractmethod
  def adicionar_produto_dispensa(self, produto_id: int, quantidade: int) -> None:
    pass

  @abstractmethod
  def remover_produto_dispensa(self, produto_id: int, quantidade: int) -> None:
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
  def quitar_dividas(self) -> None:
    pass


"""
  Implementação Interface Dispensa
"""

class DispensaInterface(ABC):
  @abstractmethod
  def estoque(cls) -> Dict[int, int]:
    pass

  @abstractmethod
  def adicionar_produto(cls, db: Type["BaseRepository"], id_residencia: int, produto_id: int, quantidade: int) -> None:
    pass

  @abstractmethod
  def remover_produto(cls, db: Type["BaseRepository"], id_residencia: int, produto_id: int, quantidade: int) -> None:
    pass


"""
  Implementação Interface Residência
"""

class ResidenciaInterface(ABC):
  @abstractmethod
  def criar_residencia(cls, db: Type["BaseRepository"], id_admin: int) -> None:
    pass

  @abstractmethod
  def excluir_residencia(cls, db: Type["BaseRepository"], id_residencia: int) -> None:
    pass

  @abstractmethod
  def info_residencia(cls, db: Type["BaseRepository"], id_residencia: int) -> dict:
    pass

  @abstractmethod
  def adicionar_morador(cls, db: Type["BaseRepository"], id_residencia: int, novo_morador_id: int) -> None:
    pass

  @abstractmethod
  def remover_morador(cls, db: Type["BaseRepository"], morador_id: int) -> None:
    pass

  @abstractmethod
  def adicionar_produto_dispensa(cls, db: Type["BaseRepository"], id_residencia: int, produto_id: int, quantidade: int) -> None:
    pass

  @abstractmethod
  def remover_produto_dispensa(cls, db: Type["BaseRepository"], id_residencia: int, produto_id: int, quantidade: int) -> None:
    pass

  @abstractmethod
  def lista_compras(cls, db: Type["BaseRepository"], id_residencia: int) -> Dict[str, int]:
    pass