from pymongo import MongoClient


class Connection:
    @staticmethod
    def mongo_connect():
        client = MongoClient('localhost', 27018)

        return client['crawler']
