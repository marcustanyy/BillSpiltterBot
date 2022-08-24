from flask import Flask
from flask_restful import Resource, Api, reqparse
import ast

app = Flask(__name__)
api = Api(app)


class One(Resource):
    # methods go here
    def get(self):
        print("Users")
    
class Two(Resource):
    # methods go here
    def get(self):
        print("Locations")
    
api.add_resource(Users, '/users')  # '/users' is our entry point for Users
api.add_resource(Locations, '/locations')  # and '/locations' is our entry point for Locations

if __name__ == '__main__':
    app.run()  # run our Flask app