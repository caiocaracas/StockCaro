from scripts.interfaces import Dict
from scripts.interfaces import ListaInterface
from scripts.dispensa import Dispensa
from scripts.Repository import UserRepository

class Lista(ListaInterface):
  @classmethod
  def adicionar_produto(cls, db: UserRepository, id_user: int, novo_produto_id: int, quantidade: int) -> None:
    if quantidade <= 0 or not isinstance(quantidade, int):
      raise RuntimeError("Quantidade deve ser inteira e maior que 0")
    
    try:
      lista = cls.obter_lista(db, id_user)
      if novo_produto_id not in lista:
        db.adicionar_produto_lista_pessoal(novo_produto_id, id_user, quantidade)
      else:
        db.aumentar_quantidade_produto_lista_pessoal(id_user, novo_produto_id, quantidade)

    except RuntimeError:
      raise RuntimeError(f"Erro ao adicionar o produto de id {novo_produto_id} a lista de id{id}")


  @classmethod
  def remover_produto(cls, db: UserRepository, id_user: int, produto_id: int, quantidade: int) -> None:
    if quantidade <= 0 or not isinstance(quantidade, int):
      raise RuntimeError("Quantidade deve ser inteira e maior que 0")
    
    lista = cls.obter_lista(db, id_user)
    try:
      if produto_id in lista:
        if quantidade >= lista[produto_id]:
          db.deletar_produto_lista_pessoal(id_user, produto_id)
        else:
          db.diminuir_quantidade_produto_lista_pessoal(id_user, produto_id, quantidade)
      else:
        raise RuntimeError("Produto não está na lista pessoal")
    except RuntimeError:
      raise RuntimeError(f"Erro ao remover o produto de id {produto_id} a lista de id{id}")
  
  
  @classmethod
  def obter_lista(cls, db: UserRepository, id_user: id) -> Dict[int, int]:
    try:
      produtos = db.mostrar_produtos_lista_pessoal(id_user)
      lista = {}
      
      for key, value in produtos.items():
        lista[key] = value['quantidade_listada']

      return lista
    
    except RuntimeError:
      raise RuntimeError(f"Erro ao obter lista do usuario com id {id_user}")

  
  @classmethod
  def obter_lista_compras(cls, db: UserRepository, id_user: int, dispensa_id: int) -> Dict[int, int]:
    try:
      lista = cls.obter_lista(db, id_user)
      disp = Dispensa.estoque(db, dispensa_id)

      lista_compras = {}
      for key, value in lista.items():
        if key in disp:
          lista_compras[key] = value - disp[key]
        else:
          lista_compras[key] = value
        lista_compras[key] = lista_compras[key] if lista_compras[key] > 0 else 0
      
      del lista
      del disp

      return lista_compras
    
    except RuntimeError:
      raise RuntimeError(f"Erro ao obter uma lista comparando lista de id {id_user} e dispensa de id {dispensa_id}")


