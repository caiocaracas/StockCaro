from interfaces import *

class Residencia(Residencia):
  def __init__(self) -> None:
    pass

  def __str__(self) -> str:
    pass

  @property
  def administrador(self) -> Type["Usuario"]:
    pass

  @property
  def moradores(self) -> List[Type["Usuario"]]:
    pass

  def adicionar_morador(self, novo_morador: Type["Usuario"]) -> None:
    pass

  def remover_morador(self, morador: Type["Usuario"]) -> None:
    pass
  
  def adicionar_produto_dispensa(self, produto: Type["Produto"], quantidade: int) -> None:
    pass

  def remover_produto_dispensa(self, produto: Type["Produto"], quantidade: int) -> None:
    pass