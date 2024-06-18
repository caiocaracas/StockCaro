from scripts.GUI import GUI
from scripts.Repository import Database, UserRepository

senha_root = "senha"

def main():
  database = Database("localhost", "root", senha_root, "gerenciador_mercado")
  db = UserRepository(database)

  interface = GUI(db)

  interface.master.mainloop()


if __name__ == "__main__":
  main()
