# main.py
import os
from flask import Flask
from documented_endpoints import blueprint as documented_endpoint

app = Flask(__name__)
app.config['RESTPLUS_MASK_SWAGGER'] = False

app.register_blueprint(documented_endpoint)

if __name__ == "__main__":
    os.environ["TRANSFORMERS_OFFLINE"] = "1"
    app.run(host='0.0.0.0', port='8888')
