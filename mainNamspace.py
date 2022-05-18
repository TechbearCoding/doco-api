from flask_restx import Namespace, Resource, fields
from flask import request
from mailmerge import MailMerge


api = Namespace('Document fill', description='Fill data')
template = "contract.docx"


model = api.model('Resource', {
    'name': fields.String,
    'lastName': fields.String
})

@api.route('/check')
class Checker(Resource):
    def get(self):
        return 'It works!'

@api.route('/fill')
class Filler(Resource):
    @api.expect(model)
    def post(self):
        item = api.payload

        firstName = item['name']
        lastName =  item['lastName']

        document = MailMerge(template)
        document.merge(Name = firstName + ' ' + lastName)
        document.write('test-output.docx')
        return firstName + ' ' + lastName

