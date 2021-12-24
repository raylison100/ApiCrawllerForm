from ..dataBase.connection import Connection


class CrawlerRepository:
    def __init__(self):
        client = Connection.mongo_connect()
        database = client['crawler']
        self.collection = database['inputs']

    def create(self, data):
        self.collection.insert_one(data)

    def list(self):
        result = self.collection.find({})
        return result
