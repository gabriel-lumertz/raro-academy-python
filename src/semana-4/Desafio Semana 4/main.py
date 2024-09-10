from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/items', methods=['GET'])
def get_items():
    # TODO: Implementar chamada à API pública
    pass

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    # TODO: Implementar chamada à API pública
    pass

@app.route('/items', methods=['POST'])
def create_item():
    data = request.json
    # TODO: Implementar chamada à API pública
    pass

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.json
    # TODO: Implementar chamada à API pública
    pass

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    # TODO: Implementar chamada à API pública
    pass

if __name__ == '__main__':
    app.run(debug=True)