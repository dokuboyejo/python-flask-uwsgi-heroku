from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world():
    return jsonify({'info': 'Hello, World!'}), 200
	

if __name__ == '__main__':
    app.run()