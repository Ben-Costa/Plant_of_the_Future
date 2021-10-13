from flask import Flask, jsonify

class User:

    def __init__(self, first_name, last_name, email, password, organization):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email    
        self.first_name = first_name
        self.password = password    
        self.organization = organization    

        #pass to database to make sure doesnt exist

        #if exists return error

        #if not return user successfully created
    
    
    def user_to_json(self):

        user_Dict = {
            "email": self.email,
            "password": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "organization": self.organization
         }

        return jsonify(user_Dict), 200



    def json_to_user(self):
        pass

    def check_existance(self):
        pass