from dispensa import Dispensa
from lista import ListaGeral, ListaPessoal

from typing import List, Dict

class Residencia:
  """
  Classe que representa uma residência.

  Atributos:
    _administrador: O administrador da residência.
    _moradores (list): Uma lista de moradores da residência.
    _dispensa (Dispensa): A dispensa da residência.
    _lista_geral (ListaGeral): A lista de compras geral da residência.
    _lista_pessoal (dict): Um dicionário que mapeia o e-mail dos moradores para suas respectivas listas de compras pessoais.

  Métodos:
    administrador() -> object: Retorna o administrador da residência.
    moradores() -> List: Retorna a lista de moradores da residência.
    dispensa() -> Dispensa: Retorna a dispensa da residência.
    lista_geral() -> ListaGeral: Retorna a lista de compras geral da residência.
    lista_pessoal() -> Dict: Retorna as listas de compras pessoais dos moradores.
    adicionar_morador(admin, morador) -> None: Adiciona um novo morador à residência.
    remover_morador(admin, morador) -> None: Remove um morador da residência.
  """
  def __init__(self, administrador) -> None:
    """
    Inicializa uma residência com um administrador.

    Args:
      administrador: O administrador da residência.
    """
    self._administrador = administrador
    self._administrador.residencia(self)
    
    self._moradores: List = []
    self._dispensa = Dispensa()
    self._lista_geral = ListaGeral()
    self._lista_pessoal: Dict = {}

  @property
  def administrador(self):
    """
    Retorna o administrador da residência.

    Returns:
      O administrador da residência.
    """
    return self._administrador

  @property
  def moradores(self) -> List:
    """
    Retorna a lista de moradores da residência.

    Returns:
      Uma lista de moradores da residência.
    """
    return self._moradores

  @property
  def dispensa(self) -> Dispensa:
    """
    Retorna a dispensa da residência.

    Returns:
      A dispensa da residência.
    """
    return self._dispensa

  @property
  def lista_geral(self) -> ListaGeral:
    """
    Retorna a lista de compras geral da residência.

    Returns:
      A lista de compras geral da residência.
    """
    return self._lista_geral

  @property
  def lista_pessoal(self) -> Dict:
    """
    Retorna as listas de compras pessoais dos moradores.

    Returns:
      Um dicionário que mapeia o e-mail dos moradores para suas respectivas listas de compras pessoais.
    """
    return self._lista_pessoal

  def adicionar_morador(self, admin, morador) -> None:
    """
    Adiciona um novo morador à residência.

    Args:
      admin: O administrador que está adicionando o morador.
      morador: O morador a ser adicionado.

    Raises:
      AssertionError: Se o administrador não estiver credenciado a essa residência.
    """
    if admin != self.administrador:
      raise AssertionError("Administrador não credenciado a essa Residência")
    
    self._moradores.append(morador)
    self._lista_pessoal[morador.email] = ListaPessoal(morador)

  def remover_morador(self, admin, morador) -> None:
    """
    Remove um morador da residência.

    Args:
      admin: O administrador que está removendo o morador.
      morador: O morador a ser removido.

    Raises:
      AssertionError: Se o administrador não estiver credenciado a essa residência.
      ValueError: Se o morador não estiver na residência.
    """
    if admin != self.administrador:
      raise AssertionError("Administrador não credenciado a essa Residência")

    if morador in self._moradores:
      self._moradores.remove(morador)
      del self._lista_pessoal[morador.email]
    else:
      raise ValueError("O morador não está na residência.")
