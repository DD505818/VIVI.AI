
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/market_data', methods=['GET'])
def get_market_data():
    return jsonify({"message": "Market data endpoint is live!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
