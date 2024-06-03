from scripts.interfaces import Dict, Type
from scripts.interfaces import ListaInterface

class Lista(ListaInterface):
  @classmethod
  def adicionar_produto(cls, id: int, novo_produto_id: int, quantidade: int) -> None:
    pass

  @classmethod
  def remover_produto(cls, id: int, produto_id: int, quantidade: int) -> None:
    pass
  
  @classmethod
  def obter_lista(cls, id: int, dispensa_id: int) -> Dict[int, int]:
    pass

  @classmethod
  def valor_compra(cls, id: int) -> float:
    pass

