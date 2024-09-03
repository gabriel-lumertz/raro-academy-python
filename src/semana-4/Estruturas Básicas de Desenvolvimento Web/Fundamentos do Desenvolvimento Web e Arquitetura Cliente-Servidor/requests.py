import requests
import json

url = "http://127.0.0.1:5000/users"

payload = json.dumps({
  "name": "Luan",
  "age": 29
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)