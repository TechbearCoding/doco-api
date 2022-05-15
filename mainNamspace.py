from flask_restx import Namespace, Resource, reqparse #tiek importēti moduļi
import sqlite3 as sqlite #import sqllite

api = Namespace('Document fill', description='Fill data')


@api.route('/check')
class Checker(Resource):
    def get(self):
        return 'It works!'

# @api.route('/fill')
# class Filler(Resource):
#     def post()

