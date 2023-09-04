# A Python module for network requets
import requests
import json

# API URL
url = 'https://dummyjson.com/products'

# Get data from API
response = requests.get(url)

# load json data
data = json.loads(response.text)
for item in data["products"]:
    print(item)

