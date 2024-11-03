import requests

# Example of replicating an API call
url = 'https://consumer-api.wolt.com/order-xp/v1/pages/checkout'
headers = {
    'Content-Type': 'application/json',
    'w-wolt-session-id': 'your-session-id',
    'x-wolt-visitor-id': 'your-visitor-id',
}

data = {
    "purchase_plan": {
        "delivery_method": "homedelivery",
        "preorder_time": "2024-11-02T13:29:48.293Z",
        "menu_items": [
            {
                "item_id": "item12345",  # Replace with a valid item ID
                "quantity": 1,
                "modifiers": []
            }
        ],
        "extra_fees": {
            "fees": 1050,
            "credits": 0,
            "discounts": -199
        }
    },
    "venue_id": "65cb91f86c40272ccf808e33"  # Ensure this venue ID is correct
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
