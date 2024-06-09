from scripts.GUI import GUI
from scripts.Repository import Database, UserRepository

def main():
  database = Database("localhost", "root", "gpires10", "gerenciador_mercado")
  db = UserRepository(database)

  interface = GUI(db)

  interface.master.mainloop()


if __name__ == "__main__":
  main()
