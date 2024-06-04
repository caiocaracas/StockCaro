from scripts.interfaces import Dict, Type
from scripts.interfaces import ListaInterface
from scripts.Repository import BaseRepository

class Lista(ListaInterface):
  @classmethod
  def adicionar_produto(cls, db: Type["BaseRepository"], id: int, novo_produto_id: int, quantidade: int) -> None:
    pass

  @classmethod
  def remover_produto(cls, db: Type["BaseRepository"], id: int, produto_id: int, quantidade: int) -> None:
    pass
  
  @classmethod
  def obter_lista(cls, db: Type["BaseRepository"], id: int, dispensa_id: int) -> Dict[int, int]:
    pass

  @classmethod
  def valor_compra(cls, db: Type["BaseRepository"], id: int) -> float:
    pass

