import unittest
import json
from POFWebpage.UserClass import User
from POFWebpage.mgdb import POFDB

class TestMgDBClass(unittest.TestCase):
    
    def setUp(self):
        self.testUser1 = User("Ben", "bc@gmail.com", "PassWord")
        self.testUser2 = User("NonExisting", "bh@bmail.com", "12345", "1234", True)
        self.testDB = POFDB()
        self.testDB.userCollection.delete_one({"_id" : "NonExisting"})

      
    ###Registration Logic Testing###
    #check initializtion of db and make sure db class is filled
    def testRegistrationUserNotExist(self):
        if self.testDB.addUser(self.testUser2.userToJson()):
            self.assertEqual(self.testDB.checkForUser(self.testUser2.getUserName()), True)
        else:
            self.assertEqual(self.testDB.checkForUser(self.testUser2.getUserName()), False)

    def testRegistrationUserExist(self):
        self.testDB.userCollection.insert_one({
            "_id" : "NonExisting",
            "email": "b@bmail.com",
            "password": self.testUser2.getPassword(),
            "salt": "1234"
         })
        if self.testDB.addUser(self.testUser2.userToJson()):
            self.assertEqual(self.testDB.checkForUser(self.testUser2.getUserName()), True)
        else:
            tempUser = User.jsonToUser(self.testDB.getUser(self.testUser2.getUserName()))
            self.assertEqual(tempUser.getEmail(), "b@bmail.com")


if __name__ == '__main__':

    print("Running Website Logic Integration Testing")
    unittest.main()
