import requests


response = requests.get("https://randomuser.me/api/")
#print(response.text)

response = requests.get("https://api.thecatapi.com/")
response.text
#print(response.text)

response = requests.get("https://api.thecatapi.com/v1/breeds")
response.text
#print(response.text)


response = requests.get("https://api.thecatapi.com/v1/breeds")
print(response.status_code) # 200 -> able to comunicate
print(response.headers)
request = response.request
print(request.url)

