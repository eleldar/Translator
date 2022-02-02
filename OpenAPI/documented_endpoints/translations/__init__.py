# documented_endpoints/translations/__init__.py
from flask import request
from flask_restplus import Namespace, Resource, fields
from api.translations import get_sentences

namespace = Namespace('translation', 'Translation')

translation_model = namespace.model('Translation source', {
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

return_model = namespace.model('Translation result', {
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
    @namespace.response(404, 'Directs error')
    @namespace.expect(translation_model)

    def post(self):
        '''POST'''
        try:
            req = request.json
            direct = f"{req['sourceLanguage']}-{req['targetLanguage']}"
            source = req['text']
            message = {
                'message': get_sentences(direct, source)
            }
            return message, 200
        except KeyError:
            return 'Directs error!', 404
