from flask import Flask, request, jsonify

app = Flask(__name__)

data = {
    "temperature": 0,
    "humidity": 0
}

@app.route('/data', methods=['POST'])
def receive_data():
    global data
    data = request.json
    return jsonify({"status": "success"}), 200

@app.route('/data', methods=['GET'])
def send_data():
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
