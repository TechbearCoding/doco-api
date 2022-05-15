import sqlite3 as sqlite
from flask import Flask
from flask_restx import Resource, Api


app = Flask(__name__)
api = Api(app)

@api.route('/check')
class Checker(Resource):
    def get(self):
        return 'It works!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
