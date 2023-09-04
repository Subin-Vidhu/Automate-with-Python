# A Python module for network requets
import requests

# API URL
url = 'https://dummyjson.com/products'

# Get data from API
response = requests.get(url)

# Show data to screen
print(response.text)

