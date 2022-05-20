from flask import Flask
from flask_restx import Api
from pathlib import Path
from mainNamspace import api as ns 
from flask_cors import CORS

UPLOAD_FOLDER = Path(__file__).parent.absolute() 

api = Api(
    title='Document fill',
    version='1.0',
    description='Tool for auto filling contract ',
)
api.add_namespace(ns, path='/v1')

app = Flask(__name__)
CORS(app)
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)