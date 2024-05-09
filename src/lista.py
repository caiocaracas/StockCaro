from typing import Dict, Type
from interfaces import *
from src.interfaces import Dispensa, Produto

class ListaPessoal(Lista):
  def __init__(self, usuario: Type["Usuario"]) -> None:
    self._lista: Dict[int, int] = {}
    self._produtos = []
    self._usuario = usuario

  def adicionar_produto(self, novo_produto: Type["Produto"], quantidade: int) -> None:
    if quantidade < 0:
      raise ValueError("Quantidade precisa ser positiva")
    
    self._produtos.append(novo_produto)
    self._lista[novo_produto.id] = quantidade

  def remover_produto(self, produto: Type["Produto"], quantidade: int = 0) -> None:
    if quantidade < 0:
      raise ValueError("Quantidade precisa ser positiva")
    
    if produto in self._produtos:
      match quantidade:
        case q if q == 0:
          del self._lista[produto.id]
          del self._produtos[produto]

        case q if q > self._lista[produto.id]:
          self._lista[produto.id] -= quantidade
        
        case q if q == self._lista[produto.id]:
          del self._lista[produto.id]
          del self._produtos[produto]
        
        case q if q < self._lista[produto.id]:
          raise ValueError("Quantidade a ser removida Indisponível")
        
        case _:
          raise ValueError("Valor inserido em Quantidade Inválido")
    else:
      raise ValueError("Produto não encontrado")


  def obter_lista(self, dispensa: Type["Dispensa"]) -> Dict[int, int]:
    lista = self._lista.copy()

    for key, value in dispensa.estoque.items():  # Usar .items() para iterar sobre o dicionário
      if key in lista:
        lista[key] -= value
      if lista[key] <= 0:
        del lista[key]

    return lista

  def valor_compra(self) -> float:
    valor = 0

    lista = self.obter_lista(self._usuario.dispensa)  # Passar a dispensa do usuário para obter_lista()

    for key, value in lista.items():  # Iterar sobre os itens do dicionário retornado por obter_lista()
      if key in [produto.id for produto in self._produtos]:
        index = [produto.id for produto in self._produtos].index(key)
        valor += value * self._produtos[index].preco

    return valor
