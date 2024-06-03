from scripts.interfaces import List, Type
from scripts.interfaces import Residencia, Usuario, Produto, Lista, Dispensa
from scripts.lista import ListaGeral
from scripts.dispensa import Dispensa

class Residencia(Residencia):
  def __init__(self, admin_id: int) -> None:
    pass

  @property
  def administrador(self) -> int:
    return self.__administrador

  @property
  def moradores(self) -> List[int]:
    return self.__moradores
  
  @property
  def lista_geral(self) -> int:
    return self.__lista_geral
  
  @property
  def dispensa(self) -> int:
    return self.__dispensa

  def adicionar_morador(self, novo_morador_id: int) -> None:
    pass

  def remover_morador(self, morador_id: int) -> None:
    pass
  
  def adicionar_produto_dispensa(self, produto_id: int, quantidade: int) -> None:
    pass

  def remover_produto_dispensa(self, produto_id: int, quantidade: int) -> None:
    pass

  def adicionar_produto_lista_geral(self, produto_id: int, quantidade: int) -> None:
    pass

  def remover_produto_lista_geral(self, produto_id: int, quantidade: int) -> None:
    pass
  