from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Flask API is working!"

@app.route('/hello')
def hello():
    return jsonify({"message": "Hello from Render Flask!"})

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({"you_sent": data})
