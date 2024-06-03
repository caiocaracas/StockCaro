from scripts.interfaces import Dict, Type, List
from scripts.interfaces import Dispensa, Residencia, Produto

class Dispensa(Dispensa):
  def __init__(self, residencia_id: int) -> None:
    self.__residencia = residencia_id
    self.__estoque: Dict[int, int] = {}
    self._produtos: List[int] = []

  def __str__(self) -> str:
    pass


  @property
  def estoque(self) -> Dict[int, int]:
    return self.__estoque

  def adicionar_produto(self, produto_id: int, quantidade: int) -> None:
    pass

  def remover_produto(self, produto_id: int, quantidade: int) -> None:
    pass
