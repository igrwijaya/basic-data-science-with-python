from flask import Flask, jsonify
import re
from flask import request
from flasgger import Swagger, LazyString, LazyJSONEncoder
from flasgger import swag_from

app = Flask(__name__)

app.json_provider_class = LazyJSONEncoder
swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "API Spec for Data Processing and Modelling",
        "description": "Description of API Spec for Data Processing and Modelling",
        "version": "1.0.0"
    }
}

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'docs',
            'route': '/docs.json'
        }
    ],
    'static_url_path': '/flasgger_static',
    'swagger_ui': True,
    'specs_route': '/docs/'
}

swagger = Swagger(app, template=swagger_template, config=swagger_config)


@swag_from('docs/hello_world.yml', methods=['GET'])
@app.route('/', methods=['GET'])
def hello_world():
    json_response = {
        'description': 'Hello World Description',
        'data': 'Hello World'
    }

    response_data = jsonify(json_response)
    return response_data


@app.route('/my', methods=['GET'])
def hello_my_name():
    name = request.args.get("name")

    return "Hello, My Name is " + name


@swag_from('docs/text.yml', methods=['GET'])
@app.route('/text', methods=['GET'])
def text():
    json_response = {
        'status_code': 200,
        'description': 'Original Text',
        'data': 'Halo, Apa kabar semua?'
    }

    response_data = jsonify(json_response)

    return response_data


@swag_from('docs/text-clean.yml', methods=['GET'])
@app.route('/text-clean', methods=['GET'])
def text_clean():
    json_response = {
        'status_code': 200,
        'description': 'Original Text',
        'data': re.sub(r'[^a-zA-Z0-9]', ' ', 'Halo, Apa kabar semua?')
    }

    response_data = jsonify(json_response)

    return response_data


@swag_from('docs/text-clean-by-user.yml', methods=['POST'])
@app.route('/text-clean-by-user', methods=['POST'])
def text_clean_by_user():

    inputText = request.form.get('text')

    json_response = {
        'status_code': 200,
        'description': 'Original Text',
        'data': re.sub(r'[^a-zA-Z0-9]', ' ', inputText)
    }

    response_data = jsonify(json_response)

    return response_data


if __name__ == '__main__':
    app.run()
