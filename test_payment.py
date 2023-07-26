from coinbase_commerce.client import Client

API_KEY = "4972e118-7236-45d5-9a31-af2af8606b6e"
client = Client(api_key=API_KEY)

import http.client
import json

conn = http.client.HTTPSConnection("api.commerce.coinbase.com")
payload = ''
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}
conn.request("GET", "/checkouts", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))