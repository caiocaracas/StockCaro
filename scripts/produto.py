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
  def get_info(cls, db: UserRepository, id_produto: int) -> dict:
    try:
      produto = db.mostrar_produto_da_residencia(id_produto)
      return {
        'nome': produto['nome'],
        'id': produto['id_produto_residencia'],
        'categoria': produto['categoria'], 
        'quantidade_unidade': f"{str(produto['quantidade_unid'])} {produto['unidade_de_medida']}",
        'residencia_id': produto['residencia_id']
      }
    
    except RuntimeError:
      raise RuntimeError("Não foi possível encontrar o produto")