from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__, template_folder="templates")

# Temporary "database"
users = []

@app.route('/',methods=['GET','HEAD'])
def home():
    return render_template("index.html")   # open home page

@app.route('/register-page')
def register_page():
    return render_template("reg.html")

@app.route('/login-page')
def login_page():
    return render_template("login.html")

@app.route('/profile-page')
def profile_page():
    return render_template("profile.html")

@app.route('/customer-page')
def customer_page():
    return render_template("customerdetails.html")

@app.route('/cart-page')
def cart_page():
    return render_template("cart.html")

# =============================
# YOUR OLD API ROUTES BELOW
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
    app.run(debug=True)