import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/api/auth/"
# get credentials from command line
username = input("Username: ")
password = getpass()

# get a token 
auth_response = requests.post(auth_endpoint, json={'username': username, 'password': password})
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        "Authorization": f"Token {token}"
    }
    endpoint = "http://localhost:8000/api/products/"
    get_response = requests.get(endpoint, headers=headers)
    
    data = get_response.json()
    next_url = data['next']
    results = data['results']

    print(next_url)
    print(results)
    
    # how to loop through pagination
    # if next_url is not None:
    #     get_response = requests.get(next_url, headers=headers)

