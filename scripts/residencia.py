from scripts.interfaces import List, Dict
from scripts.interfaces import ResidenciaInterface
from scripts.Repository import UserRepository

class Residencia(ResidenciaInterface):
  @classmethod
  def administrador(cls, db: UserRepository, id: int) -> int:
    pass

  @classmethod
  def moradores(cls, db: UserRepository, id: int) -> List[int]:
    pass

  @classmethod
  def lista_geral(cls, db: UserRepository, id: int) -> int:
    pass

  @classmethod  
  def dispensa(cls, db: UserRepository, id: int) -> int:
    pass

  @classmethod
  def adicionar_morador(cls, db: UserRepository, id: int, novo_morador_id: int) -> None:
    pass

  @classmethod
  def remover_morador(cls, db: UserRepository, id: int, morador_id: int) -> None:
    pass
  
  @classmethod
  def adicionar_produto_dispensa(cls, db: UserRepository, id: int, produto_id: int, quantidade: int) -> None:
    pass

  @classmethod
  def remover_produto_dispensa(cls, db: UserRepository, id: int, produto_id: int, quantidade: int) -> None:
    pass

  @classmethod
  def adicionar_produto_lista_geral(cls, db: UserRepository, id: int, produto_id: int, quantidade: int) -> None:
    pass

  @classmethod
  def remover_produto_lista_geral(cls, db: UserRepository, id: int, produto_id: int, quantidade: int) -> None:
    pass

  @classmethod
  def lista_compras(cls, db: UserRepository, id_residencia: int) -> Dict[str, int]:
    pass