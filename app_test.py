import requests
import pandas as pd
from datetime import datetime

# Sample data
sample_data = {
    'temperature': 6.559,
    'humidity': 73.8,
    'wind_speed': 0.083,
    'general_diffuse_flows': 0.051,
    'diffuse_flows': 0.119,
    'zone': 'zone_2',
    'timestamp': datetime.strptime("2017-01-01 00:30:00", '%Y-%m-%d %H:%M:%S'),
}

# URL of your Flask app's endpoint
url = 'http://127.0.0.1:5000/submit_data'

# Send the POST request with the sample data
response = requests.post(url, params=sample_data)

# Check the response status
if response.status_code == 200:
    print("POST request successful!", response.json())
else:
    print("POST request failed.")
