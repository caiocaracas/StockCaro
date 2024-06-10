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
        if value['quantidade_existente'] > 0:
          estoque[key] = value['quantidade_existente']
      
      return estoque
    except RuntimeError:
      raise RuntimeError("Impossível encontrar informações sobre essa dispensa")

  @classmethod
  def adicionar_produto(cls, db: UserRepository, produto_id: int, quantidade: int) -> None:
    if quantidade < 0 or not isinstance(quantidade, int):
      raise RuntimeError("Quantidade tem que ser inteira e positiva")
    
    try:
      db.aumentar_quantidade_produto_dispensa(produto_id, quantidade)
    except RuntimeError:
      raise RuntimeError("Impossível adicionar produto na dispensa")


  @classmethod
  def remover_produto(cls, db: UserRepository, id_dispensa: int, produto_id: int, quantidade: int) -> None:
    if quantidade < 0 or not isinstance(quantidade, int):
      raise RuntimeError("Quantidade tem que ser inteira e positiva")
    
    try:
      estoque = cls.estoque(db, id_dispensa)
      if produto_id in estoque:
        
        if quantidade >= estoque[produto_id]:
          db.deletar_produto_da_dispensa(produto_id)
        else:
          db.diminuir_quantidade_produto_dispensa(produto_id, quantidade)

      else:
        raise RuntimeError("Produto não existe na dispensa")
    except RuntimeError:
      raise RuntimeError("Impossível remover produto da dispensa")
