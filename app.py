'''
Registration of a user 0 tokens.
Each user gets 10 tokens.
Store a sentecne on our database for 1 token.
Retrieve his stored sentence on out database for 1 token.
'''

# Import modules and packages
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt


# Define App Architecture
app = Flask(__name__)
api = Api(app)

client = MongoClient('mongodb://db:27017')
db = client.SentenceDatabase

users = db['Users']


def verifyPw(username, password):
    hashed_pw = users.find({
        'Username' : username
        })[0]['Password']

    if bcrypt.hashpw(password.encode('utf8'), hashed_pw) == hashed_pw:
        return True

    else:
        return False


def countTokens(username):

    tokens = users.find({
        'Username' : username
        })[0]['Tokens']

    return tokens


# Classes
class Register(Resource):

    def post(self):

        # Step 1: get posted data by the user.
        postedData = request.get_json()

        # Get the data
        username = postedData['username']
        password = postedData['password']   #'123xyz'

        hashed_pw = hashed = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

        # Store username and pw into the database
        users.insert({
            'Username' : username,
            'Password' : hashed_pw,
            'Sentence' : '',
            'Tokens' : 10
            })

        retJson = {
            'status' : 200,
            'msg' : 'You succesfully signed-up for the API as {}'.format(username)
        }

        return jsonify(retJson)


class Store(Resource):

    def post(self):

        # Step 1. Get the posted data
        postedData = request.get_json()

        # Step 2. Read the data
        username = postedData['username']
        password = postedData['password']
        sentence = postedData['sentence']

        # Step 3. Verify the username password match
        correct_pw = verifyPw(username, password)

        if not correct_pw:

            retJson = {
                'status' : 302
            }

            return jsonify(retJson)

        # Step 4. Verify user has enough tokens
        num_tokens = countTokens(username)

        if not num_tokens <= 0:

            retJson = {
                'status' : 301
            }

            return jsonify(retJson)

        # Step 5. Store the sentence, take tokens away and return 200 response
        users.update({
            'Username' : username
            }, {
                '$set' : {
                    "Sentence" : sentence,
                    "Tokens" : num_tokens - 1}
            })

        retJson = {
            'status' : 200,
            'msg' : 'Sentence saved successfuly.'
        }

        return jsonify(retJson)


class Get(Resource):

    def post(self):

        postedData = request.get_json()

        username = postedData['username']
        password = postedData['password']

        # Verify the username password match
        correct_pw = verifyPw(username, password)

        if not correct_pw:

            retJson = {
                'status' : 302
            }

            return jsonify(retJson)

        # Verify user has enough tokens
        num_tokens = countTokens(username)

        if not num_tokens <= 0:

            retJson = {
                'status' : 301
            }

            return jsonify(retJson)

        # Make the user pay!
        users.update({
            'Username' : username
            }, {
                '$set' : {
                    'Tokens' : num_tokens - 1
                }
            })


        sentence = users.find({
            'Username' : username
            })[0]['Sentence']


        retJson = {
            'status' : 200,
            'sentence' : sentence
        }

        return jsonify(retJson)


api.add_resource(Register, '/register')
api.add_resource(Store, '/store')
api.add_resource(Get, '/get')


if __name__ == '__main__':
    app.run(host = '0.0.0.0')