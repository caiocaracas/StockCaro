from src.interfaces import List, Type
from src.interfaces import Residencia, Usuario, Produto, Lista, Dispensa
from src.lista import ListaGeral
from src.dispensa import Dispensa

class Residencia(Residencia):
  def __init__(self, admin: Type["Usuario"]) -> None:
    self._administrador = admin
    self._lista_geral = ListaGeral(self)
    self._dispensa = Dispensa(self)
    self._moradores: List[Type["Usuario"]] = [admin]

  @property
  def administrador(self) -> Type["Usuario"]:
    return self._administrador

  @property
  def moradores(self) -> List[Type["Usuario"]]:
    return self._moradores
  
  @property
  def lista_geral(self) -> Type["Lista"]:
    return self._lista_geral
  
  @property
  def dispensa(self) -> Type["Dispensa"]:
    return self._dispensa

  def adicionar_morador(self, novo_morador: Type["Usuario"]) -> None:
    if novo_morador not in self.moradores:
      self._moradores.append(novo_morador)

  def remover_morador(self, morador: Type["Usuario"]) -> None:
    if morador in self.moradores:
      self._moradores.remove(morador)
  
  def adicionar_produto_dispensa(self, produto: Type["Produto"], quantidade: int) -> None:
    self._dispensa.adicionar_produto(produto, quantidade)

  def remover_produto_dispensa(self, produto: Type["Produto"], quantidade: int) -> None:
    self._dispensa.remover_produto(produto, quantidade)
  
  def adicionar_produto_lista_geral(self, produto: Type["Produto"], quantidade: int) -> None:
    self._lista_geral.adicionar_produto(produto, quantidade)

  def remover_produto_lista_geral(self, produto: Type["Produto"], quantidade: int) -> None:
    self._lista_geral.remover_produto(produto, quantidade)
  