from scripts.interfaces import List
from scripts.interfaces import ProdutoInterface

"""
  Implementação de Produto
"""

class Produto(ProdutoInterface):
  @classmethod
  def get_nome_produto(cls, id: int) -> str:
    pass
  
  @classmethod
  def set_nome_produto(cls, id: int, novo_nome: str) -> None:
    pass
  
  @classmethod
  def get_preco(cls, id: int) -> float:
    pass
  
  @classmethod
  def set_preco(cls, id: int, novo_preco: float) -> None:
    pass

  @classmethod
  def pertence(cls, id: int) -> List[int]:
    pass

  @classmethod
  def adicionar_usuario(cls, id: int, novo_usuario: int) -> None:
    pass
  
  @classmethod
  def remover_usuario(cls, id: int, usuario: int) -> None:
    pass