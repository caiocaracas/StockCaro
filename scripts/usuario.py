from typing import Dict
from scripts.interfaces import UsuarioInterface
from scripts.Repository import UserRepository
from scripts.lista import Lista
from scripts.dispensa import Dispensa
from scripts.residencia import Residencia

class Usuario(UsuarioInterface):
  def __init__(self, nome: str, email: str, senha: str, id_usuario: int, id_residencia: int, db: UserRepository) -> None:
    self.__nome = nome
    self.__senha = senha
    self.__email = email
    self.__id = id_usuario
    self.__lista = id_usuario  # Relação do banco de dados é de 1 pra 1
    self.__residencia = id_residencia
    self.__db = db

  @property
  def id(self) -> int:
    return self.__id
  
  @property
  def nome(self) -> str:
    return self.__nome

  @property
  def lista(self) -> int:
    return self.__lista
  
  @property
  def email(self) -> str:
    return self.__email

  @email.setter
  def email(self, novo_email: str) -> None:
    email = novo_email.split('@')
    if len(email) == 2:
      if len(email[1].split('.')) in (2, 3):
        self.__db.alterar_email(self.id, novo_email)
        self.__email = novo_email

  @property
  def senha(self) -> str:
    return self.__senha

  @senha.setter
  def senha(self, nova_senha: str) -> None:
    self.__senha = nova_senha

  @property
  def residencia(self) -> int:
    return self.__residencia
  
  @residencia.setter
  def residencia(self, residencia_id: int) -> None:
    self.__residencia = residencia_id
  
  @classmethod
  def carregar_usuario(cls, atributos: dict, db: UserRepository) -> 'Usuario':
    nome = atributos['nome']
    email = atributos['email']
    senha = atributos['senha']
    id_usuario = atributos['id_usuario']
    id_residencia = atributos['residencia_id']
    return cls(nome, email, senha, id_usuario, id_residencia, db)

  @classmethod
  def salvar_usuario(cls,  db: UserRepository, nome: str, email: str, senha: str) -> None:
    try:
      db.registrar_usuario(nome, email, senha)
    except RuntimeError as erro:
      raise erro

  def autenticar(self, email: str, senha: str) -> bool:
    return email == self.email and senha == self.senha
  
  def alterar_senha(self, antiga_senha: str, nova_senha: str) -> None:
    if antiga_senha == self.senha:
      self.__db.alterar_senha(self.id, nova_senha)
      self.__senha = nova_senha

  def adicionar_produto_lista(self, novo_produto_id: int, quantidade: int) -> None:
    try:
      Lista.adicionar_produto(self.__db, self.lista, novo_produto_id, quantidade)
    except RuntimeError as erro:
      raise erro

  def remover_produto_lista(self, produto_id: int, quantidade: int) -> None:
    try:
      Lista.remover_produto(self.__db, self.lista, produto_id, quantidade)
    except RuntimeError as erro:
      raise erro

  def adicionar_produto_dispensa(self, produto_id: int, quantidade: int) -> None:
    try:
      Residencia.adicionar_produto_dispensa(self.__db, self.residencia, produto_id, quantidade)
    except RuntimeError as erro:
      raise erro

  def remover_produto_dispensa(self, produto_id: int, quantidade: int) -> None:
    try:
      Residencia.remover_produto_dispensa(self.__db, self.residencia, produto_id, quantidade)
    except RuntimeError as erro:
      raise erro

  def dividas(self) -> Dict[str, float]:
    pass

  def obter_listas(self) -> Dict[Dict[str, int], float]:
    pass

  def finalizar_compra(self) -> None:
    pass

  def quitar_dividas(self) -> None:
    pass


"""
  Implementação de Administrador
"""

class Administrador(Usuario):
  def __init__(self, nome: str, email: str, senha: str, residencia_id: int, db: UserRepository) -> None:
    super().__init__(nome, email, senha, residencia_id, db)

  def adicionar_produto_geral(self, produto_id: int, quantidade: int) -> None:
    try:
      Residencia.adicionar_produto_lista_geral(self.__db, self.residencia, produto_id, quantidade)
    except RuntimeError as erro:
      raise erro

  def remover_produto_geral(self, produto_id: int, quantidade: int) -> None:
    try:
      Residencia.remover_produto_lista_geral(self.__db, self.residencia, produto_id, quantidade)
    except RuntimeError as erro:
      raise erro

  def adicionar_morador(self, morador_id: int) -> None:
    try:
      Residencia.adicionar_morador(self.__db, self.residencia, morador_id)
    except RuntimeError as erro:
      raise erro

  def remover_morador(self, morador_id: int) -> None:
    try:
      Residencia.remover_morador(self.__db, self.residencia, morador_id)
    except RecursionError as erro:
      raise erro