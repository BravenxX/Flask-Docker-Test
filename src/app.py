from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def ping():
    return jsonify({"respuesta": "Saludos"})


@app.route('/users', methods=['GET'])
def getUsers():
    return jsonify({"users": [{"user": "juan"}, {"user": "pedro"}]})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
