from flask import Flask, jsonify

class User:

    def ceate_user(self):

        User = {
            "_id": "",
            "email": "",
            "password": "",
            "name": "",
            "organization": ""
         }

        return jsonify(User), 200

