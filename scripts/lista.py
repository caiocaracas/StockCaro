from scripts.interfaces import Dict
from scripts.interfaces import ListaInterface
from scripts.Repository import UserRepository

class Lista(ListaInterface):
  @classmethod
  def adicionar_produto(cls, db: UserRepository, id: int, novo_produto_id: int, quantidade: int) -> None:
    pass

  @classmethod
  def remover_produto(cls, db: UserRepository, id: int, produto_id: int, quantidade: int) -> None:
    pass
  
  @classmethod
  def obter_lista(cls, db: UserRepository, id: int, dispensa_id: int) -> Dict[int, int]:
    pass


