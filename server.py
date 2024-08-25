from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/bfhl', methods=['POST'])
def handle_post():
    data = request.json.get('data', [])
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]
    highest_lowercase_alphabet = sorted([char for char in alphabets if char.islower()], reverse=True)[:1]
    
    response = {
        "is_success": True,
        "user_id": "Nivesh_Potu_07082003",
        "email": "nivesh.potu2021@vitstudent.ac.in",
        "roll_number": "21BCE3058",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": highest_lowercase_alphabet
    }
    
    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(debug=True)