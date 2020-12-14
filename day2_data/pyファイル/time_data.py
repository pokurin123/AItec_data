from var import Var
from db import DB
class DataAccess:
    def get_spots(self):
        query = "SELECT when_build FROM my_spot4 WHERE ID = 1"
        data = ()
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)
print("動いてる1")
