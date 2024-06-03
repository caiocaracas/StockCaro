from scripts.interfaces import List
from scripts.interfaces import Produto

"""
  Implementação de Produto Pessoal
"""

class ProdutoPessoal(Produto):
  def __init__(self, nome_prodto: str, id_produto: int, preco: float, usuarios: List[int]) -> None:
    self.__nome_produto = nome_prodto
    self.__preco = preco
    self.__pertence = usuarios
    self.__id = id_produto
  
  @property
  def nome_produto(self) -> str:
    return self.__nome_produto
  
  @nome_produto.setter
  def nome_produto(self, novo_nome: str) -> None:
    self.__nome_produto = novo_nome
  
  @property
  def id(self) -> int:
    return self.__id
  
  @property
  def preco(self) -> float:
    return self.__preco
  
  @preco.setter
  def preco(self, novo_preco: float) -> None:
    self.__preco = novo_preco
  
  @property
  def pertence(self) -> List[int]:
    return self.__pertence
  
  def adicionar_usuario(self, novo_usuario: int) -> None:
    if novo_usuario not in self.pertence:
      self.__pertence.append(novo_usuario)

  def remover_usuario(self, usuario: int) -> None:
    if usuario in self._pertence:
      self.__pertence.remove(usuario)
    else:
      raise ValueError("Esse usuario não possui esse produto na lista")