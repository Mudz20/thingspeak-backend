
from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

# Replace with your actual values
CHANNEL_ID = "2983435"
READ_API_KEY = "1MT14J6BGB42VCPD"

@app.route('/api/data')
def get_data():
    url = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?api_key={READ_API_KEY}&results=10"
    response = requests.get(url)
    return jsonify(response.json())

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

