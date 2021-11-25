from flask import Flask
import pymongo 
from pymongo import MongoClient
from pymongo.errors import ConfigurationError, ConnectionFailure, OperationFailure
from .to_ignore import var
import uuid

#db = cluster["test1"]
#collection = db["test"]

class POFDB:

    def __init__(self):
        
        try:
            cluster = MongoClient(var)
            db = cluster["POFDataBase"]
            temp = cluster.admin.command('ping')
            print(temp)
            

            self.mgclient = cluster
            self.db = db
            self.userCollection = db["Users"]
            self.connection_status = True
            #get databases
            #dbs = cluster.list_databases()
            #print(dbs)
            #get collections
        except ConfigurationError:
            print("Configuration Error: Database Connection Failed")
            self.connection_status = False
        except ConnectionFailure:
            print("Execption Error: Database Connection Failed")
            self.connection_status = False
            return
        except OperationFailure:
            print("Authentication Failure: Invalid Credentials")
            self.connection_status = False
            return



        #self.userCollection.insert_one({"_id": 1 ,"name" : "Ben"})

    def verify_Location():
        pass

    #User interface

    def checkForUser(self, User):
        
        userCheck = self.userCollection.find_one({"_id" : User.username})

        if userCheck == None:
            return False

        else:
            return True


    def addUser(self, User):
        
        if self.checkForUser:
            return "Error: User already exists"
        else:
            self.userCollection.insert_one(User)
            return 1


    def getUser(self, User):
        
        if not self.checkForUser:
            return "Error: User does not exist"
        else:
            return self.userCollection(User)







#list_collection_names
#myclient.list_databases():


#test = POFDB(url)
#cluster = MongoClient(var)
#temp = cluster.admin.command('ping')
#print(temp)
#dbs = cluster.list_databases()
#collections = cluster.list

#for db in dbs:
#    print(db)

#db = POFDB()
#print(db.userCollection.find_one({"_id" : 1}))

#for cursor in db.userCollection.find({"_id" : 0}):
#    print(cursor)