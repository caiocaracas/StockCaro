import mysql.connector
from abc import ABC
import datetime

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
    
    def __verificar_se_divida_existe(self, id_divida: int) -> bool:
        query = "SELECT 1 FROM dividas WHERE id_divida = %s;"
        try:
            cursor = self.database.cursor
            cursor.execute(query, (id_divida,))
            result = cursor.fetchone()
            return bool(result)
        except mysql.connector.Error as err:
            raise RuntimeError(f"Erro ao verificar se divida de ID {id_divida} existe no banco: {str(err)}")
  
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
    
    def __verificar_se_produto_dispensa_existe(self, id_produto_dispensa: int) -> bool:
        query = "SELECT 1 FROM produtos_dispensas WHERE id_produto_dispensa = %s;"
        try:
            cursor = self.database.cursor
            cursor.execute(query, (id_produto_dispensa,))
            result = cursor.fetchone()
            return bool(result)
        except mysql.connector.Error as err:
            raise RuntimeError(f"Erro ao verificar se produto na dispensa de ID {id_produto_dispensa} existe no banco: {str(err)}")

    def __verificar_se_produto_residencia_e_usuario_existe(self, id_produto_residencia: int, id_usuario:int) -> bool:
        query = "SELECT 1 FROM produtos_residencia__usuarios WHERE (produto_residencia_id = %s AND usuario_id = %s);"
        try:
            cursor = self.database.cursor
            cursor.execute(query, (id_produto_residencia, id_usuario))
            result = cursor.fetchone()
            return bool(result)
        except mysql.connector.Error as err:
            raise RuntimeError(f"Erro ao verificar se o usuario de ID {id_usuario} usa o produto de ID {id_produto_residencia}: {str(err)}")
    
    #Tested
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

    #Tested
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

    #Tested            
    ## Pre-condição - o usuário referente ao método tem que existir
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

    #Tested        
    ## Pre_condição - usuario referente ao metodo tem que existir
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

    #Tested     
    ## Pre_condição - usuario referente ao metodo tem que existir
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
    
    #Tested 
    ##
    def registrar_residencia(self, id_adm:int) -> int:
       query = "INSERT INTO residencias (usuario_adm_id) VALUES (%s)"
       try:
           self.database.cursor.execute(query, (id_adm,))
           self.database.connection.commit()
       except mysql.connector.Error as err:
           raise RuntimeError(f"Erro ao criar uma residencia: {str(err)}")

    #Tested    
    ## Pre_condição - residencia referente ao metodo tem que existir 
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
    
    #Tested
    ## Pre_condição - residencia referente ao metodo tem que existir
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

    #Tested 
    ## Pre_condição - residencia e usuario referente ao metodo tem que existir   
    def adicionar_usuario_em_residencia(self, id_residencia:int, id_usuario:int):
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
    
    #Tested
    ## Pre_condição - residencia referente ao m/etodo tem que existir 
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
    
    #Tested
    ## Pre_condição - residencia referente ao metodo tem que existir
    def mostrar_moradores(self, id_residencia:int) -> dict:
        if self.__verificar_se_residencia_existe(id_residencia):
            query = "SELECT * FROM usuarios WHERE residencia_id = %s;"
            try:
               cursor = self.database.cursor
               cursor.execute(query, (id_residencia,))
               result = cursor.fetchall()
               if result:
                   columns = [desc[0] for desc in self.database.cursor.description]  # Obter os nomes das colunas
                   return [dict(zip(columns, row)) for row in result]  # Combinar colunas e valores em um dicionário
               else:
                   return {}
            except mysql.connector.Error as err:
               # Aqui você pode levantar uma exceção personalizada ou apenas logar o erro
               raise RuntimeError(f"Erro ao buscar moradores: {str(err)}")
               return {}
        else:
             raise RuntimeError(f"ERRO: a residencia de ID {id_residencia} não existe")

    # Tested
    def registrar_produto_residencia(self, id_residencia, nome:str, quantidade:int, unid_medida:str, categoria):
        query = "INSERT INTO produtos_residencia (residencia_id, nome, quantidade_unid, unidade_de_medida, categoria) VALUES (%s, %s, %s, %s, %s )"
        try: 
            self.database.cursor.execute(query, (id_residencia, nome, quantidade, unid_medida, categoria)) 
            self.database.connection.commit()
        except mysql.connector.Error as err:
            raise RuntimeError(f"Erro ao registrar produto na residência de ID {id_residencia}: {str(err)}")
    
    # Tested
    ## Pre_condição - produto da residencia referente ao metodo tem que existir
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
    
    # Tested
    ## Pre_condição - residencia tem que existir
    def mostrar_produtos_cadastrados_da_residencia(self, id_residencia: int) -> dict:
        if self.__verificar_se_residencia_existe(id_residencia):
            query = "SELECT * FROM produtos_residencia WHERE residencia_id = %s;"
            try:
                cursor = self.database.cursor
                cursor.execute(query, (id_residencia,))
                result = cursor.fetchall()
                if result:
                    columns = [desc[0] for desc in cursor.description]  # Obter os nomes das colunas
                    return [dict(zip(columns, row)) for row in result]  # Combinar colunas e valores em um dicionário
                else:
                    return {}
            except mysql.connector.Error as err:
                raise RuntimeError(f"Erro ao mostrar produtos cadastrados da residência: {str(err)}")
                return {}
        else:
            raise RuntimeError(f"ERRO: a residencia de ID {id_residencia} não existe no banco")
    
    # Tested
    ## Pre_condição - produto residencia tem que existir
    def mostar_produto_da_residencia(self, id_produto_residencia: int) -> dict:
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
    
    # Tested
    def adicionar_produto_lista_pessoal(self, id_produto_residencia, usuario_id, quantidade):
        query = "INSERT INTO produtos_listados_pessoais (produto_residencia_id, usuario_id, quantidade_listada) VALUES (%s, %s, %s);"
        try:
            self.database.cursor.execute(query, (id_produto_residencia, usuario_id, quantidade))
            self.database.connection.commit()
        except mysql.connector.Error as err:
            raise RuntimeError(f"Erro ao registrar produto na lista pessoal de ID {usuario_id}: {str(err)}")
            
    # Tested
    ## Pre_condição - produto listado referente ao metodo tem que existir
    def deletar_produto_lista_pessoal(self, id_produto_listado):
        if self.__verificar_se_produto_listado_pessoal_existe(id_produto_listado):
            query = "DELETE FROM produtos_listados_pessoais WHERE id_produto_listado_pessoal = %s;"
            try:
                cursor = self.database.cursor
                cursor.execute(query, (id_produto_listado,))
                self.database.connection.commit()
            except mysql.connector.Error as err:
                raise RuntimeError(f"Erro ao deletar o produto listado de ID {id_produto_listado}: {str(err)}")
        else:
            raise RuntimeError(f"ERRO: o produto listado de ID {id_produto_listado} não existe")
    
    # Tested
    ## Pre_condição - usuario referente ao metodo tem que existir
    def mostrar_produtos_listados_do_usuario(self, id_usuario: int) -> dict:
        if self.__verificar_se_usuario_existe(id_usuario):
            query = '''
            SELECT id_produto_listado_pessoal, id_produto_residencia, residencia_id, usuario_id, quantidade_listada, nome, quantidade_unid, unidade_de_medida, categoria, preco_medio
            FROM produtos_listados_pessoais
            INNER JOIN produtos_residencia 
            ON produtos_listados_pessoais.produto_residencia_id = produtos_residencia.id_produto_residencia
            WHERE usuario_id = %s; '''
            try:
                cursor = self.database.cursor
                cursor.execute(query, (id_usuario,))
                result = self.database.cursor.fetchall()
                if result:
                    columns = [desc[0] for desc in cursor.description]  # Obter os nomes das colunas
                    return [dict(zip(columns, row)) for row in result]  # Combinar colunas e valores em uma lista de dicionários
                else: 
                    return {}
            except mysql.connector.Error as err:
                raise RuntimeError(f"Erro ao mostrar produtos listados do usuário: {str(err)}")
                
        else:
            raise RuntimeError(f"ERRO: o usuario de ID {id_usuario} não existe")
        
    # Tested
    # Pre-condição: um registro não pode ser duplicado
    def registrar_usuario_consumidor_de_um_produto(self, id_produto_residencia:int, id_usuario:int) -> None:
        if not self.__verificar_se_produto_residencia_e_usuario_existe(id_produto_residencia, id_usuario):
            query = "INSERT INTO produtos_residencia__usuarios (produto_residencia_id, usuario_id) VALUES (%s, %s);"
            try:
                self.database.cursor.execute(query, (id_produto_residencia, id_usuario))
                self.database.connection.commit()
            except mysql.connector.Error as err:
                raise RuntimeError(f"ERRO: erro ao registrar um produto: {str(err)}")

        else:
            raise RuntimeError(f"ERRO: erro ao registrar consumidor de um produto, o usuario de ID {id_usuario} ou produto de ID {id_produto_residencia} não existem")
    
    # Tested
    ## Pre_condição - produto da residencia e usuario referente ao metodo tem que existir
    def deletar_usuario_que_consome_um_produto(self, id_produto_residencia:int, id_usuario:int):
        query = "DELETE FROM produtos_residencia__usuarios WHERE  produto_residencia_id = %s AND usuario_id = %s;"
        if self.__verificar_se_produto_residencia_e_usuario_existe(id_produto_residencia, id_usuario):
            try:
               cursor = self.database.cursor
               cursor.execute(query, (id_produto_residencia, id_usuario))
               self.database.connection.commit()
            except mysql.connector.Error as err:
                raise RuntimeError(f"Erro ao deletar registro do usuario de ID {id_usuario} de consumir o produto {id_produto_residencia}: {str(err)}")
        else:
            raise RuntimeError(f"ERRO: o usuario de ID {id_usuario} não consome o produto de ID {id_produto_residencia}")

    # Tested
    ## Pre_condição - produto da residencia referente ao metodo tem que existir
    def mostrar_usuarios_consomem_certo_produto(self, id_produto_residencia: int) -> dict:
        if self.__verificar_se_produto_residencia_existe(id_produto_residencia):
            query = '''SELECT * FROM usuarios WHERE id_usuario IN (
                SELECT usuario_id FROM produtos_residencia__usuarios WHERE produto_residencia_id = %s);'''
            try:
                self.database.cursor.execute(query, (id_produto_residencia,))
                result = self.database.cursor.fetchall()
                if result:
                    columns = [desc[0] for desc in self.database.cursor.description]  # Obter os nomes das colunas
                    return [dict(zip(columns, row)) for row in result]  # Combinar colunas e valores em um dicionário
                else:
                    return {}
            except mysql.connector.Error as err:
                raise RuntimeError(f"Erro ao mostrar usuários que consomem certo produto: {str(err)}")
                return {}
        else:
            raise RuntimeError(f"ERRO: o produto residencia de ID {id_produto_residencia} não existe")
    
    # Tested
    ## Pre_condição - usuario referente ao metodo tem que existir e ele tem que estar em ua residencia
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
    
    
    ## Pre_condição - usuario referente ao metodo tem que existir
    def mostrar_compras_de_usuario(self, id_usuario: int) -> dict:
        if self.__verificar_se_usuario_existe(id_usuario):
            query = "SELECT * FROM compras WHERE usuario_id = %s;"
            try:
                self.database.cursor.execute(query, (id_usuario,))
                result = self.database.cursor.fetchall()
                if result:
                    columns = [desc[0] for desc in self.database.cursor.description]  # Obter os nomes das colunas
                    return [dict(zip(columns, row)) for row in result]    # Combinar colunas e valores em um dicionário
                else:
                    return {}
            except mysql.connector.Error as err:
                raise RuntimeError(f"Erro ao mostrar compras de usuário: {str(err)}")
        else:
            raise RuntimeError(f"ERRO: o usuario de ID {id_usuario} não existe")
    
    # Tested
    ## Pre_condição - residencia referente ao metodo tem que existir
    def mostrar_todas_as_compras_da_residencia(self, id_residencia: int) -> dict:
        if self.__verificar_se_residencia_existe(id_residencia):
            query = "SELECT * FROM compras WHERE residencia_id = %s;"
            try:
                self.database.cursor.execute(query, (id_residencia,))
                result = self.database.cursor.fetchall()
                if result:
                    columns = [desc[0] for desc in self.database.cursor.description]  # Obter os nomes das colunas
                    return dict(zip(columns, result))  # Combinar colunas e valores em um dicionário
                else:
                    return {}
            except mysql.connector.Error as err:
                raise RuntimeError(f"Erro ao mostrar todas as compras da residência: {str(err)}")
                return {}
        else:
            raise RuntimeError(f"ERRO: a residencia de ID {id_residencia} não existe")
    

    ## Tested
    def registrar_produto_comprado(self, id_produto_residencia:int, id_compra:int, preco:float, quantidade_comprada:int):
        query = '''INSERT INTO produtos_comprados (produto_residencia_id, compra_id, preco, quantidade_comprada) 
        VALUES (%s, %s, %s, %s); '''
        try:
            self.database.cursor.execute(query, (id_produto_residencia, id_compra, preco, quantidade_comprada))
            self.database.connection.commit()
        except mysql.connector.Error as err:
            raise RuntimeError(f"Erro ao registrar produto comprado: {str(err)}")
            
    # Tested
    ## Pre_condição - compra referente ao metodo tem que existir    
    def mostrar_produtos_de_uma_compra(self, id_compra: int) -> dict:
        if self.__verificar_se_compra_existe(id_compra):
            query = '''
            SELECT id_produto_residencia, id_produto_comprado, compra_id, nome, preco, quantidade_unid, unidade_de_medida, categoria, preco_medio, quantidade_comprada
            FROM produtos_comprados 
            INNER JOIN produtos_residencia ON produtos_comprados.produto_residencia_id = produtos_residencia.id_produto_residencia
            WHERE compra_id = %s;'''
            try:
                self.database.cursor.execute(query, (id_compra,))
                result = self.database.cursor.fetchall()
                if result:
                    columns = [desc[0] for desc in self.database.cursor.description]  # Obter os nomes das colunas
                    return [dict(zip(columns, row)) for row in result]  # Combinar colunas e valores em um dicionário
                else:
                    return {}
            except mysql.connector.Error as err:
                raise RuntimeError(f"Erro ao mostrar produtos de uma compra: {str(err)}")
        else:
            raise RuntimeError(f"ERRO: a compra de ID {id_compra} não existe")
        
    # Tested
    def adicionar_produto_na_dispensa(self, id_produto_comprado:int, quantidade:int) ->bool:
        query = "INSERT INTO produtos_dispensas (produto_comprado_id, quantidade_existente) VALUES (%s, %s);"
        try:
            self.database.cursor.execute(query, (id_produto_comprado, quantidade))
            self.database.connection.commit()
        except mysql.connector.Error as err:
            raise RuntimeError(f"Erro ao registrar produto na dispensa: {str(err)}")

    # Tested      
    ## Pre_condição - produto da dispensa referente ao metodo tem que existir 
    def deletar_produto_da_dispensa(self, id_produto_dispensa:int) ->bool:
        if self.__verificar_se_produto_dispensa_existe(id_produto_dispensa):
            query = "DELETE FROM produtos_dispensas WHERE id_produto_dispensa = %s;"
            try:        
                cursor = self.database.cursor
                cursor.execute(query, (id_produto_dispensa,))
                self.database.connection.commit()
            except mysql.connector.Error as err:
                raise RuntimeError(f"Erro ao deletar produto da dispensa de ID {id_produto_dispensa}: {str(err)}")
        else:
            raise RuntimeError(f"ERRO: o produto da dispensa de ID {id_produto_dispensa} não existe")
   
    # Tested
    # Pre_condição - residencia referente ao metodo tem que existir 
    def mostrar_produtos_dispensa(self, id_residencia: int) -> dict:
        if self.__verificar_se_residencia_existe(id_residencia):
            query = '''
            SELECT id_produto_residencia, id_produto_comprado, produto_comprado_id, compra_id, nome, preco, quantidade_unid, unidade_de_medida, categoria, preco_medio, quantidade_comprada, quantidade_existente
            FROM produtos_dispensas 
            INNER JOIN produtos_comprados ON produtos_dispensas.produto_comprado_id = produtos_comprados.id_produto_comprado
            INNER JOIN produtos_residencia ON produtos_comprados.produto_residencia_id = produtos_residencia.id_produto_residencia
            WHERE produtos_residencia.residencia_id = %s;'''
            try:
                self.database.cursor.execute(query, (id_residencia,))
                result = self.database.cursor.fetchall()
                if result:
                    columns = [desc[0] for desc in self.database.cursor.description]  # Obter os nomes das colunas
                    return [dict(zip(columns, row)) for row in result]  # Combinar colunas e valores em um dicionário
                else:
                    return {}
            except mysql.connector.Error as err:
                raise RuntimeError(f"Erro ao mostrar produtos da dispensa: {str(err)}")
                
        else:
             raise RuntimeError(f"ERRO: a residencia de ID {id_residencia} não existe")
    
    # Tested
    def registrar_dividas(self, id_compra:int, valor:float, id_usuario_beneficiario:int, id_usuario_pagador:int):
       data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       query = "INSERT INTO dividas (compra_id,valor, beneficiado, pagador, data_divida) VALUES (%s, %s, %s, %s, %s);"
       try:
           self.database.cursor.execute(query,(id_compra, valor, id_usuario_beneficiario, id_usuario_pagador, data))
           self.database.connection.commit()
       except mysql.connector.Error as err:
           raise RuntimeError(f"Erro ao registrar divida: {str(err)}")
    
    # Tested
    ## Pre-condição: a divida tem que existir
    def registrar_debito(self, id_divida:int):
        if self.__verificar_se_divida_existe(id_divida):
            data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            query = f"UPDATE dividas SET data_debito = '{data}' WHERE id_divida = '{id_divida}';"
            self.database.cursor.execute(query)
            self.database.connection.commit()
        else:
            raise RuntimeError(f"ERRO: divida de ID {id_divida} não existe no banco") 
        
    
    
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

