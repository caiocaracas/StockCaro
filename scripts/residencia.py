from scripts.interfaces import List, Dict
from scripts.interfaces import ResidenciaInterface
from scripts.dispensa import Dispensa
from scripts.lista import Lista
from scripts.Repository import UserRepository

class Residencia(ResidenciaInterface):
  @classmethod
  def administrador(cls, db: UserRepository, id: int) -> int:
    try:
      residencia = db.get_residencia(id)
      return residencia['admin_id']
    except RuntimeError:
      raise RuntimeError("Não foi possível encontrar a residência")

  @classmethod
  def moradores(cls, db: UserRepository, id: int) -> List[int]:
    try:
      residencia = db.get_residencia(id)
      return residencia['moradores']
    except RuntimeError:
      raise RuntimeError("Não foi possível encontrar a residência")

  @classmethod
  def lista_geral(cls, db: UserRepository, id: int) -> int:
    try:
      residencia = db.get_residencia(id)
      return residencia['lista_geral_id']
    except RuntimeError:
      raise RuntimeError("Não foi possível encontrar a residência")

  @classmethod  
  def dispensa(cls, db: UserRepository, id: int) -> int:
    try:
      residencia = db.get_residencia(id)
      return residencia['dispensa_id']
    except RuntimeError:
      raise RuntimeError("Não foi possível encontrar a residência")

  @classmethod
  def adicionar_morador(cls, db: UserRepository, id: int, novo_morador_id: int) -> None:
    try:
      db.adicionar_usuario_em_residencia(id, novo_morador_id)
    except RuntimeError:
      raise RuntimeError(f"Não foi possível adicionar morador {novo_morador_id} em residência {id}")

  @classmethod
  def remover_morador(cls, db: UserRepository, id: int, morador_id: int) -> None:
    try:
      db.remover_usuario_de_residencia(id, morador_id)
    except RuntimeError:
      raise RuntimeError(f"Não foi possível remover morador {morador_id} em residência {id}")
  
  @classmethod
  def adicionar_produto_dispensa(cls, db: UserRepository, id: int, produto_id: int, quantidade: int) -> None:
    try:
      Dispensa.adicionar_produto(db, cls.dispensa(db, id), produto_id, quantidade)
    except RuntimeError:
      raise RuntimeError("Não foi possível adicionar produto na dispensa")

  @classmethod
  def remover_produto_dispensa(cls, db: UserRepository, id: int, produto_id: int, quantidade: int) -> None:
    try:
      Dispensa.remover_produto(db, cls.dispensa(db, id), produto_id, quantidade)
    except RuntimeError:
      raise RuntimeError("Não foi possível remover produto da dispensa")

  @classmethod
  def adicionar_produto_lista_geral(cls, db: UserRepository, id: int, produto_id: int, quantidade: int) -> None:
    try:
      Lista.adicionar_produto(db, cls.lista_geral(db, id), produto_id, quantidade)
    except RuntimeError:
      raise RuntimeError("Não foi possível adicionar produto a lista geral")

  @classmethod
  def remover_produto_lista_geral(cls, db: UserRepository, id: int, produto_id: int, quantidade: int) -> None:
    try:
      Lista.remover_produto(db, cls.lista_geral(db, id), produto_id, quantidade)
    except RuntimeError:
      raise RuntimeError("Não foi possível adicionar produto a lista geral")

  @classmethod
  def lista_compras(cls, db: UserRepository, id_residencia: int) -> Dict[str, int]:
    try:
      moradores = cls.moradores(db, id_residencia)
    except RuntimeError:
      moradores = []
    
    lista_compras = {}
    for morador in moradores:
      pass
    
    return lista_compras