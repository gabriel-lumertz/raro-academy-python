from flask import Flask, request, jsonify
import requests

BASE_URL = 'https://jsonplaceholder.typicode.com/posts'

app = Flask(__name__)

@app.route('/items', methods=['GET'])
def get_items():

    response = requests.get(BASE_URL)

    return jsonify(response.json()), response.status_code

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):

    response = requests.get(f'{BASE_URL}/{item_id}')

    return jsonify(response.json()), response.status_code

@app.route('/items', methods=['POST'])
def create_item():
    
    data = request.json

    response = requests.post(BASE_URL, json=data)

    return jsonify(response.json()), response.status_code

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    
    data = request.json

    response = requests.put(f'{BASE_URL}/{item_id}', json=data)

    return jsonify(response.json()), response.status_code

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    
    response = requests.delete(f'{BASE_URL}/{item_id}')

    if response.status_code == 200:
        return '', 204

if __name__ == '__main__':
    app.run(debug=True)