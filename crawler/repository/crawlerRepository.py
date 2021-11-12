from ..dataBase.connection import Connection


class CrawlerRepository:
    def __init__(self):
        cnt = Connection.mongo_connect()
        self.db = cnt['inputs']

    def create(self, data):
        self.db.insert_one(data)
