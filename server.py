from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask on Render!"

@app.route('/api/data')
def get_data():
    return jsonify({"message": "This is data from your Flask API!"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
