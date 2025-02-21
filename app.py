from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['GET', 'POST'])
def bfhl_api():
    if request.method == 'GET':
        return jsonify({"operation_code": 1})

    elif request.method == 'POST':
        data = request.get_json()

         # Check if "data" key exists in the JSON request
        if not data or "data" not in data:
            return jsonify({"error": "Missing 'data' key in request body"}), 400
        
        # Extract numbers and alphabets
        numbers = [x for x in data["data"] if x.isdigit()]
        alphabets = [x for x in data["data"] if x.isalpha()]

        # Find highest alphabet (case insensitive)
        highest_alphabet = max(alphabets, key=lambda x: x.lower()) if alphabets else None
        
        response = {
            "is_success": True,
            "user_id": "YourName_DDMMYYYY",  # Replace with actual details
            "email": "your_college_email@example.com",
            "roll_number": "Your_Roll_Number",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": highest_alphabet,
        }
        return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
