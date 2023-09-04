API (notes)
API stands for Application Programming Interface. It's like a set of instructions that a computer can use to do things. For example, if you wanted to order a pizza online, the website you use would send instructions to the pizza shop using an API. The pizza shop would then use the instructions to make and deliver the pizza.

Almost every popular website has an API, and you can use Python to interact with it.

Some popular websites that have an API are: Facebook, Twitter, Yelp, Google Maps, Stripe, Twilio, Amazon, YouTube, Flickr, Spotify, Dropbox, PayPal, MailChimp, SendGrid, Ebay, Foursquare and LinkedIn.

How to use an API
While these websites look totally different, the API you can use simply sends textual data. So you can easily use it in your Python program.

# A Python module for network requets
import requests
 
# API URL
url = 'https://dummyjson.com/products'
 
# Get data from API
response = requests.get(url)
 
# Show data to screen
print(response.text)
Data returned from an API is often in JSON format. Let's see an example of how you can parse JSON with Pyton:

import json
 
# Load JSON data
data = json.loads(json_data)
 
# Iterate through the data
for item in data:
    # Display the item name
    print(item['name'])
    # Display the item description
    print(item['description'])
That's it! Simple right?



Let's do an API request, then parse the JSON data and show product information:

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
That outputs every product as a JSON object. To list only the product names you can do this:

for item in data["products"]:
    print(item['title'])
Keep in mind that how you use the JSON data, depends on the JSON returned by the API.



When you get data from an API, the action is called an HTTP GET request. Besides getting data from an API, sometimes you want to send data to an API. That's called an HTTP POST request.

This is how you can do an HTTP POST request with Python:

import requests
 
url = 'http://example.com/post'
data = {'data': 'value'}
 
r = requests.post(url, data=data)
 
print(r.text)
To use an API, you often need an API key. You can almost always get the API key you need directly from the companies website. The key is used to authenticate to the company.



Weather API
Let build an example of that, a program that gets the weather for London, United Kingdom. It uses the OpenWeatherMap API, which provides access to current weather data, forecasts, and historical data. To use the OpenWeatherMap API, you will need to sign up for a free API key. Once you have your API key, you can use the requests library in Python to make calls to the API and retrieve the data you need.

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
Here the API key is directly written into the URL. Of course, it's a better practice to put the API key in it's own variable.

import requests
 
# Set up your API key
api_key = 'YOUR_API_KEY'
 
# Set up the city you want to get the weather for
city = 'London'
 
# Make the API call
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city, api_key)
response = requests.get(url)
 
# Get the data from the response
data = response.json()
 
# Print out the current temperature
print(data['main']['temp'])