import pymongo
import  os
__author__ = 'jslvtr'


class Database(object):
    URI = 'mongodb://heroku_2c6b6dhv:123@ds035673.mlab.com:35673/heroku_2c6b6dhv'
    DATABASE = None

    @staticmethod
    def initialize():
        try:
            client = pymongo.MongoClient(Database.URI)
            Database.DATABASE = client.get_default_database()
        except:
            print("fasfs \n")

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection, query, data):
        Database.DATABASE[collection].update(query, data, upsert=True)

    @staticmethod
    def remove(collection, query):
        return Database.DATABASE[collection].remove(query)
