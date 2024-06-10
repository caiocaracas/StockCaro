import mysql.connector
from abc import ABC
import datetime

'''
* Sucetivel a erros por alteração na estrutura no banco de dados: exclusão da tabela produtos_dispensa e adição de uma coluna quantidade existente em produtos
* da residencia
* Garantir que a chave primaria id_produto e consumidor seja respeitada
* Decidir a identificação dos produtos_residencia e listado pessoal e geral, junto com quem consome 
'''

# Classe base para conexão com o banco de dados
class Database:
    def __init__(self, host, user, password, database):
        """
        Inicializa a conexão com o banco de dados.
        
        Parâmetros:
        - host: endereço do servidor do banco de dados
        - user: nome de usuário para a conexão
        - password: senha para a conexão
        - database: nome do banco de dados a ser utilizado
        """
        try:
            # Tenta estabelecer a conexão com o banco de dados
            self.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            # Cria um cursor para executar comandos SQL]
            self.cursor = self.connection.cursor()
        except mysql.connector.Error as err:
            # Levanta um erro se a conexão falhar
            raise RuntimeError(f"Erro ao conectar ao banco de dados: {str(err)}")
            
    def close(self):
        """
        Fecha a conexão com o banco de dados e o cursor.
        """
        self.cursor.close()  # Fecha o cursor
        self.connection.close()  # Fecha a conexão

# Classe base para repositórios, utilizando a funcionalidade de classe abstrata
class BaseRepository(ABC):
    def __init__(self, database: Database) -> None:
        """
        Inicializa o repositório base com uma instância de conexão ao banco de dados.
        
        Parâmetros:
        - database: instância da classe Database que gerencia a conexão com o banco de dados
        """
        self.database = database


class UserRepository(BaseRepository):
    def __init__(self, database):
        super().__init__(database)
    
    def __verificar_se_usuario_existe(self, id_usuario: int) -> bool:
        query = "SELECT 1 FROM usuarios WHERE id_usuario = %s;"
        try:
            cursor = self.database.cursor
            cursor.execute(query, (id_usuario,))
            result = cursor.fetchone()
            return bool(result)
        except mysql.connector.Error as err:
            raise RuntimeError(f"Erro ao verificar se o usuário de email {id_usuario} existe no banco: {str(err)}")
            
    def __verificar_se_produto_residencia_existe(self, id_produto_residencia: int) -> bool:
        query = "SELECT 1 FROM produtos_residencia WHERE id_produto_residencia = %s;"
        try:
            cursor = self.database.cursor
            cursor.execute(query, (id_produto_residencia,))
            result = cursor.fetchone()
            return bool(result)
        except mysql.connector.Error as err:
            raise RuntimeError(f"Erro ao verificar se o produto que a residencia de ID {id_produto_residencia} existe no banco: {str(err)}")
            
    def __verificar_se_residencia_existe(self, id_residencia: int) -> bool:
        query = "SELECT 1 FROM residencias WHERE id_residencia = %s;"
        try:
            cursor = self.database.cursor
            cursor.execute(query, (id_residencia,))
            result = cursor.fetchone()
            return bool(result)
        except mysql.connector.Error as err:
            raise RuntimeError(f"Erro ao verificar se a residencia de ID {id_residencia} existe no banco: {str(err)}")
    
    def __verificar_se_compra_existe(self, id_compra: int) -> bool:
        query = "SELECT 1 FROM compras WHERE id_compra = %s;"
        try:
            cursor = self.database.cursor
            cursor.execute(query, (id_compra,))
            result = cursor.fetchone()
            return bool(result)
        except mysql.connector.Error as err:
            raise RuntimeError(f"Erro ao verificar se a compra de ID {id_compra} existe no banco: {str(err)}")
    
    def __verificar_se_transferencia_existe(self, id_transferencia: int) -> bool:
        query = "SELECT 1 FROM transferencias WHERE id_transferencia = %s;"
        try:
            cursor = self.database.cursor
            cursor.execute(query, (id_transferencia,))
            result = cursor.fetchone()
            return bool(result)
        except mysql.connector.Error as err:
            raise RuntimeError(f"Erro ao verificar se transferencia de ID {id_transferencia} existe no banco: {str(err)}")
  
    def __verificar_se_usuario_tem_residencia(self, id_usuario:int) -> bool:
        query = "SELECT 1 FROM usuarios WHERE (id_usuario = %s AND residencia_id IS NOT NULL);"
        try:
            cursor = self.database.cursor
            cursor.execute(query, (id_usuario,))
            result = cursor.fetchone()
            return bool(result)
        except mysql.connector.Error as err:
            raise RuntimeError(f"Erro ao verificar se usuario de ID {id_usuario} tem residencia: {str(err)}")
        
    def __verificar_se_produto_listado_pessoal_existe(self, id_produto_listado: int) -> bool:
        query = "SELECT 1 FROM produtos_listados_pessoais WHERE id_produto_listado_pessoal = %s;"
        try:
            cursor = self.database.cursor
            cursor.execute(query, (id_produto_listado,))
            result = cursor.fetchone()
            return bool(result)
        except mysql.connector.Error as err:
            raise RuntimeError(f"Erro ao verificar se produto listado de ID {id_produto_listado} existe no banco: {str(err)}")
    
    def __verificar_se_produto_dispensa_existe(self, produto_residencia_id: int) -> bool:
        query = "SELECT 1 FROM produtos_residencia WHERE id_produto_residencia = %s and quantidade_existente != '0';"
        try:
            cursor = self.database.cursor
            cursor.execute(query, (produto_residencia_id,))
            result = cursor.fetchone()
            return bool(result)
        except mysql.connector.Error as err:
            raise RuntimeError(f"Erro ao verificar se produto na dispensa de ID {produto_residencia_id} existe no banco: {str(err)}")

    def login(self, email: str) -> dict:
            query = "SELECT * FROM usuarios WHERE email = %s;"
            try:
                cursor = self.database.cursor
                cursor.execute(query, (email,))
                result = cursor.fetchone()
                if result:
                    columns = [desc[0] for desc in cursor.description]  
                    return dict(zip(columns, result))  
                else:
                    return {}
            except mysql.connector.Error as err:
                self.database.rollback()
                raise RuntimeError(f"Erro ao buscar usuário: {str(err)}")

    def registrar_usuario(self, nome: str, email: str, senha: str) -> None:
        if not self.__verificar_se_usuario_existe(email):
            try:
                query = "INSERT INTO usuarios (nome, email, senha, residencia_id) VALUES (%s, %s, %s, null)"
                values = (nome, email, senha)
                cursor = self.database.cursor
                cursor.execute(query, values)
                self.database.connection.commit()
            except mysql.connector.Error as err:
                self.database.connection.rollback()
                raise RuntimeError(f"Erro ao registrar um usuário: {str(err)}")
        else:
            raise RuntimeError("ERRO: o email já existe")
           
    # Pre-condição - o usuário referente ao método tem que existir
    def deletar_usuario(self, id_usuario: int):
        if self.__verificar_se_usuario_existe(id_usuario):
            query = "DELETE FROM usuarios WHERE id_usuario = %s;"
            try:
                cursor = self.database.cursor
                cursor.execute(query, (id_usuario,))
                self.database.connection.commit()
            except mysql.connector.Error as err:
                raise RuntimeError(f"Erro ao deletar o usuário de ID { id_usuario }: {str(err)}")
        else:
            raise RuntimeError(f"ERRO: o usuário de ID {id_usuario} não existe")
       
    # Pre_condição - usuario referente ao metodo tem que existir
    def alterar_senha(self, id_usuario:int, nova_senha:str):
        if self.__verificar_se_usuario_existe(id_usuario):
            query = "UPDATE usuarios SET senha = %s WHERE id_usuario = %s;"
            try:
                cursor = self.database.cursor
                cursor.execute(query, (nova_senha, id_usuario))
                self.database.connection.commit()
            except mysql.connector.Error as err:
                raise RuntimeError(f"Erro ao alterar a senha do usuário de ID {id_usuario}: {str(err)}")
        else:
            raise RuntimeError(f"ERRO: o usuário de ID {id_usuario} não existe")
    
    # Pre_condição - usuario referente ao metodo tem que existir
    def alterar_email(self, id_usuario:int, novo_email:str):
        if self.__verificar_se_usuario_existe(id_usuario):
            query = "UPDATE usuarios SET email = %s WHERE id_usuario = %s;"
            try:
                cursor = self.database.cursor
                cursor.execute(query, (novo_email, id_usuario))
                self.database.connection.commit()
            except mysql.connector.Error as err:
                raise RuntimeError(f"Erro ao alterar o e-mail do usuário de ID {id_usuario}: {str(err)}")
        else:
            raise RuntimeError(f"ERRO: o usuário de ID {id_usuario} não existe")
    
    #
    def registrar_residencia(self, id_adm:int) -> int:
       query = "INSERT INTO residencias (usuario_adm_id) VALUES (%s)"
       try:
           self.database.cursor.execute(query, (id_adm,))
           self.database.connection.commit()
       except mysql.connector.Error as err:
           raise RuntimeError(f"Erro ao criar uma residencia: {str(err)}")
  
    # Pre_condição - residencia referente ao metodo tem que existir 
    def deletar_residencia(self, id_residencia:int) -> bool:
        if self.__verificar_se_residencia_existe(id_residencia):
            query = "DELETE FROM residencias WHERE id_residencia = %s;"
            try:
                self.database.cursor.execute(query, (id_residencia,))
                self.database.connection.commit()
            except mysql.connector.Error as err:
                raise RuntimeError(f"Erro ao deletar residencia de ID {id_residencia}: {str(err)}")
        else:
            raise RuntimeError(f"ERRO: a residencia de ID {id_residencia} não existe")
    
    # Pre_condição - residencia referente ao metodo tem que existir
    def alterar_adm_de_uma_residencia(self, id_residencia:int, id_novo_adm:int):
        if self.__verificar_se_residencia_existe(id_residencia):
           query = "UPDATE residencias SET usuario_adm_id = %s WHERE id_residencia = %s;"
           try:
               cursor = self.database.cursor
               cursor.execute(query, (id_novo_adm, id_residencia))
               self.database.connection.commit()
           except mysql.connector.Error as err:
               raise RuntimeError(f"Erro ao alterar o administrador da residência de ID {id_residencia}: {str(err)}")
        else:
           raise RuntimeError(f"ERRO: a residência de ID {id_residencia} não existe")

    # Pre_condição - residencia e usuario referente ao metodo tem que existir   
    def adicionar_morador(self, id_residencia:int, id_usuario:int):
        if self.__verificar_se_residencia_existe(id_residencia) and self.__verificar_se_usuario_existe(id_usuario):
            query = "UPDATE usuarios SET residencia_id = %s WHERE id_usuario = %s;"
            try:
                cursor = self.database.cursor
                cursor.execute(query, (id_residencia, id_usuario))
                self.database.connection.commit()
            except mysql.connector.Error as err:
                raise RuntimeError(f"Erro ao adicionar o usuário de ID {id_usuario} à residência de ID {id_residencia}: {str(err)}")
        else:
            raise RuntimeError(f"ERRO: a residência de ID {id_residencia} ou o usuário de ID {id_usuario} não existem")
    
    # Pre_condição - usuario referente ao metodo tem que existir
    def remover_morador(self, id_usuario) -> None:
        if self.__verificar_se_usuario_existe(id_usuario):
            query = "UPDATE usuarios SET residencia_id = null WHERE id_usuario = %s;"
            try:
                cursor = self.database.cursor
                cursor.execute(query, (id_usuario,))
                self.database.connection.commit()
            except mysql.connector.Error as err:
                raise RuntimeError(f"Erro remover moradorde ID {id_usuario}: {str(err)}")
        else:
            raise RuntimeError(f"ERRO: ao remover morador, o usuário de ID {id_usuario} não existe")
    
    # Pre_condição - residencia referente ao metodo tem que existir 
    def mostrar_residencia(self, id_residencia:int) -> dict:
        if self.__verificar_se_residencia_existe(id_residencia):
            query = "SELECT * FROM residencias WHERE id_residencia = %s;"
            try:
                cursor = self.database.cursor
                cursor.execute(query, (id_residencia,))
                result = cursor.fetchone()
                if result:
                    if result:
                        columns = [desc[0] for desc in self.database.cursor.description]  # Obter os nomes das colunas
                        return dict(zip(columns, result))  # Combinar colunas e valores em um dicionário
                    else:
                        return {}
            except mysql.connector.Error as err:
                # Aqui você pode levantar uma exceção personalizada ou apenas logar o erro
                raise RuntimeError(f"Erro ao buscar residência: {str(err)}")
                return {}
        else:
            raise RuntimeError(f"ERRO: a residencia de ID {id_residencia} não existe")

    # Pre_condição - residencia referente ao metodo tem que existir
    def mostrar_moradores(self, id_residencia:int) -> dict:
        if self.__verificar_se_residencia_existe(id_residencia):
            query = "SELECT * FROM usuarios WHERE residencia_id = %s;"
            try:
               cursor = self.database.cursor
               cursor.execute(query, (id_residencia,))
               consulta = cursor.fetchall() # list[list[atributo]]
               if consulta:
                    columns = [desc[0] for desc in cursor.description] # Lista dos nomes das colunas da tabela
                    lista_dicionario = [dict(zip(columns, row)) for row in consulta] # lista das informaçoes dos produtos em forma de lista de dicionarios
                    lista_de_ids = [dic['id_usuario'] for dic in lista_dicionario]# Lista com o id de cada produto da consulta
                    result = dict(zip(lista_de_ids, lista_dicionario)) # dicionario com chaves sendo os ids e os valores sendo um dicionario que representa as informações do produto
                    return result #row = result[i] # Combina os valores dos id com os valores da linha
               else:
                   return {}
            except mysql.connector.Error as err:
               # Aqui você pode levantar uma exceção personalizada ou apenas logar o erro
               raise RuntimeError(f"Erro ao buscar moradores: {str(err)}")
               return {}
        else:
             raise RuntimeError(f"ERRO: a residencia de ID {id_residencia} não existe")

    def buscar_residencia_por_admin(self, id_admin: int) -> int:
        query = "SELECT * FROM residencias WHERE usuario_adm_id = %s"
        try:
            cursor = self.database.cursor
            cursor.execute(query, (id_admin,))
            consulta = cursor.fetchall()
            if consulta:
                return consulta[0][0]
            else:
                return None
        except mysql.connector.Error as erro:
            raise RuntimeError(f"Erro ao buscar residencia: {erro}")
        
    def buscar_usuario_por_id(self, id_user: int) -> dict:
        query = "SELECT nome, email, residencia_id FROM usuarios WHERE id_usuario = %s"
        try:
            cursor = self.database.cursor
            cursor.execute(query, (id_user,))
            consulta = cursor.fetchall()
            if consulta:
                colunas = [descricao[0] for descricao in cursor.description]
                lista_ids = [dict(zip(colunas, linha)) for linha in consulta]
                return lista_ids[0]
            else:
                return {}
        except mysql.connector.Error as erro:
            raise RuntimeError(f"Erro ao buscar usuario: {erro}")
    
    def registrar_produto_residencia(self, id_residencia: int, nome:str, quantidade:int, unid_medida:str, categoria):
        query = "INSERT INTO produtos_residencia (residencia_id, nome, quantidade_unid, unidade_de_medida, categoria) VALUES (%s, %s, %s, %s, %s )"
        try: 
            self.database.cursor.execute(query, (id_residencia, nome, quantidade, unid_medida, categoria)) 
            self.database.connection.commit()
        except mysql.connector.Error as err:
            raise RuntimeError(f"Erro ao registrar produto na residência de ID {id_residencia}: {str(err)}")
    
    # Pre_condição - produto da residencia referente ao metodo tem que existir
    def deletar_produto_residencia(self, id_produto_residencia:int) -> bool:
        if self.__verificar_se_produto_residencia_existe(id_produto_residencia):
            query = "DELETE FROM produtos_residencia WHERE id_produto_residencia = %s;"
            try:
                cursor = self.database.cursor
                cursor.execute(query, (id_produto_residencia,))
                self.database.connection.commit()
            except mysql.connector.Error as err:
                raise RuntimeError(f"Erro ao deletar o produto da residencia de ID {id_produto_residencia}: {str(err)}")
        else:
            raise RuntimeError(f"ERRO: o produto da residencia solicitado para deleção de ID {id_produto_residencia} não existe")
    
    # Pre_condição - residencia tem que existir
    def mostrar_produtos_cadastrados_da_residencia(self, id_residencia: int) -> dict:
        if self.__verificar_se_residencia_existe(id_residencia):
            query = "SELECT * FROM produtos_residencia WHERE residencia_id = %s;"
            try:
                cursor = self.database.cursor
                cursor.execute(query, (id_residencia,))
                consulta = cursor.fetchall() # list[list[atributo]]
                if consulta:
                    columns = [desc[0] for desc in cursor.description] # Lista dos nomes das colunas da tabela
                    lista_dicionario = [dict(zip(columns, row)) for row in consulta] # lista das informaçoes dos produtos em forma de lista de dicionarios
                    lista_de_ids = ([(dict['id_produto_residencia']) for dict in lista_dicionario])# Lista com o id de cada produto da consulta
                    result = dict(zip(lista_de_ids, lista_dicionario)) # dicionario com chaves sendo os ids e os valores sendo um dicionario que representa as informações do produto
                    return result #row = result[i] # Combina os valores dos id com os valores da linha
                else:
                    return {}
            except mysql.connector.Error as err:
                raise RuntimeError(f"Erro ao mostrar produtos cadastrados da residência: {str(err)}")
                return {}
        else:
            raise RuntimeError(f"ERRO: a residencia de ID {id_residencia} não existe no banco")
    
    # Pre_condição - produto residencia tem que existir
    def mostrar_produto_da_residencia(self, id_produto_residencia: int) -> dict:
        if self.__verificar_se_produto_residencia_existe(id_produto_residencia):
            query = "SELECT * FROM produtos_residencia WHERE id_produto_residencia = %s;"
            try:
                cursor = self.database.cursor
                cursor.execute(query, (id_produto_residencia,))
                result = cursor.fetchone()
                if result:
                    columns = [desc[0] for desc in cursor.description]  # Obter os nomes das colunas
                    return dict(zip(columns, result))  # Combinar colunas e valores em uma lista de dicionários
                else:
                    return {}
            except mysql.connector.Error as err:
                raise RuntimeError(f"Erro ao mostrar produto da residência: {str(err)}")
                return {}
        else:
            raise RuntimeError(f"ERRO: o produto residência de ID {id_produto_residencia} não existe no banco")
    
    def adicionar_produto_lista_pessoal(self, id_produto_residencia, usuario_id, quantidade):
        query = "INSERT INTO produtos_listados_pessoais (produto_residencia_id, usuario_id, quantidade_listada) VALUES (%s, %s, %s);"
        try:
            self.database.cursor.execute(query, (id_produto_residencia, usuario_id, quantidade))
            self.database.connection.commit()
        except mysql.connector.Error as err:
            raise RuntimeError(f"Erro ao registrar produto na lista pessoal de ID {usuario_id}: {str(err)}")
            
    # Pre_condição - produto listado referente ao metodo tem que existir
    def deletar_produto_lista_pessoal(self, usuario_id:int, produto_residencia_id:int):
        if self.__verificar_se_produto_residencia_existe(produto_residencia_id):
            query = "DELETE FROM produtos_listados_pessoais WHERE usuario_id = %s and produto_residencia_id = %s;"
            try:
                cursor = self.database.cursor
                cursor.execute(query, (usuario_id, produto_residencia_id))
                self.database.connection.commit()
            except mysql.connector.Error as err:
                raise RuntimeError(f"Erro ao deletar o produto listado de ID {produto_residencia_id}: {str(err)}")
        else:
            raise RuntimeError(f"ERRO: o produto listado de ID {produto_residencia_id} não existe")
    
    
    def aumentar_quantidade_produto_lista_pessoal(self, usuario_id:int, produto_residencia_id:int, quantidade_adicionada:int):
        if self.__verificar_se_produto_residencia_existe(produto_residencia_id):
            query = "UPDATE produtos_listados_pessoais SET quantidade_listada = quantidade_listada + %s WHERE produto_residencia_id = %s and usuario_id = %s;"
            try:
                cursor = self.database.cursor
                cursor.execute(query, (quantidade_adicionada, produto_residencia_id, usuario_id))
                self.database.connection.commit()
            except mysql.connector.Error as err:
                raise RuntimeError(f"Erro adicionar quantidade de um produto de ID {produto_residencia_id} na lista {str(err)}")
        else:
            raise RuntimeError(f"ERRO: ao aumentar a quantiade de um produto na lista, o produto de ID {produto_residencia_id} não existe")
    
    def diminuir_quantidade_produto_lista_pessoal(self, usuario_id:int, produto_residencia_id:int, quantidade_adicionada:int):
        if self.__verificar_se_produto_residencia_existe(produto_residencia_id):
            query = "UPDATE produtos_listados_pessoais SET quantidade_listada = quantidade_listada +- %s WHERE produto_residencia_id = %s and usuario_id = %s;"
            try:
                cursor = self.database.cursor
                cursor.execute(query, (quantidade_adicionada, produto_residencia_id, usuario_id))
                self.database.connection.commit()
            except mysql.connector.Error as err:
                raise RuntimeError(f"Erro adicionar diminuir de um produto de ID {produto_residencia_id} na lista {str(err)}")
        else:
            raise RuntimeError(f"ERRO: ao diminuir a quantiade de um produto na lista, o produto de ID {produto_residencia_id} não existe")
    
    # Pre_condição - usuario referente ao metodo tem que existir
    def mostrar_produtos_lista_pessoal(self, id_usuario: int) -> dict:
        if self.__verificar_se_usuario_existe(id_usuario):
            query = "SELECT * FROM produtos_listados_pessoais WHERE usuario_id = %s"
            try:
                cursor = self.database.cursor
                cursor.execute(query, (id_usuario,))
                consulta = cursor.fetchall() # list[list[atributo]]
                if consulta:
                    columns = [desc[0] for desc in cursor.description] # Lista dos nomes das colunas da tabela
                    lista_dicionario = [dict(zip(columns, row)) for row in consulta] # lista das informaçoes dos produtos em forma de lista de dicionarios
                    lista_de_ids = [produto['produto_residencia_id'] for produto in lista_dicionario] # Lista com o id de cada produto da consulta
                    result = dict(zip(lista_de_ids, lista_dicionario)) # dicionario com chaves sendo os ids e os valores sendo um dicionario que representa as informações do produto
                    return result #row = result[i] # Combina os valores dos id com os valores da linha
                else: 
                    return {}
            except mysql.connector.Error as err:
                raise RuntimeError(f"Erro ao mostrar produtos listados do usuário: {str(err)}")
                
        else:
            raise RuntimeError(f"ERRO: o usuario de ID {id_usuario} não existe")
    
    # Pre_condição - usuario referente ao metodo tem que existir e ele tem que estar em ua residencia
    def registrar_compra(self, id_usuario: int, supermercado: str) -> bool:
        if self.__verificar_se_usuario_existe(id_usuario):
            if self.__verificar_se_usuario_tem_residencia(id_usuario):
                data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Formato de data compatível com MySQL
                query = "INSERT INTO compras (usuario_id, data_compra, supermercado) VALUES (%s, %s, %s)"
                try:
                    self.database.cursor.execute(query, (id_usuario, data, supermercado))
                    self.database.connection.commit()
                except mysql.connector.Error as err:
                    raise RuntimeError(f"Erro ao registrar compra: {str(err)}")
            else: 
                raise RuntimeError(f"Erro ao registrar compra, o usuario de ID {id_usuario} não possui residencia")
        else:
            raise RuntimeError(f"Erro ao registrar compra, o usuario de ID {id_usuario} não existe")
     
    # Pre_condição - usuario referente ao metodo tem que existir
    def mostrar_compras_de_usuario(self, id_usuario: int) -> dict:
        if self.__verificar_se_usuario_existe(id_usuario):
            query = "SELECT * FROM compras WHERE usuario_id = %s;"
            try:
                self.database.cursor.execute(query, (id_usuario,))
                consulta = self.database.cursor.fetchall() # list[list[atributo]]
                if consulta:
                    columns = [desc[0] for desc in self.database.cursor.description] # Lista dos nomes das colunas da tabela
                    lista_dicionario = [dict(zip(columns, row)) for row in consulta] # lista das informaçoes dos produtos em forma de lista de dicionarios
                    lista_de_ids = ([(dict['id_produto_residencia']) for dict in lista_dicionario])# Lista com o id de cada produto da consulta
                    result = dict(zip(lista_de_ids, lista_dicionario)) # dicionario com chaves sendo os ids e os valores sendo um dicionario que representa as informações do produto
                    return result #row = result[i] # Combina os valores dos id com os valores da linha
                else:
                    return {}
            except mysql.connector.Error as err:
                raise RuntimeError(f"Erro ao mostrar compras de usuário: {str(err)}")
        else:
            raise RuntimeError(f"ERRO: o usuario de ID {id_usuario} não existe")
    
    # Pre_condição - residencia referente ao metodo tem que existir
    def mostrar_todas_as_compras_da_residencia(self, id_residencia: int) -> dict:
        if self.__verificar_se_residencia_existe(id_residencia):
            query = "SELECT * FROM compras WHERE residencia_id = %s;"
            try:
                self.database.cursor.execute(query, (id_residencia,))
                consulta = self.database.cursor.fetchall() # list[list[atributo]]
                if consulta:
                    columns = [desc[0] for desc in self.database.cursor.description] # Lista dos nomes das colunas da tabela
                    lista_dicionario = [dict(zip(columns, row)) for row in consulta] # lista das informaçoes dos produtos em forma de lista de dicionarios
                    lista_de_ids = ([(dict['id_produto_residencia']) for dict in lista_dicionario])# Lista com o id de cada produto da consulta
                    result = dict(zip(lista_de_ids, lista_dicionario)) # dicionario com chaves sendo os ids e os valores sendo um dicionario que representa as informações do produto
                    return result #row = result[i] # Combina os valores dos id com os valores da linha
                else:
                    return {}
            except mysql.connector.Error as err:
                raise RuntimeError(f"Erro ao mostrar todas as compras da residência: {str(err)}")
                return {}
        else:
            raise RuntimeError(f"ERRO: a residencia de ID {id_residencia} não existe")
    
    def registrar_produto_comprado(self, id_produto_residencia:int, id_compra:int, preco:float, quantidade_comprada:int):
        query = '''INSERT INTO produtos_comprados (produto_residencia_id, compra_id, preco, quantidade_comprada) 
        VALUES (%s, %s, %s, %s); '''
        try:
            self.database.cursor.execute(query, (id_produto_residencia, id_compra, preco, quantidade_comprada))
            self.database.connection.commit()
        except mysql.connector.Error as err:
            raise RuntimeError(f"Erro ao registrar produto comprado: {str(err)}")
            
    # Pre_condição - compra referente ao metodo tem que existir    
    def mostrar_produtos_de_uma_compra(self, id_compra: int) -> dict:
        if self.__verificar_se_compra_existe(id_compra):
            query = '''
            SELECT id_produto_residencia, id_produto_comprado, compra_id, nome, preco, quantidade_unid, unidade_de_medida, categoria, preco_medio, quantidade_comprada
            FROM produtos_comprados 
            INNER JOIN produtos_residencia ON produtos_comprados.produto_residencia_id = produtos_residencia.id_produto_residencia
            WHERE compra_id = %s;'''
            try:
                self.database.cursor.execute(query, (id_compra,))
                consulta = self.database.cursor.fetchall() # list[list[atributo]]
                if consulta:
                    columns = [desc[0] for desc in self.database.cursor.description] # Lista dos nomes das colunas da tabela
                    lista_dicionario = [dict(zip(columns, row)) for row in consulta] # lista das informaçoes dos produtos em forma de lista de dicionarios
                    lista_de_ids = ([(dict['id_produto_residencia']) for dict in lista_dicionario])# Lista com o id de cada produto da consulta
                    result = dict(zip(lista_de_ids, lista_dicionario)) # dicionario com chaves sendo os ids e os valores sendo um dicionario que representa as informações do produto
                    return result #row = result[i] # Combina os valores dos id com os valores da linha
                else:
                    return {}
            except mysql.connector.Error as err:
                raise RuntimeError(f"Erro ao mostrar produtos de uma compra: {str(err)}")
        else:
            raise RuntimeError(f"ERRO: a compra de ID {id_compra} não existe")
   
    # Pre_condição - produto da dispensa referente ao metodo tem que existir 
    def deletar_produto_da_dispensa(self, id_produto_dispensa:int) ->bool:
        if self.__verificar_se_produto_dispensa_existe(id_produto_dispensa):
            query = "UPDATE produtos_residencia SET quantidade_existente = 0 WHERE id_produto_residencia = %s"
            try:        
                cursor = self.database.cursor
                cursor.execute(query, (id_produto_dispensa,))
                self.database.connection.commit()
            except mysql.connector.Error as err:
                raise RuntimeError(f"Erro ao deletar produto da dispensa de ID {id_produto_dispensa}: {str(err)}")
        else:
            raise RuntimeError(f"ERRO: o produto da dispensa de ID {id_produto_dispensa} não existe")
   
    def aumentar_quantidade_produto_dispensa(self, produto_residencia_id:int, quantidade_adicionada:int):
        if self.__verificar_se_produto_residencia_existe(produto_residencia_id):
            query = "UPDATE produtos_residencia SET quantidade_existente = quantidade_existente + %s WHERE id_produto_residencia = %s;"
            try:
                cursor = self.database.cursor
                cursor.execute(query, (quantidade_adicionada, produto_residencia_id))
                self.database.connection.commit()
            except mysql.connector.Error as err:
                raise RuntimeError(f"Erro adicionar quantidade de um produto de ID {produto_residencia_id} na dispensa {str(err)}")
        else:
            raise RuntimeError(f"ERRO: ao aumentar a quantiade de um produto na dispensa, o produto de ID {produto_residencia_id} não existe")
    
    def diminuir_quantidade_produto_dispensa(self, produto_residencia_id:int, quantidade_adicionada:int):
        if self.__verificar_se_produto_residencia_existe(produto_residencia_id):
            query = "UPDATE produtos_residencia SET quantidade_existente = quantidade_existente - %s WHERE id_produto_residencia = %s;"
            try:
                cursor = self.database.cursor
                cursor.execute(query, (quantidade_adicionada, produto_residencia_id))
                self.database.connection.commit()
            except mysql.connector.Error as err:
                raise RuntimeError(f"Erro diminuir quantidade de um produto de ID {produto_residencia_id} na lista geral: {str(err)}")
        else:
            raise RuntimeError(f"ERRO: ao diminuir a quantiade de um produto na dispensa, o produto de ID {produto_residencia_id} não existe")
        
    # Pre_condição - residencia referente ao metodo tem que existir 
    def mostrar_produtos_dispensa(self, id_residencia: int) -> dict:
        if self.__verificar_se_residencia_existe(id_residencia):
            query = "SELECT id_produto_residencia, quantidade_existente FROM produtos_residencia WHERE residencia_id = %s"
            try:
                self.database.cursor.execute(query, (id_residencia,))
                consulta = self.database.cursor.fetchall() # list[list[atributo]]
                if consulta:
                    columns = [desc[0] for desc in self.database.cursor.description] # Lista dos nomes das colunas da tabela
                    lista_dicionario = [dict(zip(columns, row)) for row in consulta] # lista das informaçoes dos produtos em forma de lista de dicionarios
                    lista_de_ids = ([(dict['id_produto_residencia']) for dict in lista_dicionario])# Lista com o id de cada produto da consulta
                    result = dict(zip(lista_de_ids, lista_dicionario)) # dicionario com chaves sendo os ids e os valores sendo um dicionario que representa as informações do produto
                    return result #row = result[i] # Combina os valores dos id com os valores da linha
                else:
                    return {}
            except mysql.connector.Error as err:
                raise RuntimeError(f"Erro ao mostrar produtos da dispensa: {str(err)}")
                
        else:
             raise RuntimeError(f"ERRO: a residencia de ID {id_residencia} não existe")
    
    def registrar_transferencia(self, id_compra:int, valor:float, id_usuario_beneficiario:int, id_usuario_pagador:int):
       data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       query = "INSERT INTO dividas (compra_id,valor, beneficiado, pagador, data_divida) VALUES (%s, %s, %s, %s, %s);"
       try:
           self.database.cursor.execute(query,(id_compra, valor, id_usuario_beneficiario, id_usuario_pagador, data))
           self.database.connection.commit()
       except mysql.connector.Error as err:
           raise RuntimeError(f"Erro ao registrar divida: {str(err)}")
    
    # Pre-condição: a divida tem que existir
    def confirmar_transferencia(self, id_divida:int):
        if self.__verificar_se_divida_existe(id_divida):
            data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            query = f"UPDATE dividas SET data_debito = '{data}' WHERE id_divida = '{id_divida}';"
            self.database.cursor.execute(query)
            self.database.connection.commit()
        else:
            raise RuntimeError(f"ERRO: divida de ID {id_divida} não existe no banco") 
        
    #consultar dividas confirmadas e não confirmadas
    
'''

Falta:
    integração
    adição de funcionalidades
    
Ideias:
    Saldo: separar e planejar um valor do mes nas compras 
    Validade: opção de registrar a validade de um produto para não perde-lo
    listas: o usuario ter diferentes listas pessoais diferentes momentos 
    supermercados: analisar preços dos produtos comprados em cada supermercado
    estimativa da duração do produto: de acordo com consumo refrequente e homegenio do produto, estimar a duração dele 
'''

