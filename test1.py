import os
import requests

api_key = os.environ.get("API_KEY")
url = "https://example.com/api/data"

response = requests.get(url, headers={"Authorization": f"Bearer {api_key}"})

if response.status_code == 200:
    print("Data fetched successfully!")
else:
    print("Failed to fetch data")
