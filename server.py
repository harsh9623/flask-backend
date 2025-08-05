from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask on Render!"

@app.route('/api/data')
def get_data():
    return jsonify({"message": "This is data from your Flask API!"})

if __name__ == '__main__':
    app.run()
