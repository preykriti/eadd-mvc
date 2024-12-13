from flask import Flask, request, jsonify
import os
from flask_cors import CORS
from models import getTodo

app = Flask(__name__)
CORS(app)

@app.route('/mytask', methods=['GET'])
def home():
    todos = getTodo()
    todoData = [{"title": todo.title} for todo in todos]
    return jsonify(todoData)

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)