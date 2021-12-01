#from typing_extensions import ParamSpecKwargs
from flask import Flask
import pymongo 
from pymongo import MongoClient
from pymongo.errors import ConfigurationError, ConnectionFailure, OperationFailure
from .to_ignore import var
import uuid, json

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

    def getConnectionStatus(self):
        return self.connection_status

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
    def checkForUser(self, userName):

        userCheck = self.userCollection.find_one({"_id" : userName})

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
        jsonDict = json.loads(User)
        if self.checkForUser(jsonDict['_id']):
            return False
        else:
            self.userCollection.insert_one(jsonDict)
            return True

    #Requires: userName
    #Modifies: will return a user json of the specificed username
    #Effects: when called, if the username exists in the db, will return the user, else return false
    def getUser(self, userName):
        
        if not self.checkForUser(userName):
            return False
        else:
            return self.userCollection.find_one({"_id" : userName})

    
    #Requires: userName
    #Modifies: will delete user from db class
    #Effects: Will delete the user from the user collection based on the if the 
    #         username exists. 
    def deleteUser(self, userName):
        
        if not self.checkForUser(userName):
            return False
        else:
            self.userCollection.delete_one({"_id" : userName})
            return True



#usage
if __name__ == '__main__':
    pass
    #On registration
    #1. Get form info
    #make a user class
    
    #2. Check if username exists in db- if false go to #3 else send error message- user already exists
    #if POFDB.checkForUser(username):
    #    print("User Exists")
    #else:
    #    a = User(stuff[])
    #    POFDB.addUser(a) #-internally will call check if exists
    
    #3. Make a new user class with info- user class initialization (with only 3 arguements (no salt)) will be returned- 3 arguments will make a salt and hash the password
    #4. call add to db
    #5. add to db will first verify user does not exist, if true
    #6. add information to the db
    # 
    # On login
    #1. get form info
    #2. check if username exists- if true go to 3, else error message username not found
    #3. pull user from db using the given username
    #4. using given salt from pulled user info, call function to compare password- so verifyPassword(enteredPassword)- will do the encoding and return
    #whether the hashed password matches stored password
    #5. if match- successful login

#list_collection_names
#myclient.list_databases():

