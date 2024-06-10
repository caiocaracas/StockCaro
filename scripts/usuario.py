from typing import Dict
from scripts.interfaces import UsuarioInterface
from scripts.Repository import UserRepository
from scripts.lista import Lista
from scripts.produto import Produto
from scripts.residencia import Residencia

class Usuario(UsuarioInterface):
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
      validar_email = email.split("@")
      if len(validar_email) == 2:
        if len(validar_email[1].split('.')) in (2, 3):
          db.registrar_usuario(nome, email, senha)
      else:
        raise RuntimeError("Email de cadastro inválido")
    
    except RuntimeError as erro:
      raise erro
    
  @classmethod
  def excluir_usuario(cls, db: UserRepository, id_usuario: int) -> None:
    try:
      db.deletar_usuario(id_usuario)
    except RuntimeError:
      raise RuntimeError(f"Não foi possível exluir o usuário de id {id_usuario}")
  
  def __init__(self, nome: str, email: str, senha: str, id_usuario: int, id_residencia: int, db: UserRepository) -> None:
    self.__nome = nome
    self.__senha = senha
    self.__email = email
    self.__id = id_usuario
    self.__residencia = id_residencia
    self.__db = db

  @property
  def id(self) -> int:
    return self.__id
  
  @property
  def nome(self) -> str:
    return self.__nome
  
  @property
  def email(self) -> str:
    return self.__email

  @email.setter
  def email(self, novo_email: str) -> None:
    email = novo_email.split('@')
    if len(email) == 2:
      if len(email[1].split('.')) in (2, 3):
        self.database.alterar_email(self.id, novo_email)
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

  @property
  def database(self) -> UserRepository:
    return self.__db
  
  @property
  def lista(self) -> dict:
    try:
      lista_ids = Lista.obter_lista(self.database, self.id)
      lista = {}
      for key, value in lista_ids.items():
        produto_info = Produto.get_info(self.database, key)
        produto = f"{produto_info['nome']} -- {produto_info['categoria']}"
        lista[produto] = value

      del lista_ids
      return lista
    except RuntimeError as erro:
      raise erro

  def autenticar(self, email: str, senha: str) -> bool:
    return email == self.email and senha == self.senha
  
  def alterar_senha(self, antiga_senha: str, nova_senha: str) -> bool:
    if antiga_senha == self.senha:
      self.database.alterar_senha(self.id, nova_senha)
      self.__senha = nova_senha
      return True
    return False

  def adicionar_produto_lista(self, novo_produto_id: int, quantidade: int) -> None:
    try:
      Lista.adicionar_produto(self.database, self.id, novo_produto_id, quantidade)
    except RuntimeError as erro:
      raise erro

  def remover_produto_lista(self, produto_id: int, quantidade: int) -> None:
    try:
      Lista.remover_produto(self.database, self.id, produto_id, quantidade)
    except RuntimeError as erro:
      raise erro

  def adicionar_produto_dispensa(self, produto_id: int, quantidade: int) -> None:
    try:
      Residencia.adicionar_produto_dispensa(self.database, produto_id, quantidade)
    except RuntimeError as erro:
      raise erro

  def remover_produto_dispensa(self, produto_id: int, quantidade: int) -> None:
    try:
      Residencia.remover_produto_dispensa(self.database, self.residencia, produto_id, quantidade)
    except RuntimeError as erro:
      raise erro

  def obter_listas_compra(self) -> Dict[str, int]:
    try:
      return Residencia.lista_compras(self.database, self.residencia)
    except RuntimeError as erro:
      raise erro

  def finalizar_compra(self, detalhes_compra: dict) -> None:
    try:
      print(detalhes_compra)
    except RuntimeError as erro:
      raise erro

  def dividas(self) -> Dict[int, float]:
    try:
      transferencias = self.database.buscar_transferencia(self.id)
  
      divida = {}
      for transf in transferencias.values():
        if transf['confirmado'] == 1:
          
          if transf['beneficiado_id'] == self.id:
          
            if transf['pagador_id'] not in divida:
              divida[transf['pagador_id']] = -transf['valor']
            else:
              divida[transf['pagador_id']] -= transf['valor']
        
          elif transf['pagador_id'] == self.id:
          
            if transf['beneficiado_id'] not in divida:
              divida[transf['beneficiado_id']] = transf['valor']
            else:
              divida[transf['beneficiado_id']] += transf['valor']
      
      return divida
  
    except RuntimeError as erro:
      raise erro
  
  def quitar_dividas(self, usuario_referente_divida: int) -> None:
    try:
      id_divida = self.database.buscar_transferencia_pendente(self.id, usuario_referente_divida)
      self.database.confirmar_transferencia(id_divida)
    except RuntimeError as erro:
      raise erro

  def emitir_pedido_quitar_divida(self, usuario_referente_divida: int) -> None:
    try:
      dividas = self.dividas()
      if usuario_referente_divida in dividas:
        if dividas[usuario_referente_divida] < 0:
          self.database.registrar_transferencia(usuario_referente_divida, self.id,
                                               -dividas[usuario_referente_divida], False)
    
    except RuntimeError as erro:
      raise erro

"""
  Implementação de Administrador
"""

class Administrador(Usuario):
  @classmethod
  def carregar_admin(cls, atributos: dict, db: UserRepository) -> 'Administrador':
    nome = atributos['nome']
    email = atributos['email']
    senha = atributos['senha']
    id_usuario = atributos['id_usuario']
    id_residencia = atributos['residencia_id']
    
    return cls(nome, email, senha, id_usuario, id_residencia, db)
  
  def __init__(self, nome: str, email: str, senha: str, id_usuario: int, residencia_id: int, db: UserRepository) -> None:
    super().__init__(nome, email, senha, id_usuario, residencia_id, db)

  def adicionar_morador(self, morador_id: int) -> None:
    try:
      Residencia.adicionar_morador(self.database, self.residencia, morador_id)
    except RuntimeError as erro:
      raise erro

  def remover_morador(self, morador_id: int) -> None:
    try:
      Residencia.remover_morador(self.database, morador_id)
    except RuntimeError as erro:
      raise erro