# documented_endpoints/__init__.py
from flask import Blueprint
from flask_restplus import Api
from documented_endpoints.translations import namespace as translations_ns

blueprint = Blueprint('api', __name__, url_prefix='/api')

api_extension = Api(
    blueprint,
    title='NLP',
    version='0.1',
    description='OpenApi for NLP applications',
    doc='/'
)

api_extension.add_namespace(translations_ns)
