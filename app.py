from flask import Flask, make_response, jsonify
from model import db

app = Flask(__name__)


@app.route('/hello')
def hello_world():  # put application's code here
    return 'Hello World New!'


@app.route('/api/products', methods=['GET'])
def getAllProducts():  # put application's code here
    return make_response(jsonify({"products": db}), 200)

# Linux on ARM (linux/arm64)
# Linux on AMDX64 (linux/amd64)
# windows on AMD (windows/AMD64)

# Container Network Model

# LibNetwork

# Drivers




if __name__ == '__main__':
    app.run()
