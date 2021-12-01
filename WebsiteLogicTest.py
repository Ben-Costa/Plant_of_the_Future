import unittest
import json
from POFWebpage.UserClass import User
from POFWebpage.mgdb import POFDB

class TestMgDBClass(unittest.TestCase):
    
    def setUp(self):
        self.testUser1 = User("Ben", "bc@gmail.com", "PassWord")
        self.testUser2 = User("NonExisting", "bh@bmail.com", "12345", "1234")
        self.testDB = POFDB()
        self.testDB.userCollection.delete_one({"_id" : "NonExisting"})

      

    #check initializtion of db and make sure db class is filled
    def testRegistrationUserNotExist(self):
        if self.testDB.addUser(self.testUser2.userToJson()):
            self.assertEqual(self.testDB.checkForUser(self.testUser2.getUserName()), True)
        else:
            self.assertEqual(self.testDB.checkForUser(self.testUser2.getUserName()), False)

    def testRegistrationUserExist(self):
        self.testDB.userCollection.insert_one({
            "_id" : "NonExisting",
            "email": "bh@bmail.com",
            "password": "12345",
            "salt": "1234"
         })
        if self.testDB.addUser(self.testUser2.userToJson()):
            self.assertEqual(self.testDB.checkForUser(self.testUser2.getUserName()), True)
        else:
            self.assertEqual(self.testDB.checkForUser(self.testUser2.getUserName()), False)


if __name__ == '__main__':

    print("running")
    unittest.main()
