from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse, request
from model.astro_model import AstroModel

app = Flask(__name__)
api = Api(app)

class Astronauts(Resource):
    def get(self):
        print "getting data about number of astronauts in space"
        return #to be implemented (DAO class) by calling the model

    def post(self):
        print "posting Astronaut data"
        parser = reqparse.RequestParser()
        return #call the model and post data

    def delete(self):
        print "deleting all astronauts"
        #call the model to delete all astronauts

class Astronaut(Resource):
    def get(self, astroId):
        print "getting information about 1 Astronaut"
        #call the model to get a astronaut

    def delete(self, astroId):
        print "deleting an Astronaut with ID: " + repr(astroId)
        #call the model to delete a astronaut

    def put(self, astroId):
        print "updating an Astronaut with ID: " + repr(astroId)
        #call the model to update the astronaut

api.add_resource(Astronauts, '/astronauts')
api.add_resource(Astronaut, '/astronauts/<string:astroId>')

if __name__ == '__main__':
    app.run(host=0.0.0.0, port=5000, debug=True)
