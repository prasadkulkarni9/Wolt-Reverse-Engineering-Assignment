import requests

# Define the endpoint URL
url = "https://restaurant-api.wolt.com/v1/pages/search"

# Define the headers for the request
headers = {
    "Accept": "application/json",
    "Accept-Language": "en",
    "App-Language": "en",
    "App-Locale": "en-US",
    "App-Currency-Format": "MeKArzIzNCw1NsKgwqQ=",
    "Client-Version": "24.42.0",
    "ClientVersionNumber": "132024420",
    "Platform": "Android",
    "User-Agent": "Wolt/24.42.0; Build/132024420; Android/7.0; Genymobile Phone; en",
    "UserLocationLat": "60.16759",
    "UserLocationLng": "24.941",
    "w-wolt-session-id": "d5c8fc7b-47ac-4720-a5fe-766fe4443f92",
    "x-wolt-visitor-id": "e073c048-3400-4de3-9a56-6da1451a9644",
    "Content-Type": "application/json; charset=UTF-8",
    "Content-Length": "50",
    "Connection": "close",
    "Accept-Encoding": "gzip, deflate"
}

# Define the payload (request body)
payload = {
    "q": "pet food",
    "lat": 60.1675867,
    "lon": 24.9409963
}

# Send the POST request
response = requests.post(url, headers=headers, json=payload)

# Check if the request was successful
if response.status_code == 200:
    # Print the JSON response
    print("Response:", response.json())
else:
    print("Error:", response.status_code, response.text)
