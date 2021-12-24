import os

from pymongo import MongoClient


class Connection:
    @staticmethod
    def mongo_connect():
        client = MongoClient(host=os.getenv('MONGO_HOST'), port=27018)
        server_info = client.server_info()
        print(server_info)
        return client
