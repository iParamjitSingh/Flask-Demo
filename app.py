from flask import Flask, request, jsonify, send_file
import matplotlib.pyplot as plt
from io import BytesIO

app = Flask(__name__)

@app.route('/route', methods=['GET'])
def route():
    src = request.args.get('src', 'Earth')  # Default value for src parameter is 'Earth'
    dest = request.args.get('dest', 'World')  # Default value for dest parameter is 'World'
    return jsonify({'message': f'Hello, from {src} to {dest}!'})
    
# @app.route('/plotGraph')
# def plotGraph():
#     # Generate the figure **without using pyplot**.
#     fig = plot_Graph()

#     # Save the plot as a temporary image file
#     img_buffer = BytesIO()
#     fig.savefig(img_buffer, format='png')
#     img_buffer.seek(0)

#     # Clear the plot to release memory
#     fig.clf()

#     # Return the image file as a response
#     return send_file(img_buffer, mimetype='image/png')

@app.route("/")
def start():
    return "The IRROS Server is Running"
