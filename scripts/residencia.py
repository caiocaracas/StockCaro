from scripts.interfaces import List, Type
from scripts.interfaces import ResidenciaInterface
from scripts.Repository import BaseRepository

class Residencia(ResidenciaInterface):
  @classmethod
  def administrador(cls, db: Type["BaseRepository"], id: int) -> int:
    pass

  @classmethod
  def moradores(cls, db: Type["BaseRepository"], id: int) -> List[int]:
    pass

  @classmethod
  def lista_geral(cls, db: Type["BaseRepository"], id: int) -> int:
    pass

  @classmethod  
  def dispensa(cls, db: Type["BaseRepository"], id: int) -> int:
    pass

  @classmethod
  def adicionar_morador(cls, db: Type["BaseRepository"], id: int, novo_morador_id: int) -> None:
    pass

  @classmethod
  def remover_morador(cls, db: Type["BaseRepository"], id: int, morador_id: int) -> None:
    pass
  
  @classmethod
  def adicionar_produto_dispensa(cls, db: Type["BaseRepository"], id: int, produto_id: int, quantidade: int) -> None:
    pass

  @classmethod
  def remover_produto_dispensa(cls, db: Type["BaseRepository"], id: int, produto_id: int, quantidade: int) -> None:
    pass

  @classmethod
  def adicionar_produto_lista_geral(cls, db: Type["BaseRepository"], id: int, produto_id: int, quantidade: int) -> None:
    pass

  @classmethod
  def remover_produto_lista_geral(cls, db: Type["BaseRepository"], id: int, produto_id: int, quantidade: int) -> None:
    pass