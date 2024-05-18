import random
import string

from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# A list of words
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "ice", "jackfruit", "kiwi", "lemon", "mango", "nectarine", "orange", "pineapple", "quince", "raspberry", "strawberry", "tangerine", "ugli", "victoria", "watermelon", "xigua", "yellow", "zucchini"]


@app.route('/data', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and file.filename.endswith('.zip'):
        file.save(os.path.join('/home/cveta/Uni/2.Semester/CN/dummyBE/', file.filename))
        print('File saved successfully!')
        return jsonify({'message': 'File successfully uploaded'}), 200
    else:
        return jsonify({'error': 'Unsupported file type'}), 400


@app.route('/infer', methods=['POST'])
def classify():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    file.save(os.path.join('/home/cveta/Uni/2.Semester/CN/dummyBE/', file.filename))
    # Generate a random string of length 10
    random_string = random.choice(words)

    return random_string, 200

@app.route('/training', methods=['POST'])
def starttraining():
    return jsonify({'message': 'OK'}), 200

@app.route('/serving', methods=['POST'])
def startserving():
    return jsonify({'message': 'OK'}), 200

@app.route('/serving', methods=['DELETE'])
def stopserving():
    return jsonify({'message': 'OK'}), 200

if __name__ == '__main__':
    app.run(debug=True)
