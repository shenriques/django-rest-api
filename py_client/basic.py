import requests

endpoint = "http://localhost:8000/api/"
get_response = requests.post(endpoint, json={'title': 'crockus bag', 'content': 'i see black', 'price': '10'})
print(get_response.json()) 