# Types of Web APIs:
# SOAP - Focus on strict and formal API design
#      - Enterprise applications
#
# REST - Focus on simplicity & scalability
#      - Most common API architecture
#
# GraphQL - Focus on flexibility
#         - Optimized for performance

# urllib module
# - Bundled with Python
# - Powerful module but not very developer-friendly
from urllib.request import urlopen
api = "http://api.music-catalog.com/"

with urlopen(api) as response:
    data = response.read()
    string = data.decode()
    print(string)

# requests package
# - Many powerful built-in features
# - Easier to use
import requests 
api = "http://api.music-catalog.com/"

response = requests.get(api)
print(response.text)

#methods:
# .get() - retrieve a resource
# 
# .post() - create a resource
# 
# .put() - update an existing resource
# 
# .delete() - remove a resource

#URLs 
# URL - Uniform Resource Locator
# The structured address to an API Resource
# Customize the URL to interact with specific API Resources
# 
# example: http://350.5th-ave.com/unit/243?floor=77
# breakdown -
# (http://) Protocol - the means of transportation
# (350.5th-ave.com) Domain - the street address of the office building
# (:80) Port - the gate or door to use when entering the building
# (/unit/243) Path - the specific office unit inside the building
# (?floor=77) Query - any additional instructions

# adding query parameters with requests:
# append to the url string -
#response = requests.get('http://350.5th-ave.com/unit/243?floor=77&elevator=True')
#print(response.url)
# 
# Use the params argument to add query parameters -
#query_params = {'floor':77, 'elevator':True}
#response = requests.get('http://350.5th-ave.com/unit/243', params=query_params)
#print(response.url)

# status codes:
# 70 status codes grouped into 5 categories
# status code categories - 
# 1XX - informational responses
# 2XX - successful responses
# 3XX - redirection messages
# 4XX - client error responses
# 5XX - server error responses
# 
# Freq. used status codes
# 200 - everythings good (requests.codes.ok)
# 404 - thing requested doesn't exist (requests.codes.not_found)
# 401 - unauthorized
# 500 - internal server error
# 
# Each response object has a status-code attribute which contains the numeric value of the status-code
response.status_code == 200
# Look-up status codes using the requests.codes
response = requests.get('https://api.datacamp.com/this/is/the/wrong/path')
response.status_code == requests.codes.not_found

# headers:
# headers contain information that describe the message or data being sent or received
# such as the type of content we are sending or the date the requested resource was last modified
# headers are always formatted as key-value pairs separated by a colon
# each header starts with a case-insensitive key, followed by a colon, and then the value of that header
# Adding headers to a request -
response = requests.get('http://api.datacamp.com',
                        headers ={'accept':'application/json'})
# Reading response headers
response.headers['content-type']
# or get method on dictionary
response.headers.get('content-type')

# authentication methods:
# add an authorization header
# method - basic authentication
requests.get('http://api.music-catalog.com', auth=('username','password'))
# method - API key/token authentication
# using query parameter ^
params = {'access_token': 'faaa1c97bd3f4bd9b024c708c979feca'}
requests.get('http://api.music-catalog.com/albums',params=params)
# adding a "Bearer" authorization header
headers = {'Authorization': 'Bearer faaa1c97bd3f4bd9b024c708c979feca'}
requests.get('http://api.music-catalog.com/albums', headers=headers)

#From Python to JSON and back:
import json #javascript object notation
#pythons built-in json package can encode(turn python code into json) and decode(the reverse)
album = {'id':42, 'title':"Back in Black"}
string = json.dumps(album) #Encodes a python object to a JSON string
album = json.loads(string) #Decodes a JSON string to a Python object

# Encoding and Decoding using the requests package
# 
# receive JSON data
# GET request with an accept header for JSON data
response = requests.get('http://api.music-catalog.com/lyrics',
                        headers={'accept':'application/json'})
# print the json text
print(response.text)
# decode into a python object
data = response.json()
print(data['artist'])

# sending JSON data
playlist = {'name':'Road trip','genre':'rock','private':'true'}
# add playlist using via the 'json' argument
response = requests.post("http://api.music-catalog.com/playlists", json=playlist)
# get the request object
request = response.request
# print the request content-type header
print(request.headers['content-type'])

#Error Handling:
# 4XX status code - Client Errors
# indicates the request from the client could not be handled properly
# common causes - bad requests, authentication failures, wrong header, etc.
# resolution - fix the request
# common status codes -
# 401 unauthorized - the rquest lacks valid authentication credentials for the requested resource
# 404 Not Found - Indicates that the server cannot find the resource that was requested
# 429 Too Many Requests - The client has sent too many requests in a given amount of time
#
# 5XX status code - Server Errors
# arises from problems on the server
# beyond the client's control
# common causes - server overloaded, server configuration errors, internal errors
# resolution - should be fixed by the API administrator
# Clients cannot resolve these errors but should address them in the code to prevent unexpected behavior or bugs
# common status codes -
# 500 Internal Server Error  - The server experienced an unexpected issue which prevents it from responding
# 502 Bad Gateway - The API server could not successfully reach another server it needed to cmoplete the response
# 504 Gateway Timeout - The server (which acts as a gateway) did not get a response from the upstream server in time
#
# Handling API errors
import requests

url = 'http://api.music-catalog.com/albums'

r = requests.get(url)
if r.status_code >= 400:
    print('oops something went wrong')
else:
    print('all good')
#
# Handling Connection errors
import requests
from requests.exceptions import ConnectionError
url=''

try:
    r = requests.get(url)
    print(r.status_code)
except ConnectionError as conn_err:
    print(f'Connection Error! {conn_err}.')
    print(conn_err)
#
#NOTE: use both techniques together! requests library makes this straight forward
#
# Handling API & Connection errors together with requests package
import requests
# 1: Import the requests library exceptions
from requests.exceptions import ConnectionError, HTTPError

try:
    r = requests.get('http://api.music-catalog.com/albums')
    # 2: Enable raising exceptions for returned error statuscodes
    r.raise_for_status()

    print(r.status_code)
# 3: Catch any connection errors
except ConnectionError as conn_err:
    print(f'Connection Error! {conn_err}.')

# 4: Catch error responses from the API server
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
 