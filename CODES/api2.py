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

for item in data["products"]:
    print(item['title'])


#
import requests
 
#Define the API endpoint
url = 'http://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=YOUR_API_KEY'
 
#Make the request to the API
response = requests.get(url)
 
#Parse the response
data = response.json()
 
#Access the data
temperature = data['main']['temp']
humidity = data['main']['humidity']
 
#Print the data
print('Temperature:', temperature)
print('Humidity:', humidity)