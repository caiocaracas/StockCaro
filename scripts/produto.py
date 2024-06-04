from scripts.interfaces import List, Type
from scripts.interfaces import ProdutoInterface
from scripts.Repository import BaseRepository

"""
  Implementação de Produto
"""

class Produto(ProdutoInterface):
  @classmethod
  def get_nome_produto(cls, db: Type["BaseRepository"], id: int) -> str:
    pass
  
  @classmethod
  def set_nome_produto(cls, db: Type["BaseRepository"], id: int, novo_nome: str) -> None:
    pass
  
  @classmethod
  def get_preco(cls, db: Type["BaseRepository"], id: int) -> float:
    pass
  
  @classmethod
  def set_preco(cls, db: Type["BaseRepository"], id: int, novo_preco: float) -> None:
    pass

  @classmethod
  def pertence(cls, db: Type["BaseRepository"], id: int) -> List[int]:
    pass

  @classmethod
  def adicionar_usuario(cls, db: Type["BaseRepository"], id: int, novo_usuario: int) -> None:
    pass
  
  @classmethod
  def remover_usuario(cls, db: Type["BaseRepository"], id: int, usuario: int) -> None:
    pass