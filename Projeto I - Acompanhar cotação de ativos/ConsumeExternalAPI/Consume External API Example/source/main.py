import requests
import os
from dotenv import load_dotenv

response = requests.get("https://randomuser.me/api/")
#print(response.text)

response = requests.get("https://api.thecatapi.com/")
response.text
#print(response.text)

response = requests.get("https://api.thecatapi.com/v1/breeds")
response.text
#print(response.text)


response = requests.get("https://api.thecatapi.com/v1/breeds")
#print(response.status_code) # 200 -> able to comunicate
#print(response.headers)
request = response.request
#print(request.url)

# Example on how to protect an API key
load_dotenv()
api_key = os.getenv("API_KEY")
print(f'API Key: {str(api_key)}')

url = "https://brapi.dev/api/quote/PETR4"
params = {
    'token': {api_key},
}
 
response = requests.get(url, params=params)
 
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Request failed with status code {response.status_code}")
    print(f"{response.json()}")

