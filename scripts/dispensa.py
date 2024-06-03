from scripts.interfaces import Dict, List
from scripts.interfaces import DispensaInterface

class Dispensa(DispensaInterface):
  @classmethod
  def estoque(cls) -> Dict[int, int]:
    pass

  @classmethod
  def adicionar_produto(cls, id: int, produto_id: int, quantidade: int) -> None:
    pass

  @classmethod
  def remover_produto(cls, id: int, produto_id: int, quantidade: int) -> None:
    pass
