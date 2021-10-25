import requests

response = requests.post('http://127.0.0.1:5000/', json={"title": "First web task"})
response = requests.post('http://127.0.0.1:5000/', json={"title": "Second web task"})
#print(response)
response.json()