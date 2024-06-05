from scripts.interfaces import Dict
from scripts.interfaces import DispensaInterface
from scripts.Repository import UserRepository

class Dispensa(DispensaInterface):
  @classmethod
  def estoque(cls, db: UserRepository) -> Dict[int, int]:
    pass

  @classmethod
  def adicionar_produto(cls, db: UserRepository, id: int, produto_id: int, quantidade: int) -> None:
    pass

  @classmethod
  def remover_produto(cls, db: UserRepository, id: int, produto_id: int, quantidade: int) -> None:
    pass
