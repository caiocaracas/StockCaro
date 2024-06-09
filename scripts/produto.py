from scripts.interfaces import List
from scripts.interfaces import ProdutoInterface
from scripts.Repository import UserRepository

"""
  Implementação de Produto
"""

class Produto(ProdutoInterface):
  @classmethod
  def criar_produto(cls, db: UserRepository, id_residencia: int, nome: str, quantidade: int, unid_medida: str = None, categoria: str = None) -> None:
    try:
      db.registrar_produto_residencia(id_residencia, nome, quantidade, unid_medida, categoria)
    except RuntimeError:
      raise RuntimeError("Não foi possível cadastrar o produto")
  
  @classmethod
  def deletar_produto(cls, db: UserRepository, id_produto: int) -> None:
    try:
      db.deletar_produto_residencia(id_produto)
    except RuntimeError:
      raise RuntimeError(f"Não foi possivel deletar o produto de id {id_produto}")

  @classmethod
  def get_nome_produto(cls, db: UserRepository, id_produto: int) -> str:
    try:
      produto = db.mostrar_produto_da_residencia(id_produto)
      return produto['nome']
    except RuntimeError:
      raise RuntimeError("Não foi possível encontrar o produto")
  
  @classmethod
  def get_preco(cls, db: UserRepository, id_produto: int) -> float:
    try:
      produto = db.mostrar_produto_da_residencia(id_produto)
      return produto['preco_medio']
    except RuntimeError:
      raise RuntimeError("Não foi possível encontrar o produto")

  @classmethod
  def pertence(cls, db: UserRepository, id_produto: int) -> List[int]:
    try:
      users = db.mostrar_usuarios_consomem_certo_produto(id_produto)
      return list(users.keys())
    except RuntimeError:
      raise RuntimeError("Não foi possível encontrar o produto")

  @classmethod
  def adicionar_usuario(cls, db: UserRepository, id_produto: int, novo_usuario: int) -> None:
    try:
      db.registrar_usuario_consumidor_de_um_produto(id_produto, novo_usuario)
    except RuntimeError:
      raise RuntimeError("Não foi possível adicionar usuario na lista de produto")
  
  @classmethod
  def remover_usuario(cls, db: UserRepository, id_produto: int, usuario: int) -> None:
    try:
      db.deletar_usuario_que_consome_um_produto(id_produto, usuario)
    except RuntimeError:
      raise RuntimeError("Não foi possível adicionar usuario na lista de produto")