from flask_restx import Namespace, Resource, fields
from flask import request
from mailmerge import MailMerge


api = Namespace('Document fill', description='Fill data')
template = "contract.docx"


model = api.model('Resource', {
    'name': fields.String,
    'lastName': fields.String,
    'companyName': fields.String,
    'regNr': fields.String,
    'email': fields.String,
    'phone': fields.String,
    'address': fields.String,
    'bank': fields.String,
    'bankCode': fields.String,
    'accountNr': fields.String,
    'date': fields.String
})

# 2022.gada ___.decembrī

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
        document.merge(companyName = item['companyName'])
        document.merge(regNr = item['regNr'])
        document.merge(email = item['email'])
        document.merge(phone = item['phone'])
        document.merge(address = item['address'])
        document.merge(bank = item['bank'])
        document.merge(bankCode = item['bankCode'])
        document.merge(accountNr = item['accountNr'])
        document.merge(date = item['date'])
        document.write('test-output.docx')
        return firstName + ' ' + lastName

