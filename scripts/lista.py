from scripts.interfaces import Dict, Type
from scripts.interfaces import Lista, Usuario, Produto, Dispensa, Residencia

class ListaPessoal(Lista):
  def __init__(self, usuario: int) -> None:
    self.__lista: Dict[int, int] = {}
    self.__usuario = usuario
  
  def __str__(self) -> str:
    pass

  def adicionar_produto(self, novo_produto_id: int, quantidade: int) -> None:
    pass

  def remover_produto(self, produto_id: int, quantidade: int) -> None:
    pass

  def obter_lista(self, dispensa_id: int) -> Dict[int, int]:
    pass

  def valor_compra(self) -> float:
    pass



"""
  Implementação de Lista Geral
"""

class ListaGeral(Lista):
  def __init__(self, residencia_id: int) -> None:
    self.__lista: Dict[int, int] = {}
    self.__residencia = residencia_id
    
  
  def __str__(self) -> str:
    pass

  def adicionar_produto(self, novo_produto: Type["Produto"], quantidade: int) -> None:
    pass

  def remover_produto(self, produto: Type["Produto"], quantidade: int) -> None:
    pass


  def obter_lista(self, dispensa: Type["Dispensa"]) -> Dict[int, int]:
    pass

  def valor_compra(self) -> float:
    pass
