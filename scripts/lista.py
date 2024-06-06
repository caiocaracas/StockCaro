from scripts.interfaces import Dict
from scripts.interfaces import ListaInterface
from scripts.dispensa import Dispensa
from scripts.Repository import UserRepository

class Lista(ListaInterface):
  @classmethod
  def adicionar_produto(cls, db: UserRepository, id: int, novo_produto_id: int, quantidade: int) -> None:
    try:
      db.adicionar_produto_lista_pessoal(novo_produto_id, id, quantidade)
    except RuntimeError:
      raise RuntimeError(f"Erro ao adicionar o produto de id {novo_produto_id} a lista de id{id}")

  @classmethod
  def remover_produto(cls, db: UserRepository, id: int, produto_id: int, quantidade: int) -> None:
    try:
      db.deletar_produto_lista_pessoal(produto_id, id, quantidade) # Logica não implementada
    except RuntimeError:
      raise RuntimeError(f"Erro ao remover o produto de id {produto_id} a lista de id{id}")
  
  @classmethod
  def obter_lista(cls, db: UserRepository, id: int, dispensa_id: int) -> Dict[int, int]:
    try:
      lista = db.mostrar_produtos_listados_do_usuario(id)
      disp = Dispensa.estoque(db, dispensa_id)
    except RuntimeError:
      raise RuntimeError(f"Erro ao obter uma lista comparando lista de id {id} e dispensa de id {dispensa_id}")


