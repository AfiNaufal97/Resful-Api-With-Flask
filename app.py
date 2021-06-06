from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

identitas = {}

class ContohApi(Resource):
    def get(self):
        # result = {"message" : "Aplikasi pertama saya dengan flask"}
        return identitas
    
    def post(this):
        id = request.form["id"]
        text = request.form["text"]
        identitas["id"] = id
        identitas["text"] = text
        response = {"message" : "Sukses Ditambahkan"} 
        return response

api.add_resource(ContohApi, "/my", methods=["GET", "POST"])
if __name__ == "__main__":
    app.run(debug=True, port = 5005)