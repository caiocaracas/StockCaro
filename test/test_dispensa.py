from src.dispensa import Dispensa
from src.produto import ProdutoGeral, ProdutoPessoal
from src.usuario import Morador

import unittest

class TestDispensa(unittest.TestCase):
  def setUp(self) -> None:
    self.dispensa = Dispensa()
    self.morador = Morador("Arthur", "arthur@email.com", "1234")
        
    self.produto1 = ProdutoGeral("Arroz", "Alimento", 25.99)
    self.produto2 = ProdutoGeral("Feijão", "Alimento", 9.99)
    self.produto3 = ProdutoPessoal("Desodorante", "Higiene", 8.99, self.morador)

    self.dispensa.adicionar_produto(self.produto1, 5)
    self.dispensa.adicionar_produto(self.produto2, 10)
    self.dispensa.adicionar_produto(self.produto3, 5)
    
  def tearDown(self) -> None:
    del self.dispensa
    
  def test_adicionar_produto(self) -> None:
    # Verifica se a adição de um produto aumenta o estoque corretamente
    self.dispensa.adicionar_produto(self.produto1, 5)
    self.assertEqual(self.dispensa.estoque[self.produto1.id], 10)
        
    # Verifica se a adição de outro produto não afeta outros estoques
    self.assertEqual(self.dispensa.estoque[self.produto2.id], 10)
    self.assertEqual(self.dispensa.estoque[self.produto3.id], 5)
    
  def test_remover_produto(self) -> None:
    # Verifica se a remoção de um produto reduz o estoque corretamente
    self.dispensa.remover_produto(self.produto2, 1)
    self.assertEqual(self.dispensa.estoque[self.produto2.id], 9)
        
    # Verifica se a remoção de todo o estoque de um produto o remove da dispensa
    self.dispensa.remover_produto(self.produto1, 5)
    self.assertNotIn(self.produto1.id, self.dispensa.estoque)
        
    # Verifica se tentar remover um produto que não está na dispensa gera um erro
    with self.assertRaises(ValueError):
      self.dispensa.remover_produto(self.produto1, 1)
    
  def test_adicionar_produto_invalido(self) -> None:
    # Verifica se tentar adicionar um produto inválido gera um erro
    with self.assertRaises(TypeError):
      self.dispensa.adicionar_produto("Produto Inválido", 5)
    
  def test_remover_quantidade_maior_que_estoque(self) -> None:
    # Verifica se tentar remover uma quantidade maior que o estoque gera um erro
    with self.assertRaises(ValueError):
      self.dispensa.remover_produto(self.produto1, 10)
    
  def test_remover_produto_inexistente(self) -> None:
    # Verifica se tentar remover um produto que não está na dispensa gera um erro
    with self.assertRaises(ValueError):
      self.dispensa.remover_produto(ProdutoGeral("Produto Inexistente", "Alimento", 1.99), 1)


if __name__ == "__main__":
  unittest.main()