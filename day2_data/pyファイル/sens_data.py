from var import Var
from db import DB
class DataAccess:
    def get_spots(self):
        query = "SELECT spot_type,rating_5Lv,history,culture,nature,religion,amusement FROM my_spot4 WHERE ID = 10"
        data = ()
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)

print("動いてる1")
