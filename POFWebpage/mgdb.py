from flask import Flask
import pymongo 
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure

#db = cluster["test1"]
#collection = db["test"]

class POFDB:

    def __init__(self, db_url):
        
        try:
            cluster = MongoClient(db_url)
            temp = cluster.admin.command('ping')
            print(temp)
            
            #get databases
            #dbs = cluster.list_databases()
            #print(dbs)
            #get collections

        except ConnectionFailure:
            return("Execption Error: Database Connection Failed")
        except OperationFailure:
            return("Authentication Failure: Invalid Credentials")

    def verify_Location():
        pass

#list_collection_names
#myclient.list_databases():


#test = POFDB(url)
cluster = MongoClient('')
temp = cluster.admin.command('ping')
print(temp)
dbs = cluster.list_databases()
print(dbs)
print(type(dbs))