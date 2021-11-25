from flask import Flask
import json
from POFWebpage import db
import hashlib, os, binascii




class User:

    #Requires: Username, email, password, optional salt
    #Effects: When passed the proper information, will return a user class
    def __init__(self, Username, email, password, salt=None):

        if salt is None:
            self.Username = Username
            self.email = email    
            self.salt = os.urandom(32)
            self.password = User.hashPassword(password, self.salt)   
            #self.organization = organization
        else:
            self.Username = Username
            self.email = email    
            #salt will be stored as byte
            if isinstance(salt, bytes):
                self.salt = salt 
            else:
               self.salt = salt.encode('utf-8')
            self.password = User.hashPassword(password, salt)  
            #self.organization = organization

#######Depreciated######################    
    #Requires: 
    #Modifies: 
    #Effects: Will create a hashed password from the user salt and the password
#    def hashUserPassword(self):
#        #below is old code that didnt work
#        #return hashlib.pbkdf2_hmac('sha256',self.password.encode('utf-8'),self.salt, 100000).decode()
#        return hashlib.pbkdf2_hmac('sha256',self.password.encode('utf-8'),self.salt, 100000)
#######################################3

    def hashPassword(psw, salt):
        if not isinstance(salt, bytes) :
            salt = salt.encode('utf-8')
        
        if not isinstance(psw, bytes) :
            psw = psw.encode('utf-8')

        return hashlib.pbkdf2_hmac('sha256', psw, salt, 100000)
    
    #Requires: string pswd
    #Modifies: 
    #Effects: When called and given a password, will return if the key that results from hashing the password is 
    #equal to the key of the current user
    def checkPassWordsMatch(self, pswd):
        hashedCheckPassword = User.hashPassword(pswd, self.salt)
        return hashedCheckPassword == self.password 

    #Requires: 
    #Modifies: Will create a dictionary which is transformed into a JSON
    #Effects: When called, will return a json format of the user class
    def userToJson(self):

        user_Dict = {
            "_id" : self.Username,
            "email": self.email,
            "password": binascii.hexlify(self.password).decode('utf-8'),
            #code that didnt work"password": str(self.hashUserPassword()).replace("'", '"'),#.decode('utf-8'),
            "salt": binascii.hexlify(self.salt).decode('utf-8')#.replace("'", '"')
            #"first_name": self.first_name,
            #"last_name": self.last_name,
            #"organization": self.organization
         }


        return json.dumps(user_Dict)

    
    #Requires: Json object in the format of a user
    #Modifies: 
    #Effects: When called, will return a user class that is created from the passed json object. Will only pass a user object if
    #the json contains all the needed info
    def jsonToUser(user_json):
        
        user_dict = json.loads(user_json)
        if User.verifyIfJsonIsUser(user_dict):
            return User(user_dict['_id'], user_dict['email'], user_dict['password'], user_dict['salt'])
        else:
            return "Error: Json does not have all required fields to be a user"



    #Requires: Json object
    #Modifies: 
    #Effects: Will check if the json contains all the information to be classified as a user
    def verifyIfJsonIsUser(user_dict):
        
        if all (keys in user_dict for keys in ('_id', 'email', 'password', 'salt')):
            return True
        else:
            return False

    



#Usage

if __name__ == '__main__':
    newUser = User("Ben", "bc@gmail.com)", 12345)

    jSON = ""

    newUser.user_to_json()
    newUser.verifyIfJsonIsUser()
    newUser2 = newUser.json_to_user(jSON)

    newUser.check_existance()
    newUser.addUserToDB()
    
    
    #On registration
    #1. Get form info
    #2. Check if username exists in db- if false go to #3 else send error message- user already exists
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



        #Requires: db object
    #Modifies: 
    #Effects: When called, will check if the username exists in the database, if not will return false, if the user is in the db will return true
    #def checkIfUserExistsInDB(username, db):
        
        #pass to database to make sure doesnt exist- pass the user_to_json
    #    dbCheck = db.checkForUser(username)
        
        #if exists return error
    #    if dbCheck == 1:
    #        return 1
    #    else:
        #if not return user successfully created
    #        return dbCheck


        #Requires: db object
    #Modifies: will add user to db
    #Effects: Will create a hashed password from the user salt and the password
    #def addUserToDB(self, db):
        #pass user to database to attempt creating a new user
    #    return db.addUser(self.user_to_json())
    
    #Requires: db object, username
    #Modifies: creates user from db
    #Effects: Will create a hashed password from the user salt and the password
    #def getUserFromDatabase(userName, db):
    #    pass