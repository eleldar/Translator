# documented_endpoints/translations/__init__.py
from flask import request
from flask_restplus import Namespace, Resource, fields

namespace = Namespace('translation', 'Translation')

translation_model = namespace.model('Translation', {
    'text': fields.String(
        required=True,
        description='Text for translation'
    ),
    'sourceLanguage': fields.String(
        required=True,
        description='Source languge ID'
    ),
    'targetLanguage': fields.String(
        required=True,
        description='Sourse language ID'
    ),
    'message': fields.String(
     #   required=True,
        readonly=True,
        description='Translated text'
    ),
})


@namespace.route('')
class translations(Resource):
    '''POST'''

    @namespace.expect(translation_model)
    @namespace.marshal_with(translation_model)
    def post(self):
        '''POST'''
        translation_example = {
            'text': 'text',
            'sourceLanguage': 'sourceLanguage',
            'targetLanguage': 'targetLanguage',
            'message': 'Translated text'
        }

        return translation_example, 200
