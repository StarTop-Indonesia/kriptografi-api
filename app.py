from flask import Flask, request
from flask.wrappers import Response
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)

api = Api(app)

CORS(app)

class Modification(Resource):
    def get(self):
        response = {"msg":"Salam dari Binjai"}
        return response
    
    def post(self):
        type = request.form['type']
        if type == 'decrypt':
            raw_text = request.form['raw_text'] 
            processed_text = raw_text+' decrypted'
        else:
            raw_text = request.form['raw_text'] 
            processed_text = raw_text+' encrypted'

        
        response = {"msg": processed_text}
        return response

api.add_resource(Modification, "/api/modification", methods=["GET","POST"])

if __name__ == "__main__":
    app.run(debug=True, port=5005)