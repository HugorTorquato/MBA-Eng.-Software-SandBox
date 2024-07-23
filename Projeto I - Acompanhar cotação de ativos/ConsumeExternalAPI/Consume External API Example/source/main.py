

import requests
response = requests.get("https://randomuser.me/api/")
print(response.text)

print(" \n")
import requests
response = requests.get("https://api.thecatapi.com/")
response.text
print(response.text)

print(" \n")
import requests
response = requests.get("https://api.thecatapi.com/v1/breeds")
response.text
print(response.text)

