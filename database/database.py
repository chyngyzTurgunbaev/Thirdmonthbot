# import sqlite3
# from .queries import Queries
#
#
# class Database:
#     def __init__(self, path: str):
#         self.path = path
#
#     def create_table(self):
#         # connect = sqlite3.connect(self.path)
#         # контекстный менеджер
#         with sqlite3.connect(self.path) as connect:
#             connect.execute(Queries.CREATE_TABLE_REVIEW)
#             connect.execute(Queries.CREATE_TABLE_CATEGORIES)
#             connect.execute(Queries.CREATE_TABLE_DISHES)
#             connect.execute(Queries.INSERT_INTO_DISHES)
#             connect.execute(Queries.INSERT_INTO_CAT)
#             connect.commit()
#
#     def execute(self, query: str, params: tuple = None):
#         with sqlite3.connect(self.path) as connect:
#             connect.execute(query, params)
#
#
#     def fetch(self, query:str,params: tuple = None,fetchmany: bool = False):
#         with sqlite3.connect(self.path) as connect:
#             result = connect.execute(query, params)
#             return result.fetchall()
import sqlite3
from database.queries import Queries


class Database:
    def __init__(self, path: str):
        self.path = path

    def create_table(self):
        with sqlite3.connect(self.path) as connect:
            connect.execute(Queries.CREATE_TABLE_REVIEW)
            connect.execute(Queries.CREATE_TABLE_CATEGORIES)
            connect.execute(Queries.CREATE_TABLE_DISHES)
            connect.execute(Queries.INSERT_INTO_DISHES)
            connect.execute(Queries.INSERT_INTO_CAT)
            connect.commit()

    def execute(self, query: str, params: tuple = None):
        with sqlite3.connect(self.path) as connect:
            if params:
                connect.execute(query, params)
            else:
                connect.execute(query)

    def fetch(self, query: str, params: tuple = None, fetchmany: bool = False):
        with sqlite3.connect(self.path) as connect:
            cursor = connect.execute(query, params or ())
            return cursor.fetchall()
