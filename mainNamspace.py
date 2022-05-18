from flask_restx import Namespace, Resource, reqparse
from flask import request
from mailmerge import MailMerge


api = Namespace('Document fill', description='Fill data')
template = "contract.doc"


parser = reqparse.RequestParser()
parser.add_argument('firstName', type=str, help='name')
parser.add_argument('lastName', type=str, help='last names')


@api.route('/check')
class Checker(Resource):
    def get(self):
        return 'It works!'

@api.route('/fill')
class Filler(Resource):
    @api.doc(parser=parser)
    def post(self):
        args = parser.parse_args()
        firstName = args['firstName']
        lastName = args['lastName'] 
        document = MailMerge(template)
        document.merge(Name = firstName + ' ' + lastName)
        document.write('test-output.docx')
        return firstName + ' ' + lastName

