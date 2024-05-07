from abc import ABC, abstractmethod

class ProdutoBase(ABC):
  """
  Classe abstrata que define um produto base.

  Atributos:
    _id_counter (int): Um contador estático para gerar IDs únicos para os produtos.

  Métodos abstratos:
    __str__() -> str: Representação do objeto como uma string.
    __eq__(objeto: object) -> bool: Verifica se dois objetos são iguais.

  Propriedades:
    id (int): O ID do produto.
    produto (str): O nome do produto.
    categoria (str): A categoria do produto.
    preco (float): O preço do produto.
  """
  _id_counter = 2000
  
  def __init__(self, produto: str, categoria: str, preco: float) -> None:
    """
    Inicializa um produto base.

    Args:
      produto (str): O nome do produto.
      categoria (str): A categoria do produto.
      preco (float): O preço do produto.
    """
    self._id_produto: int = ProdutoBase._id_counter
    self._produto: str = produto 
    self._categoria: str = categoria
    self._preco: float = preco

    ProdutoBase._id_counter += 1

  @abstractmethod
  def __str__(self) -> str:
    pass

  @abstractmethod
  def __eq__(self, objeto: object) -> bool:
    pass

  @property
  def id(self) -> int:
    """
    Retorna o ID do produto.

    Returns:
      int: O ID do produto.
    """
    return self._id_produto
  
  @property
  def produto(self) -> str:
    """
    Retorna o nome do produto.

    Returns:
      str: O nome do produto.
    """
    return self._produto

  @produto.setter
  def produto(self, novo_produto: str) -> None:
    """
    Define um novo nome para o produto.

    Args:
      novo_produto (str): O novo nome do produto.
    """
    self._produto = novo_produto

  @property
  def categoria(self) -> str:
    """
    Retorna a categoria do produto.

    Returns:
      str: A categoria do produto.
    """
    return self._categoria

  @categoria.setter
  def categoria(self, nova_categoria: str) -> None:
    """
    Define uma nova categoria para o produto.

    Args:
      nova_categoria (str): A nova categoria do produto.
    """
    self._categoria = nova_categoria

  @property
  def preco(self) -> float:
    """
    Retorna o preço do produto.

    Returns:
      float: O preço do produto.
    """
    return self._preco

  @preco.setter
  def preco(self, novo_preco: float) -> None:
    """
    Define um novo preço para o produto.

    Args:
      novo_preco (float): O novo preço do produto.
    
    Raises:
      ValueError: Se o novo preço for negativo.
    """
    if novo_preco >= 0:
      self._preco = novo_preco
    else:
      raise ValueError("O preço deve ser um número positivo.")


class ProdutoPessoal(ProdutoBase):
  """
  Classe que representa um produto pessoal.

  Atributos:
    pertence (list): Uma lista de usuários aos quais o produto pertence.

  Métodos:
    __str__() -> str: Representação do objeto como uma string.
    __eq__(objeto: object) -> bool: Verifica se dois objetos são iguais.
    adicionar_usuario(novo_usuario) -> None: Adiciona um novo usuário ao produto.
    remover_usuario(usuario) -> None: Remove um usuário do produto.
  """
  def __init__(self, produto: str, categoria: str, preco: float, usuario) -> None:
    """
    Inicializa um produto pessoal.

    Args:
      produto (str): O nome do produto.
      categoria (str): A categoria do produto.
      preco (float): O preço do produto.
      usuario: O usuário associado ao produto.
    """
    super().__init__(produto, categoria, preco)
    self._pertence = [usuario]

  def __str__(self) -> str:
    """
    Retorna a representação do produto pessoal como uma string.

    Returns:
      str: A representação do produto pessoal.
    """
    return f"Produto Pessoal: {self.produto}, Categoria: {self.categoria}, Preço: {self.preco}"

  def __eq__(self, objeto: object) -> bool:
    """
    Verifica se dois objetos são iguais.

    Args:
      objeto (object): O objeto a ser comparado.

    Returns:
      bool: True se os objetos forem iguais, False caso contrário.
    """
    return isinstance(objeto, ProdutoPessoal) and super().__eq__(objeto)

  @property
  def pertence(self) -> list:
    """
    Retorna a lista de usuários aos quais o produto pertence.

    Returns:
      list: A lista de usuários.
    """
    return self._pertence

  def adicionar_usuario(self, novo_usuario) -> None:
    """
    Adiciona um novo usuário ao produto.

    Args:
      novo_usuario: O novo usuário a ser adicionado ao produto.
    """
    if novo_usuario not in self._pertence:
      self._pertence.append(novo_usuario)

  def remover_usuario(self, usuario) -> None:
    """
    Remove um usuário do produto.

    Args:
      usuario: O usuário a ser removido do produto.
    
    Raises:
      ValueError: Se o usuário não estiver associado ao produto.
    """
    if usuario in self._pertence:
      self._pertence.remove(usuario)
    else:
      raise ValueError(f"{usuario.nome} não é um usuário deste produto pessoal.")


class ProdutoGeral(ProdutoBase):
  """
  Classe que representa um produto geral.

  Métodos:
    __str__() -> str: Representação do objeto como uma string.
    __eq__(objeto: object) -> bool: Verifica se dois objetos são iguais.
  """
  def __str__(self) -> str:
    """
    Retorna a representação do produto geral como uma string.

    Returns:
      str: A representação do produto geral.
    """
    return f"Produto Geral: {self.produto}, Categoria: {self.categoria}, Preço: {self.preco}"

  def __eq__(self, objeto: object) -> bool:
    """
    Verifica se dois objetos são iguais.

    Args:
      objeto (object): O objeto a ser comparado.

    Returns:
      bool: True se os objetos forem iguais, False caso contrário.
    """
    return isinstance(objeto, ProdutoGeral) and super().__eq__(objeto)
