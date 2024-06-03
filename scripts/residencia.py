from scripts.interfaces import List
from scripts.interfaces import ResidenciaInterface

class Residencia(ResidenciaInterface):
  @classmethod
  def administrador(cls, id: int) -> int:
    pass

  @classmethod
  def moradores(cls, id: int) -> List[int]:
    pass

  @classmethod
  def lista_geral(cls, id: int) -> int:
    pass

  @classmethod  
  def dispensa(cls, id: int) -> int:
    pass

  @classmethod
  def adicionar_morador(cls, id: int, novo_morador_id: int) -> None:
    pass

  @classmethod
  def remover_morador(cls, id: int, morador_id: int) -> None:
    pass
  
  @classmethod
  def adicionar_produto_dispensa(cls, id: int, produto_id: int, quantidade: int) -> None:
    pass

  @classmethod
  def remover_produto_dispensa(cls, id: int, produto_id: int, quantidade: int) -> None:
    pass

  @classmethod
  def adicionar_produto_lista_geral(cls, id: int, produto_id: int, quantidade: int) -> None:
    pass

  @classmethod
  def remover_produto_lista_geral(cls, id: int, produto_id: int, quantidade: int) -> None:
    pass