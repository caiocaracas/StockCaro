from src.interfaces import Dict, Type, List
from src.interfaces import Dispensa, Residencia, Produto

class Dispensa(Dispensa):
  def __init__(self, residencia: Type[Residencia]) -> None:
    self._residencia = residencia
    self._estoque: Dict[int, int] = {}
    self._produtos: List[Type[Produto]] = []

  @property
  def estoque(self) -> Dict[int, int]:
    return self._estoque

  @property
  def produtos(self) -> List[Type[Produto]]:
    return self._produtos

  def adicionar_produto(self, produto: Type[Produto], quantidade: int) -> None:
    if quantidade < 0:
      raise ValueError("Quantidade deve ser maior que 0")

    self._produtos.append(produto)
    self._estoque[produto.id] = quantidade

  def remover_produto(self, produto: Type[Produto], quantidade: int) -> None:
    if quantidade < 0:
      raise ValueError("Quantidade precisa ser positiva")

    if produto in self._produtos:
      index = self._produtos.index(produto)
      match quantidade:
        case q if q == 0:
          del self._estoque[produto.id]
          del self._produtos[index]
        case q if q > self._estoque[produto.id]:
          self._estoque[produto.id] -= quantidade
        case q if q == self._estoque[produto.id]:
          del self._estoque[produto.id]
          del self._produtos[index]
        case q if q < self._estoque[produto.id]:
          raise ValueError("Quantidade a ser removida Indisponível")
        case _:
          raise ValueError("Valor inserido em Quantidade Inválido")
    else:
      raise ValueError("Produto não encontrado")
