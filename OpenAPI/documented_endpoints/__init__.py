# documented_endpoints/__init__.py
from flask import Blueprint
from flask_restplus import Api
from documented_endpoints.translations import namespace as translations_ns

blueprint = Blueprint('api', __name__, url_prefix='/api')

description =  'OpenApi for English - Russia translation.\n\n'
description += 'To translation you must use next directs:\n'
description += 'en-ru, where "en" - English, "ru" - Russian.'

api_extension = Api(
    blueprint,
    title = 'NLP',
    version = '0.2',
    description = description, 
    doc='/'
)

api_extension.add_namespace(translations_ns)
