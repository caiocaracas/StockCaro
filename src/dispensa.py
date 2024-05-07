from typing import Dict

class Dispensa:
  """
  Classe que representa uma dispensa de produtos.
  
  Atributos:
    _estoque (dict): Um dicionário que mapeia o ID do produto para a quantidade em estoque.
    
  Métodos:
    estoque() -> Dict[int, int]: Retorna o estoque atual.
    adicionar_produto(produto, quantidade: int) -> None: Adiciona um produto ao estoque.
    remover_produto(produto, quantidade: int) -> None: Remove um produto do estoque.
  """
  def __init__(self) -> None:
    """
    Inicializa a dispensa com um estoque vazio.
    """
    self._estoque: Dict[int, int] = {}

  @property
  def estoque(self) -> Dict[int, int]:
    """
    Retorna o estoque atual.
    
    Returns:
      Dict[int, int]: Um dicionário representando o estoque atual.
    """
    return self._estoque

  def adicionar_produto(self, produto, quantidade: int) -> None:
    """
    Adiciona um produto ao estoque.

    Args:
      produto: O produto a ser adicionado.
      quantidade (int): A quantidade do produto a ser adicionada.
      
    Raises:
      TypeError: Se o produto não for instância da Classe ou das sublcasses de ProdutoBase.
      ValueError se a quantidade for menor que 0
    """
    if not hasattr(produto, "id"):
      raise TypeError("Produto Inválido")
    
    if quantidade < 0:
      raise ValueError("Quantidade de produtos Inválida")
    
    if produto.id in self._estoque:
      self._estoque[produto.id] += quantidade
    else:
      self._estoque[produto.id] = quantidade

  def remover_produto(self, produto, quantidade: int) -> None:
    """
    Remove um produto do estoque.

    Args:
      produto: O produto a ser removido.
      quantidade (int): A quantidade do produto a ser removida.
      
    Raises:
      TypeError: Se o produto não for instância da Classe ou das sublcasses de ProdutoBase.
      ValueError: Se a quantidade removida for maior que a quantidade em estoque ou se o produto não estiver no estoque.
    """
    if not hasattr(produto, "id"):
      raise TypeError("Produto Inválido")
    
    if produto.id in self._estoque:
      if self._estoque[produto.id] >= quantidade: 
        self._estoque[produto.id] -= quantidade
        
        if self._estoque[produto.id] == 0:
          del self._estoque[produto.id]
      else:
        raise ValueError("Quantidade insuficiente na dispensa.")    
    else:
      raise ValueError("O produto não está na dispensa.")
