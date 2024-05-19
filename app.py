from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/route', methods=['GET'])
def greet():
    src = request.args.get('src', 'Earth')  # Default value for src parameter is 'Earth'
    dest = request.args.get('dest', 'World')  # Default value for dest parameter is 'World'
    return jsonify({'message': f'Hello, from {src} to {dest}!'})

@app.route("/")
def start():
    return "The IRROS Server is Running"
