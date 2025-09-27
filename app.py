from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

# Temporary "database"
users = []

# Serve index.html as homepage
@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

# Serve all HTML files from root (fine folder)
@app.route('/<path:filename>')
def serve_html(filename):
    return send_from_directory('.', filename)

# =============================
# API ROUTES
# =============================

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    users.append({
        "fname": data.get("fname"),
        "lname": data.get("lname"),
        "email": data.get("email"),
        "username": data.get("username"),
        "password": data.get("password"),
        "address": "",
        "district": "",
        "mobile": ""
    })
    return jsonify({"message": "User registered successfully!"})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    for user in users:
        if user["username"] == data.get("username") and user["password"] == data.get("password"):
            return jsonify({"message": "Login successful!", "user": user})
    return jsonify({"message": "Invalid credentials"}), 401

@app.route('/update', methods=['POST'])
def update():
    data = request.json
    for user in users:
        if user["username"] == data.get("username"):
            user["address"] = data.get("address")
            user["district"] = data.get("district")
            user["mobile"] = data.get("mobile")
            return jsonify({"message": "Profile updated!", "user": user})
    return jsonify({"message": "User not found"}), 404

@app.route('/customers', methods=['GET'])
def customers():
    return jsonify(users)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)