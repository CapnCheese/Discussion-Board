import os

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

#variables
history = []
message_id = 0

@app.route("/", methods=["POST", "GET"])
def main_page():
    return render_template("main.html")

@app.route("/main", methods=["POST", "GET"])
def main():
    data = request.get_json()
    message = data.get("message")
    user = data.get("user")
    global message_id
    
    history.append({
        "id" : message_id,
        "user": user,
        "message": message
    })
    
    print(history)
    print(f"id: {message_id}")
    message_id += 1
    return jsonify(success=True)

@app.route("/get_data", methods=["POST", "GET"])
def get_data():
    return jsonify(history)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")