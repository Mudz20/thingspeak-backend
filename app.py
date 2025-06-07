from flask import Flask, render_template, jsonify
import requests
import os
from flask_cors import CORS  # Import CORS for handling cross-origin requests

app = Flask(__name__)

# Enable CORS for all routes (so that frontend can access the API from different origins)
CORS(app)

# Replace with your ThingSpeak channel details
CHANNEL_ID = "2983435"  # Your ThingSpeak channel ID
READ_API_KEY = "1MT14J6BGB42VCPD"  # Your ThingSpeak read API key

# URL to fetch data from ThingSpeak
url = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?api_key={READ_API_KEY}&results=10"

@app.route('/')
def index():
    # Serve the index.html page
    return render_template('index.html')  # Assuming the HTML file is in the 'templates' folder

@app.route('/api/data')
def get_data():
    # Fetch data from ThingSpeak
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return jsonify(data)  # Return the data as JSON for frontend to use
    else:
        return jsonify({'error': 'Failed to fetch data from ThingSpeak'}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use the default port 5000
    app.run(host='0.0.0.0', port=port)  # Run the app on all available network interfaces
