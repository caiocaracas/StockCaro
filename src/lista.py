from typing import Dict
from abc import ABC, abstractmethod

class ListadeCompras(ABC):
  """
  Classe abstrata que define uma lista de compras.

  Métodos abstratos:
    adicionar_produto(produto, quantidade: int) -> None: Adiciona um produto à lista.
    remover_produto(produto) -> None: Remove um produto da lista.
    listar_produtos() -> Dict[int, int]: Lista os produtos na lista.
  """
  def __init__(self) -> None:
    """
    Inicializa a lista de produtos como um dicionário vazio.
    """
    super().__init__()
    self._lista_de_produtos: Dict[int, int] = {}

  @abstractmethod
  def adicionar_produto(self, produto, quantidade: int) -> None:
    pass

  @abstractmethod
  def remover_produto(self, produto) -> None:
    pass

  @abstractmethod
  def listar_produtos(self) -> Dict[int, int]:
    pass


class ListaGeral(ListadeCompras):
  """
  Classe que representa uma lista de compras geral.

  Atributos:
    residencia: A residência associada à lista.

  Métodos:
    adicionar_produto(produto, quantidade: int) -> None: Adiciona um produto à lista geral.
    remover_produto(produto, quantidade: int = None) -> None: Remove um produto da lista geral.
    listar_produtos() -> Dict[int, int]: Lista os produtos na lista geral.
  """
  def __init__(self, residencia) -> None:
    """
    Inicializa a lista de compras geral.

    Args:
      residencia: A residência associada à lista.
    """
    super().__init__()
    self._residencia = residencia
  
  def adicionar_produto(self, produto, quantidade: int) -> None:
    """
    Adiciona um produto à lista geral.

    Args:
      produto: O produto a ser adicionado.
      quantidade (int): A quantidade do produto a ser adicionada.
    """
    if produto.id in self._lista_de_produtos:
      self._lista_de_produtos[produto.id] += quantidade
    else:
      self._lista_de_produtos[produto.id] = quantidade
    
  @property
  def residencia(self):
    """
    Retorna a residência associada à lista.

    Returns:
      A residência associada à lista.
    """
    return self._residencia

  def remover_produto(self, produto, quantidade: int = None) -> None:
    """
    Remove um produto da lista geral.

    Args:
      produto: O produto a ser removido.
      quantidade (int, opcional): A quantidade do produto a ser removida. Se não especificada, remove o produto completamente.
    
    Raises:
      ValueError: Se o produto não estiver na lista.
    """
    if produto.id in self._lista_de_produtos:
      if quantidade:
        self._lista_de_produtos[produto.id] -= abs(quantidade)
      else:
        del self._lista_de_produtos[produto.id]
    else:
      raise ValueError("O produto não está na lista.")

  def listar_produtos(self) -> Dict[int, int]:
    """
    Lista os produtos na lista geral.

    Returns:
      Um dicionário representando os produtos na lista geral, onde as chaves são os IDs dos produtos e os valores são as quantidades.
    """
    return self._lista_de_produtos


class ListaPessoal(ListadeCompras):
  """
  Classe que representa uma lista de compras pessoal.

  Atributos:
    morador: O usuário associado à lista.

  Métodos:
    adicionar_produto(produto, quantidade: int) -> None: Adiciona um produto à lista pessoal.
    remover_produto(produto, quantidade: int = None) -> None: Remove um produto da lista pessoal.
    listar_produtos() -> Dict[int, int]: Lista os produtos na lista pessoal.
  """
  def __init__(self, usuario) -> None:
    """
    Inicializa a lista de compras pessoal.

    Args:
      usuario: O usuário associado à lista.
    """
    super().__init__()
    self._usuario = usuario

  def adicionar_produto(self, produto, quantidade: int) -> None:
    """
    Adiciona um produto à lista pessoal.

    Args:
      produto: O produto a ser adicionado.
      quantidade (int): A quantidade do produto a ser adicionada.
    
    Raises:
      ValueError: Se a quantidade for negativa.
    """
    if quantidade < 0:
      raise ValueError("Quantidade precisa ser maior que 0")
    
    if produto.id in self._lista_de_produtos:
      self._lista_de_produtos[produto.id] += quantidade
    else:
      self._lista_de_produtos[produto.id] = quantidade

  def remover_produto(self, produto, quantidade: int = None) -> None:
    """
    Remove um produto da lista pessoal.

    Args:
      produto: O produto a ser removido.
      quantidade (int, opcional): A quantidade do produto a ser removida. Se não especificada, remove o produto completamente.
    
    Raises:
      ValueError: Se o produto não estiver na lista.
    """
    if produto.id in self._lista_de_produtos:
      
      if quantidade:
        self._lista_de_produtos[produto.id] -= abs(quantidade)
      else:
        del self._lista_de_produtos[produto.id]
    else:
      raise ValueError("O produto não está na lista.")

  def listar_produtos(self) -> Dict[int, int]:
    """
    Lista os produtos na lista pessoal.

    Returns:
      Um dicionário representando os produtos na lista pessoal, onde as chaves são os IDs dos produtos e os valores são as quantidades.
    """
    return self._lista_de_produtos

  @property
  def morador(self):
    """
    Retorna o usuário associado à lista.

    Returns:
      O usuário associado à lista.
    """
    return self._usuario
