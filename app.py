from flask import Flask, jsonify           # import flask
from service import ParamService

import json

app = Flask(__name__)             # create an app instance

@app.route("/")                   # at the end point /
def hello():                      # call method hello
    return "Hello World!"         # which returns "hello world"`

@app.route("/health")
def health():
    return "200"

@app.route("/list", methods=["GET"])
def list_params():
    return jsonify(ParamService().list())

if __name__ == "__main__":        # on running python app.py
    app.run()                   # run the flask app
    # app.run(debug=True)           # run the flask app using debugger