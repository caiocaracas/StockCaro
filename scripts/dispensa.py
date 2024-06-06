from scripts.interfaces import Dict
from scripts.interfaces import DispensaInterface
from scripts.Repository import UserRepository

class Dispensa(DispensaInterface):
  @classmethod
  def estoque(cls, db: UserRepository, id_dispensa: int) -> Dict[int, int]:
    try:
      estoque = db.mostrar_produtos_dispensa(id_dispensa)
      return estoque
    except RuntimeError:
      raise RuntimeError("Impossível encontrar informações sobre essa dispensa")

  @classmethod
  def adicionar_produto(cls, db: UserRepository, id: int, produto_id: int, quantidade: int) -> None:
    """ Esperando adição do id da residência na dispensa """
    try:
      db.adicionar_produto_na_dispensa(produto_id, quantidade)
    except RuntimeError:
      raise RuntimeError("Impossível adicionar produto na dispensa")


  @classmethod
  def remover_produto(cls, db: UserRepository, id: int, produto_id: int, quantidade: int) -> None:
    """ Esperando adição do id da residência na dispensa e criação do metodo abaixo """
    try:
      db.deletar_produto_da_dispensa()
    except RuntimeError:
      raise RuntimeError("Impossível remover produto da dispensa")
