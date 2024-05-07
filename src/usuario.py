from abc import ABC, abstractmethod
import re
from hashlib import sha256
from lista import ListaPessoal

class Usuario(ABC):
  """
  Classe abstrata que representa um usuário.

  Atributos:
    _id_counter (int): Um contador estático para gerar IDs únicos para os usuários.

  Métodos abstratos:
    __str__() -> str: Representação do objeto como uma string.
    __eq__(obj: object) -> bool: Verifica se dois objetos são iguais.

  Propriedades:
    id (int): O ID do usuário.
    nome (str): O nome do usuário.
    email (str): O e-mail do usuário.
    senha (str): A senha do usuário.
  """
  _id_counter = 1000

  def __init__(self, nome: str, email: str, senha: str) -> None:
    """
    Inicializa um usuário.

    Args:
      nome (str): O nome do usuário.
      email (str): O e-mail do usuário.
      senha (str): A senha do usuário.
    """
    super().__init__()
    self._id: int = Usuario._id_counter
    Usuario._id_counter += 1

    self._nome: str = nome
    
    self._email: str = None
    self._senha: str = None
    
    self.email = email
    self.senha = senha
  
  @abstractmethod
  def __str__(self) -> str:
    pass
  
  @abstractmethod
  def __eq__(self, obj: object) -> bool:
    pass

  @staticmethod
  def _hash_senha(senha: str) -> str:
    """
    Gera um hash SHA-256 para a senha.

    Args:
      senha (str): A senha a ser criptografada.

    Returns:
      str: O hash SHA-256 da senha.
    """
    return sha256(senha.encode()).hexdigest()

  @property
  def id(self) -> int:
    """
    Retorna o ID do usuário.

    Returns:
      int: O ID do usuário.
    """
    return self._id

  @property
  def nome(self) -> str:
    """
    Retorna o nome do usuário.

    Returns:
      str: O nome do usuário.
    """
    return self._nome

  @nome.setter
  def nome(self, novo_nome: str) -> None:
    """
    Define um novo nome para o usuário.

    Args:
      novo_nome (str): O novo nome do usuário.
    """
    self._nome = novo_nome

  @property
  def email(self) -> str:
    """
    Retorna o e-mail do usuário.

    Returns:
      str: O e-mail do usuário.
    """
    return self._email

  @email.setter
  def email(self, novo_email: str) -> None:
    """
    Define um novo e-mail para o usuário.

    Args:
      novo_email (str): O novo e-mail do usuário.

    Raises:
      ValueError: Se o e-mail fornecido não for válido.
    """
    if re.match(r"[^@]+@[^@]+\.[^@]+", novo_email):
      self._email = novo_email
    else:
      raise ValueError("Email inválido.")

  @property
  def senha(self) -> str:
    """
    Retorna a senha do usuário (não criptografada).

    Returns:
      str: A senha do usuário.
    """
    return self._senha

  @senha.setter
  def senha(self, nova_senha: str) -> None:
    """
    Define uma nova senha para o usuário.

    Args:
      nova_senha (str): A nova senha do usuário.
    """
    self._senha = self._hash_senha(nova_senha)
  
  def alterar_senha(self, antiga_senha: str, nova_senha: str) -> None:
    """
    Altera a senha do usuário.

    Args:
      antiga_senha (str): A senha atual do usuário.
      nova_senha (str): A nova senha do usuário.

    Note:
      A senha atual deve ser fornecida para alterar a senha.

    Raises:
      ValueError: Se a senha atual fornecida estiver incorreta.
    """
    if self.senha == self._hash_senha(antiga_senha):
      self._senha = nova_senha
  
  def autenticar(self, email: str, senha: str) -> bool:
    """
    Autentica o usuário.

    Args:
      email (str): O e-mail do usuário.
      senha (str): A senha do usuário.

    Returns:
      bool: True se a autenticação for bem-sucedida, False caso contrário.
    """
    return self.email == email and self.senha == self._hash_senha(senha)


class Morador(Usuario):
  """
  Classe que representa um morador.

  Atributos:
    _listaCompras (ListaPessoal): A lista de compras pessoal do morador.

  Métodos:
    __str__() -> str: Representação do objeto como uma string.
    __eq__(obj: object) -> bool: Verifica se dois objetos são iguais.
  """
  def __init__(self, nome: str, email: str, senha: str) -> None:
    """
    Inicializa um morador.

    Args:
      nome (str): O nome do morador.
      email (str): O e-mail do morador.
      senha (str): A senha do morador.
    """
    super().__init__(nome, email, senha)
    self._listaCompras = ListaPessoal(self)
  
  def __str__(self) -> str:
    """
    Retorna a representação do morador como uma string.

    Returns:
      str: A representação do morador.
    """
    return f"Morador: {self.nome}, Email: {self.email}"
  
  def __eq__(self, obj: object) -> bool:
    """
    Verifica se dois moradores são iguais.

    Args:
      obj (object): O objeto a ser comparado.

    Returns:
      bool: True se os moradores forem iguais, False caso contrário.
    """
    return isinstance(obj, Morador) and super().__eq__(obj)


class Administrador(Usuario):
  """
  Classe que representa um administrador.

  Atributos:
    _residencia: A residência associada ao administrador.
    _listaCompras (ListaPessoal): A lista de compras pessoal do administrador.

  Métodos:
    __str__() -> str: Representação do objeto como uma string.
    __eq__(obj: object) -> bool: Verifica se dois objetos são iguais.
  """
  def __init__(self, nome: str, email: str, senha: str, residencia = None) -> None:
    """
    Inicializa um administrador.

    Args:
      nome (str): O nome do administrador.
      email (str): O e-mail do administrador.
      senha (str): A senha do administrador.
      residencia: A residência associada ao administrador (opcional).
    """
    super().__init__(nome, email, senha)
    self._residencia = residencia
    self._listaCompras = ListaPessoal()

  def __str__(self) -> str:
    """
    Retorna a representação do administrador como uma string.

    Returns:
      str: A representação do administrador.
    """
    return f"Administrador: {self.nome}, Email: {self.email}"
  
  def __eq__(self, obj: object) -> bool:
    """
    Verifica se dois administradores são iguais.

    Args:
      obj (object): O objeto a ser comparado.

    Returns:
      bool: True se os administradores forem iguais, False caso contrário.
    """
    return isinstance(obj, Administrador) and super().__eq__(obj)
  
  @property
  def residencia(self):
    """
    Retorna a residência associada ao administrador.

    Returns:
      A residência associada ao administrador.
    """
    return self._residencia
  
  @residencia.setter
  def residencia(self, nova_residencia) -> None:
    """
    Define uma nova residência para o administrador.

    Args:
      nova_residencia: A nova residência associada ao administrador.
    """
    self._residencia = nova_residencia
