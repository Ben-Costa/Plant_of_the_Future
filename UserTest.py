import unittest
import json
from POFWebpage.UserClass import User
from POFWebpage.mgdb import POFDB
import hashlib, os, binascii

class TestUserClass(unittest.TestCase):

    ####11/22/notes:
    #need to ensure that the salt and the password both end up in the same type- getting an error in passhashword where it is trying to turn a btye into a byte 
    #and it doesnt like that

    def setUp(self):
        self.testUser1 = User("Ben", "bc@gmail.com", "PassWord")
        self.testUser2 = User("Ben2", "bc@gmail.com", 'PassWord', '1234', True)
        #self.testUser2Password = self.testUser2.hashUserPassword()
        #self.dbTest = POFDB()

    def testCreateUserWithoutSalt(self):
        #test created user1 without salt argument if is a user class
        self.assertIsInstance(self.testUser1, User)

    def testCreateUserWithSalt(self):
        #test created user2 with salt if is a user class
        self.assertIsInstance(self.testUser2, User)

    def testUser2Info(self):
        #print(self.testUser1)
        pass

    def testHashUserPasswordRightInfo(self):
        self.assertEqual(self.testUser2.password,binascii.hexlify(hashlib.pbkdf2_hmac('sha256',b'PassWord', b'1234', 100000)).decode('utf-8'))

    def testHashUserPasswordWrongInfo(self):
        self.assertNotEqual(self.testUser2.password,hashlib.pbkdf2_hmac('sha256',b'passWord', b'1234', 100000))

    def testcheckPassWordsMatchPositive(self):
        self.assertEqual(True, self.testUser2.checkPassWordsMatch('PassWord'))

    def testcheckPassWordsMatchNegative(self):
        self.assertEqual(False, self.testUser2.checkPassWordsMatch('assWord'))    

    #test userToJson
    def testuserToJson(self):
        test_json = {"_id": "Ben2", "email": "bc@gmail.com", "password": self.testUser2.password, "salt": binascii.hexlify(b'1234').decode('utf-8')}
        #test_json2 = {"_id": "Ben2", "email": "bc@gmail.com", "password": binascii.hexlify(User.hashPassword('PassWord', '1234')).decode('utf-8'), "salt": binascii.hexlify(b'1234').decode('utf-8')} 

        self.assertEqual(self.testUser2.userToJson(),json.dumps(test_json))

    def testVerifyIfUserIsJsonIsUser(self):
        #send a json with all information to be a user
        test_dict = {"_id": "Ben2", "email": "bc@gmail.com", "password": self.testUser2.password, "salt": binascii.hexlify(b'1234').decode('utf-8')}
        test_json = json.dumps(test_dict)
        self.assertEqual(True, User.verifyIfJsonIsUser(test_json))

    def testVerifyIfUserIsJsonIsNotUserMisNamed(self):
        #send a json with not all information to be a user
        test_dict = {"_id": "Ben2", "EMAIL": "bc@gmail.com", "password":self.testUser2.password, "salt": binascii.hexlify(b'1234').decode('utf-8')}
        test_json = json.dumps(test_dict)
        self.assertEqual(False, User.verifyIfJsonIsUser(test_json))

    def testVerifyIfUserIsJsonIsNotUserMissingKey(self):
        #send a json with not all information to be a user
        test_dict = {"_id": "Ben2", "EMAIL": "bc@gmail.com", "password": self.testUser2.password}
        test_json = json.dumps(test_dict)
        self.assertEqual(False, User.verifyIfJsonIsUser(test_json))

    def testJsonToUserRightInfo(self):
        #attempt to create a user from json containing all needed info
        test_dict = {"_id": "Ben2", "email": "bc@gmail.com", "password": self.testUser2.password, "salt": binascii.hexlify(b'1234').decode('utf-8')}
        test_json = json.dumps(test_dict)
        self.assertIsInstance(User.jsonToUser(test_json), User)

    def testJsonToUserWrongInfo(self):
        #attempt to create a user from json not containing all needed info
        test_dict = {"_id": "Ben2", "password": self.testUser2.password, "salt": binascii.hexlify(b'1234').decode('utf-8')}
        test_json = json.dumps(test_dict)
        self.assertIsInstance(User.jsonToUser(test_json), str)      





if __name__ == '__main__':

    print("running")
    unittest.main()



    #for db class
    #test checkIfUserExistsInDB
    #def testcheckIfUserExistsInDbUserDoesNotExist(self):
        #check for username that does not exist in the database
    #    pass

    #def testcheckIfUserExistsInDbUserDoesNotExist(self):
        #check for username that does exist in the database
    #    pass

    #test checkPassWordsMatch
    #def testcheckPassWordsMatch(self):
    #    pass

    #test addUserToDB
    #def testAddUserToDbUserNotIn(self):
        #try to add a user that does not exist in the database yet
    #    pass

    #def testAddUserToDbUserIn(self):
        #try to add user that does exist in the database
    #    pass

    #test getUserFromDatabase
    #def testgetUserFromDatabaseNotIn(self):
        #try to get user with username that does not exist
    #    pass

    #def testgetUserFromDatabaseIn(self):
        #try to get user with username that does exist
    #    pass    