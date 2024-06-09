from scripts.interfaces import Dict
from scripts.interfaces import ResidenciaInterface
from scripts.dispensa import Dispensa
from scripts.lista import Lista
from scripts.produto import Produto
from scripts.Repository import UserRepository

class Residencia(ResidenciaInterface):
  @classmethod
  def criar_residencia(cls, db: UserRepository, id_admin: int) -> None:
    try:
      db.registrar_residencia(id_admin)
      id_residencia = db.buscar_residencia_por_admin(id_admin)
      cls.adicionar_morador(db, id_residencia, id_admin)
    except RuntimeError:
      raise RuntimeError("Não foi possível criar a residência")


  @classmethod
  def excluir_residencia(cls, db: UserRepository, id_residencia: int) -> None:
    try:
      db.deletar_residencia(id_residencia)  
    except RuntimeError:
      raise RuntimeError(f"Não foi possível deletar a residência de id {id_residencia}")


  @classmethod
  def info_residencia(cls, db: UserRepository, id_residencia: int) -> dict:
    try:
      return {
        'id_residencia': db.mostrar_residencia(id_residencia)['id_residencia'],
        'id_administrador': db.mostrar_residencia(id_residencia)['usuario_adm_id'],
        'moradores': list(db.mostrar_moradores(id_residencia).keys())
      }
    except RuntimeError:
      raise RuntimeError("Não foi possível obter informações da residência")

  @classmethod
  def adicionar_morador(cls, db: UserRepository, id_residencia: int, novo_morador_id: int) -> None:
    try:
      db.adicionar_morador(id_residencia, novo_morador_id)
    except RuntimeError:
      raise RuntimeError(f"Não foi possível adicionar morador {novo_morador_id} em residência {id}")


  @classmethod
  def remover_morador(cls, db: UserRepository, morador_id: int) -> None:
    try:
      db.remover_morador(morador_id)
    except RuntimeError:
      raise RuntimeError(f"Não foi possível remover morador {morador_id} da residência")


  @classmethod
  def adicionar_produto_dispensa(cls, db: UserRepository, produto_id: int, quantidade: int) -> None:
    try:
      Dispensa.adicionar_produto(db, produto_id, quantidade)
    except RuntimeError:
      raise RuntimeError("Não foi possível adicionar produto na dispensa")


  @classmethod
  def remover_produto_dispensa(cls, db: UserRepository, id_residencia: int, produto_id: int, quantidade: int) -> None:
    try:
      Dispensa.remover_produto(db, id_residencia, produto_id, quantidade)
    except RuntimeError:
      raise RuntimeError("Não foi possível remover produto da dispensa")


  @classmethod
  def lista_compras(cls, db: UserRepository, id_residencia: int) -> Dict[str, int]:
    try:
      moradores = cls.info_residencia(db, id_residencia)['moradores']
    except RuntimeError:
      raise RuntimeError("Não foi possível obter informações sobre a residência")

    lista_compras_id = {}
    try:
      for morador in moradores:
        lista = Lista.obter_lista(db, morador)
        for key, value in lista.items():
          if key in lista_compras_id:
            lista_compras_id[key] += value
          else:
            lista_compras_id[key] = value
      
      estoque = Dispensa.estoque(db, id_residencia)
      lista_compras = {}
      for key, value in lista_compras_id.items():
        produto_info = Produto.get_info(db, key)
        produto = f"{produto_info['nome']} - {produto_info['quantidade_unidade']}"
        if key in estoque:
          lista_compras[produto] = value - estoque[key]
        else:
          lista_compras[produto] = value

      del estoque
      del lista_compras_id

      return lista_compras
    except RuntimeError:
      raise RuntimeError("Não foi possível obter a lista de compras")