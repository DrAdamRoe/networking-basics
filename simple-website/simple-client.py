
import http.client

# create the connection to the server
connection = http.client.HTTPConnection("127.0.0.1" , 65432)

# send a get request to the server
connection.request("GET","/")

# get the response object
response = connection.getresponse()

# print the server status
print(response.status, response.reason)

# print the http body, e.g. the html
print(response.read().decode())
