# main.py
import os
from flask import Flask
from argparse import ArgumentParser
from documented_endpoints import blueprint as documented_endpoint

app = Flask(__name__)
app.config['RESTPLUS_MASK_SWAGGER'] = False

app.register_blueprint(documented_endpoint)

if __name__ == "__main__":
    default_port = '8888'
    parser = ArgumentParser()
    parser.add_argument(
        "-p", "--port", dest="port", default=default_port,
        help=f'Enter connect port; default="{default_port}"'
    )
    args = parser.parse_args()
    os.environ["TRANSFORMERS_OFFLINE"] = "1"
    app.run(host='0.0.0.0', port=args.port)
