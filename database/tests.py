from Repository import Database, UserRepository
from view import *

db = Database("localhost", "root", "gpires10", "gerenciador_mercado")
banco = UserRepository(db)

#banco.registrar_usuario("Arthur", "hdafgp@gmail.com", "1234")
user = banco.login("hdafgp@gmail.com")

print(user)

db.close()