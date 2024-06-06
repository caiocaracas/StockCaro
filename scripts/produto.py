from scripts.interfaces import List
from scripts.interfaces import ProdutoInterface
from scripts.Repository import UserRepository

"""
  Implementação de Produto
"""

class Produto(ProdutoInterface):
  @classmethod
  def get_nome_produto(cls, db: UserRepository, id: int) -> str:
    try:
      produto = db.get_produto(id)
      return produto['nome']
    except RuntimeError:
      raise RuntimeError("Não foi possível encontrar o produto")
  
  @classmethod
  def set_nome_produto(cls, db: UserRepository, id: int, novo_nome: str) -> None:
    try:
      db.set_produto(id, propriedade="nome", valor=novo_nome)
    except RuntimeError:
      raise RuntimeError("Não foi possível modificar o produto")
  
  @classmethod
  def get_preco(cls, db: UserRepository, id: int) -> float:
    try:
      produto = db.get_produto(id)
      return float(produto['preco'])
    except RuntimeError:
      raise RuntimeError("Não foi possível encontrar o produto")
  
  @classmethod
  def set_preco(cls, db: UserRepository, id: int, novo_preco: float) -> None:
    try:
      db.set_produto(id, propriedade="preco", valor=novo_preco)
    except RuntimeError:
      raise RuntimeError("Não foi possível modificar o produto")

  @classmethod
  def pertence(cls, db: UserRepository, id: int) -> List[int]:
    try:
      produto = db.get_produto(id)
      return produto['pertence']
    except RuntimeError:
      raise RuntimeError("Não foi possível encontrar o produto")

  @classmethod
  def adicionar_usuario(cls, db: UserRepository, id: int, novo_usuario: int) -> None:
    try:
      db.adicionar_usuario_em_produto(id_produto=id, id_usuario=novo_usuario)
    except RuntimeError:
      raise RuntimeError("Não foi possível adicionar usuario na lista de produto")
  
  @classmethod
  def remover_usuario(cls, db: UserRepository, id: int, usuario: int) -> None:
    try:
      db.deletar_usuario_que_consome_um_produto(id, usuario)
    except RuntimeError:
      raise RuntimeError("Não foi possível adicionar usuario na lista de produto")