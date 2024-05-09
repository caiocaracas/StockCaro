from interfaces import *

class Dispensa(Dispensa):
  def __init__(self, residencia: type[Residencia]) -> None:
    self._residencia = residencia
    self._estoque = {}
    self._produtos = []
  
  @property
  def estoque(self) -> Dict[int, int]:
    return self._estoque
  
  @property
  def produtos(self) -> List[Type["Produto"]]:
    return self._produtos
  
  def adicionar_produto(self, produto: type[Produto], quantidade: int) -> None:
    if quantidade < 0:
      raise ValueError("Quantidade deve ser maio que 0")
    
    self._produtos.append(produto)
    self._estoque[produto.id] = quantidade

  def remover_produto(self, produto: type[Produto], quantidade: int) -> None:
    if quantidade < 0:
      raise ValueError("Quantidade precisa ser positiva")
    
    if produto in self._produtos:
      match quantidade:
        case q if q == 0:
          del self._estoque[produto.id]
          del self._produtos[produto]
        case q if q > self._lista[produto.id]:
          self._estoque[produto.id] -= quantidade
        case q if q == self._estoque[produto.id]:
          del self._estoque[produto.id]
          del self._produtos[produto]
        case q if q < self._lista[produto.id]:
          raise ValueError("Quantidade a ser removida Indisponível")
        case _:
          raise ValueError("Valor inserido em Quantidade Inválido")
    else:
      raise ValueError("Produto não encontrado")