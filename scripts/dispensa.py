from scripts.interfaces import Dict, Type
from scripts.interfaces import DispensaInterface
from scripts.Repository import BaseRepository

class Dispensa(DispensaInterface):
  @classmethod
  def estoque(cls, db: Type["BaseRepository"]) -> Dict[int, int]:
    pass

  @classmethod
  def adicionar_produto(cls, db: Type["BaseRepository"], id: int, produto_id: int, quantidade: int) -> None:
    pass

  @classmethod
  def remover_produto(cls, db: Type["BaseRepository"], id: int, produto_id: int, quantidade: int) -> None:
    pass
