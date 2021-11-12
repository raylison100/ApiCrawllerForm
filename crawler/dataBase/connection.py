from pymongo import MongoClient


class Connection:
    @staticmethod
    def mongo_connect():
        client = MongoClient(port=27017)

        return client['crawler']