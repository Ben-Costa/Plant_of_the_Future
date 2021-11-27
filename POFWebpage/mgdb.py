from typing_extensions import ParamSpecKwargs
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

    #Requires: 
    #Modifies: 
    #Effects:
    def verify_Location():
        pass

    #####User interface#####
    #Requires: userName
    #Modifies: 
    #Effects: When passed a User json, will check if the user _id exists in the user collection.
    #         if the user exists, then will return true. Else will return false.
    def checkForUser(self, User):
        
        userCheck = self.userCollection.find_one({"_id" : User.username})

        if userCheck == None:
            return False

        else:
            return True

    #Requires: User json
    #Modifies: Will add a user to the user collection in the database
    #Effects: When passed a user json, will first check to see if the user exists with the
    #         checkForUser function. If true is returned, will give an error saying the user
    #         exists in the database. Else the user is added to the user collection and 1 is returned
    def addUser(self, User):
        
        if self.checkForUser:
            return "Error: User already exists"
        else:
            self.userCollection.insert_one(User)
            return 1

    #Requires: userName
    #Modifies: will return a user json of the specificed username
    #Effects:
    def getUser(self, User):
        
        if not self.checkForUser:
            return "Error: User does not exist"
        else:
            return self.userCollection(User)

    
    #Requires: User
    #Modifies: will delete user from db class
    #Effects: Will delete the user from the user collection based on the if the 
    #         username exists. 
    def deleteUser(self, User):
        pass




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