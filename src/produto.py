from src.interfaces import List, Type
from src.interfaces import Produto, Usuario, Residencia

"""
  Implementação de Produto Pessoal
"""

class ProdutoPessoal(Produto):
  def __init__(self, nome_prodto: str, preco: float, usuarios: List[Type["Usuario"]] = []) -> None:
    self._nome_produto = nome_prodto
    self._preco = preco
    self._pertence = usuarios
    self._id = Produto.id_counter
    Produto.id_counter += 1
  
  def __str__(self) -> str:
    return f"{self.id} - {self.nome_produto}: R${self.preco}"
  
  def __eq__(self, produto: Produto) -> bool:
    return self.nome_produto == produto.nome_produto and self.preco == produto.preco
  
  @property
  def nome_produto(self) -> str:
    return self._nome_produto
  
  @nome_produto.setter
  def nome_produto(self, novo_nome: str) -> None:
    self._nome_produto = novo_nome
  
  @property
  def id(self) -> int:
    return self._id
  
  @property
  def preco(self) -> float:
    return self._preco
  
  @preco.setter
  def preco(self, novo_preco: float) -> None:
    self._preco = novo_preco
  
  @property
  def pertence(self) -> List[Type["Usuario"]]:
    return self._pertence
  
  def adicionar_usuario(self, novo_usuario: Type["Usuario"]) -> None:
    if novo_usuario not in self.pertence:
      self._pertence.append(novo_usuario)

  def remover_usuario(self, usuario: Type["Usuario"]) -> None:
    if usuario in self._pertence:
      self._pertence.remove(usuario)
    else:
      raise ValueError("Esse usuario não possui esse produto na lista")


"""
  Implementação de Produto Geral
"""

class ProdutoGeral(ProdutoPessoal):
  def __init__(self, nome_prodto: str, preco: float, residencia: Type["Residencia"] = None) -> None:
    if residencia:
      usuarios = residencia.moradores()
    else:
      usuarios = []
    super().__init__(nome_prodto, preco, usuarios)

