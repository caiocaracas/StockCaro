from scripts.interfaces import Dict
from scripts.interfaces import DispensaInterface
from scripts.Repository import UserRepository

class Dispensa(DispensaInterface):
  @classmethod
  def estoque(cls, db: UserRepository, id_dispensa: int) -> Dict[int, int]:
    try:
      produtos = db.mostrar_produtos_dispensa(id_dispensa)
      estoque = {}
      
      for key, value in produtos.items():
        estoque[key] = value['quantidade_existente']
      
      return estoque
    except RuntimeError:
      raise RuntimeError("Impossível encontrar informações sobre essa dispensa")

  @classmethod
  def adicionar_produto(cls, db: UserRepository, id_dispensa: int, produto_id: int, quantidade: int) -> None:
    try:
      pass
    except RuntimeError:
      raise RuntimeError("Impossível adicionar produto na dispensa")


  @classmethod
  def remover_produto(cls, db: UserRepository, id_dispensa: int, produto_id: int, quantidade: int) -> None:
    try:
      pass
    except RuntimeError:
      raise RuntimeError("Impossível remover produto da dispensa")
