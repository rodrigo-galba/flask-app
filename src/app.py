from flask import Flask, jsonify, request
from service import ParamService
from user_service import UserService

import requests

app = Flask(__name__)


@app.route("/")
def hello():
    return 'Hello World!'


@app.route("/health")
def health():
    msg = "Current instances\n"
    response = requests.get('http://169.254.169.254/latest/meta-data/local-ipv4')
    return response.text


@app.route("/list", methods=["GET"])
def list_params():
    return jsonify(ParamService().list())


@app.route('/users', methods=['POST'])
def create():
    body = request.get_json()
    new_user = UserService().create(body)
    return jsonify(new_user)


@app.route('/users', methods=['GET'])
def list_users():
    list = UserService().list()
    return jsonify(list)


@app.route('/users', methods=['DELETE'])
def delete():
    user = UserService().delete()
    return jsonify(user)


if __name__ == "__main__":        # on running python app.py
    app.run(host="0.0.0.0")       # run the flask app
    # app.run(debug=True)         # run the flask app using debugger