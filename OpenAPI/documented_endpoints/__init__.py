# documented_endpoints/__init__.py
from flask import Blueprint
from flask_restplus import Api
from documented_endpoints.translations import namespace as translations_ns

blueprint = Blueprint('api', __name__, url_prefix='/api')

description =  'OpenApi for NLP applications.\n\n'
description += 'To translation you can use next directs:\n'
description += 'en-ru, ru-en, ar-ru, ru-ar, en-ar, ar-en,\n'
description += 'where "en" - English, "ru" - Russian, "ar" - Arabic'

api_extension = Api(
    blueprint,
    title = 'NLP',
    version = '0.1',
    description = description, 
    doc='/'
)

api_extension.add_namespace(translations_ns)
