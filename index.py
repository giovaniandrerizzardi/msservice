from processors import decoder, interscityManager
from flask import Flask, request
from flask_restful import Resource, Api
from processors import model, interscityManager

app = Flask(__name__)
api = Api(app)

todos = {}


class Test(Resource):
    def post(self):
        
        json_data = request.get_json(force=True)
        print(json_data)
        return {}


api.add_resource(Test, '/cadastroRecurso')

if __name__ == '__main__':
    app.run(debug=True, port=4501)
