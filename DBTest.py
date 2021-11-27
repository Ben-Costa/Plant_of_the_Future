import unittest
import json
from POFWebpage.UserClass import User
from POFWebpage.mgdb import POFDB
import hashlib, os, binascii

class TestMgDBClass(unittest.TestCase):
    
    #check initializtion of db and make sure db class is filled
    def testDBInitializationConnectionCorrect(self):
        pass

    #check if user exists when given a user that does exist
    def testCheckForUserExists(self):
        pass  

    #check if user ecists given user does not exist in the db currently
    def testCheckForUserNotExists(self):
        pass

    #try to delete a user from the db given the user does not exist
    def testDeleteUserNotExists(self):
        pass
    
    #try to delete a user from the db given the user does exist
    def testDeleteUserExists(self):
        pass    
    
    #try to add a user given the user exists
    def testAddUserExists(self):
        pass   

    #try to add a user given the user does not exist
    def testAddUserNotExists(self):
        pass

    #try to get user from db given the user exists
    def testGetUserExists(self):
        pass   

    #try to get a user from the db given the user does not exist
    def testGetUserNotExists(self):
        pass      
    
if __name__ == '__main__':

    print("running")
    unittest.main()
