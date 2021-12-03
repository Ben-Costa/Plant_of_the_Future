import unittest
import json
from POFWebpage.UserClass import User
from POFWebpage.mgdb import POFDB
import hashlib, os, binascii

class TestMgDBClass(unittest.TestCase):
    
    def setUp(self):
        self.testUser1 = User("Ben", "bc@gmail.com", "PassWord")
        self.testUser2 = User("NonExisting", "bh@bmail.com", "12345", "1234", True)
        self.testDB = POFDB()
        self.testDB.userCollection.delete_one({"_id" : "NonExisting"})

      

    #check initializtion of db and make sure db class is filled
    def testDBInitializationConnectionCorrect(self):
        self.assertIsInstance(self.testDB,POFDB)

    
    #check if user exists given user does not exist in the db currently
    def testCheckForUserNotExists(self):
        self.assertEqual(False, self.testDB.checkForUser(self.testUser2.getUserName()))

    #try to add a user given the user does not exist
    def testAddUserNotExists(self):
        self.assertEqual(True, self.testDB.addUser(self.testUser2.userToJson())) 

    #try to delete a user from the db given the user does exist
    def testDeleteUserExists(self):
        self.testDB.userCollection.insert_one({
            "_id" : "NonExisting",
            "email": "bh@bmail.com",
            "password": "12345",
            "salt": "1234"
         })
        self.assertEqual(True, self.testDB.deleteUser('NonExisting')) 
    
    #try to add a user given the user exists
    def testAddUserExists(self):
        self.testDB.userCollection.insert_one({
            "_id" : "NonExisting",
            "email": "bh@bmail.com",
            "password": "12345",
            "salt": "1234"
         })
        self.assertEqual(False, self.testDB.addUser(self.testUser2.userToJson()))

    #check if user exists when given a user that does exist
    def testCheckForUserExists(self):
        self.testDB.userCollection.insert_one({
            "_id" : "NonExisting",
            "email": "bh@bmail.com",
            "password": "12345",
            "salt": "1234"
         })
        self.assertEqual(True, self.testDB.checkForUser(self.testUser2.getUserName())) 

    ######below is not done
    #try to get user from db given the user exists
    def testGetUserExists(self):
        self.testDB.userCollection.insert_one({
            "_id" : "NonExisting",
            "email": "bh@bmail.com",
            "password": "12345",
            "salt": "1234"
         })
        self.assertEqual(self.testDB.getUser(self.testUser2.getUserName())['_id'], 'NonExisting') 

   
    #try to delete a user from the db given the user does not exist
    def testDeleteUserNotExists(self):
        self.assertEqual(False, self.testDB.deleteUser(self.testUser2.getUserName())) 
 
    #try to get a user from the db given the user does not exist
    def testGetUserNotExists(self):
        self.assertEqual(False, self.testDB.getUser(self.testUser2.getUserName())) 
    
if __name__ == '__main__':

    print("running")
    unittest.main()
