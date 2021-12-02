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
#######################################

    #Getters
    def getUserName(self):
        return self.Username
    
    def getPassword(self):
        return self.password

    def getEmail(self):
        return self.email

    #Requires: psw and salt
    #Modifies: 
    #Effects: When called and given a password and a salt, will first convert both to type byte
    #if not already in that form, and then return a hash of the psw using the salt
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
        return hashedCheckPassword #== self.password 

    #Requires: 
    #Modifies: Will create a dictionary which is transformed into a JSON
    #Effects: When called, will return a json format of the user class
    def userToJson(self):

        user_Dict = {
            "_id" : self.Username,
            "email": self.email,
            "password": binascii.hexlify(self.password).decode('utf-8'),
            #"password": str(self.hashUserPassword()).replace("'", '"'),#.decode('utf-8'),
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
        
        #Determined if is not already an instance of a dictionary
        if not isinstance(user_json, dict):
            user_dict = json.loads(user_json)
        else:
            user_dict = user_json

        #checks if the passed user dictionary contains all of the required inforamtion
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
    




