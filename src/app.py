from flask import Flask, jsonify
from flask import request
app = Flask(__name__)
import json

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]


@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    todos.append(request_body)
    print("Incoming request with the following body", request_body)
    json_text2 = jsonify('Response for the POST todo')
    return jsonify(todos)


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(1)
    print("This is the position to delete: ",position)
    return jsonify(todos)

    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)