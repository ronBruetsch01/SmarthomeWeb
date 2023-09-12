import requests

endpoint = "http://127.0.0.1:8000/rest/rest_home/"

response = requests.get(endpoint,
                         params={"param1":"Berg"},
                           json={"query":"Hallo!"})

print(response.json())