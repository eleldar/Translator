# documented_endpoints/translations/__init__.py
from flask import request
from flask_restplus import Namespace, Resource, fields

namespace = Namespace('translation', 'Translation')

translation_model = namespace.model('Source', {
    'text': fields.String(
        required=True,
        description='Text for translation',
        example='Hello World!'
    ),
    'sourceLanguage': fields.String(
        required=True,
        description='Source languge ID',
        example='en'
    ),
    'targetLanguage': fields.String(
        required=True,
        description='Sourse language ID',
        example='ru'
    ),
})

return_model = namespace.model('Result', {
    'message': fields.String(
        readonly=True,
        description='Translated text',
        example='Привет Мир!'
    ),
})

@namespace.route('')
class translations(Resource):
    '''POST'''
    @namespace.response(200, 'Ok', model=return_model)
    @namespace.expect(translation_model)

    def post(self):
        '''POST'''
        translation_example = {
            'message': 'Translated text'
        }

        return translation_example, 200
